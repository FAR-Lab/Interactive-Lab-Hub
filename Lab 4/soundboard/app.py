"""Six-slot soundboard: upload audio from a browser, play it by touching MPR121 pads.

Run on the Pi:   python app.py
Then open:       http://<pi-ip>:5000 from any device on the same network.

Pads 0-5 on the MPR121 play slots 1-6. If the sensor isn't connected (or you run
this on your laptop), the web side still works and you can test playback from it.
"""
import json
import os
import shutil
import subprocess
import threading
import time

from flask import Flask, abort, jsonify, request, send_file, send_from_directory
from werkzeug.utils import secure_filename

NUM_SLOTS = 6
HERE = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(HERE, "audio")
META_PATH = os.path.join(AUDIO_DIR, "slots.json")
ALLOWED_EXT = {".mp3", ".wav", ".ogg", ".m4a", ".aac", ".flac"}

os.makedirs(AUDIO_DIR, exist_ok=True)

app = Flask(__name__, static_folder=None)
app.config["MAX_CONTENT_LENGTH"] = 25 * 1024 * 1024  # 25 MB per upload

meta_lock = threading.Lock()


def load_meta():
    try:
        with open(META_PATH) as f:
            meta = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        meta = {}
    return {str(i): meta.get(str(i)) for i in range(1, NUM_SLOTS + 1)}


def save_meta(meta):
    tmp = META_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(meta, f, indent=2)
    os.replace(tmp, META_PATH)


def slot_path(slot):
    entry = load_meta().get(str(slot))
    return os.path.join(AUDIO_DIR, entry["file"]) if entry else None


def check_slot(slot):
    if not 1 <= slot <= NUM_SLOTS:
        abort(404)


# --- Playback -----------------------------------------------------------------

class Player:
    """Plays one file at a time; starting a new one stops the current one."""

    def __init__(self):
        self.proc = None
        self.slot = None
        self.lock = threading.Lock()
        self.cmd = self._find_player()

    @staticmethod
    def _find_player():
        if shutil.which("ffplay"):
            return ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet"]
        if shutil.which("afplay"):  # macOS, for testing on a laptop
            return ["afplay"]
        return None

    def play(self, slot):
        path = slot_path(slot)
        if not path or not os.path.exists(path):
            return False
        if not self.cmd:
            print("No audio player found. Install one with: sudo apt install ffmpeg")
            return False
        with self.lock:
            self._stop_locked()
            self.proc = subprocess.Popen(self.cmd + [path])
            self.slot = slot
        print(f"Playing slot {slot}")
        return True

    def stop(self):
        with self.lock:
            self._stop_locked()

    def _stop_locked(self):
        if self.proc and self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=1)
            except subprocess.TimeoutExpired:
                self.proc.kill()
        self.proc = None
        self.slot = None

    def now_playing(self):
        with self.lock:
            if self.proc and self.proc.poll() is None:
                return self.slot
            return None


player = Player()


# --- Touch sensor ---------------------------------------------------------------

sensor_status = {"connected": False, "error": None}


def touch_loop():
    try:
        import board
        import busio
        import adafruit_mpr121

        i2c = busio.I2C(board.SCL, board.SDA)
        mpr121 = adafruit_mpr121.MPR121(i2c)
    except Exception as e:  # no sensor, not on a Pi, or libraries missing
        sensor_status["error"] = str(e)
        print(f"Touch sensor not available ({e}). Web upload still works.")
        return

    sensor_status["connected"] = True
    print("MPR121 connected. Pads 0-5 play slots 1-6.")
    was_touched = [False] * NUM_SLOTS
    while True:
        for pad in range(NUM_SLOTS):
            touched = mpr121[pad].value
            if touched and not was_touched[pad]:  # trigger on the touch, not the hold
                player.play(pad + 1)
            was_touched[pad] = touched
        time.sleep(0.05)


# --- Routes --------------------------------------------------------------------

@app.get("/")
def index():
    return send_from_directory(HERE, "index.html")


@app.get("/api/slots")
def list_slots():
    return jsonify({
        "slots": load_meta(),
        "playing": player.now_playing(),
        "sensor": sensor_status,
    })


@app.post("/api/slots/<int:slot>")
def upload(slot):
    check_slot(slot)
    f = request.files.get("file")
    if not f or not f.filename:
        return jsonify(error="Choose an audio file to upload."), 400
    ext = os.path.splitext(f.filename)[1].lower()
    if ext not in ALLOWED_EXT:
        return jsonify(error=f"{ext or 'That file'} isn't supported. Use MP3, WAV, OGG, M4A, AAC or FLAC."), 400

    with meta_lock:
        meta = load_meta()
        old = meta.get(str(slot))
        if player.now_playing() == slot:
            player.stop()
        if old:
            try:
                os.remove(os.path.join(AUDIO_DIR, old["file"]))
            except FileNotFoundError:
                pass
        stored = f"slot{slot}{ext}"
        f.save(os.path.join(AUDIO_DIR, stored))
        meta[str(slot)] = {
            "file": stored,
            "name": secure_filename(f.filename) or stored,
            "label": request.form.get("label", "").strip()[:40],
            "size": os.path.getsize(os.path.join(AUDIO_DIR, stored)),
            "uploaded": int(time.time()),
        }
        save_meta(meta)
    return jsonify(slot=meta[str(slot)])


@app.patch("/api/slots/<int:slot>")
def relabel(slot):
    check_slot(slot)
    with meta_lock:
        meta = load_meta()
        if not meta.get(str(slot)):
            abort(404)
        meta[str(slot)]["label"] = (request.json or {}).get("label", "").strip()[:40]
        save_meta(meta)
    return jsonify(slot=meta[str(slot)])


@app.delete("/api/slots/<int:slot>")
def clear(slot):
    check_slot(slot)
    with meta_lock:
        meta = load_meta()
        old = meta.get(str(slot))
        if old:
            if player.now_playing() == slot:
                player.stop()
            try:
                os.remove(os.path.join(AUDIO_DIR, old["file"]))
            except FileNotFoundError:
                pass
            meta[str(slot)] = None
            save_meta(meta)
    return jsonify(ok=True)


@app.get("/api/slots/<int:slot>/audio")
def audio(slot):
    check_slot(slot)
    path = slot_path(slot)
    if not path or not os.path.exists(path):
        abort(404)
    return send_file(path, conditional=True)


@app.post("/api/slots/<int:slot>/play")
def play(slot):
    check_slot(slot)
    if not player.play(slot):
        return jsonify(error="Nothing to play. Upload a file to this slot first."), 400
    return jsonify(ok=True)


@app.post("/api/stop")
def stop():
    player.stop()
    return jsonify(ok=True)


@app.errorhandler(413)
def too_large(_):
    return jsonify(error="That file is over 25 MB. Trim it or export at a lower bitrate."), 413


if __name__ == "__main__":
    threading.Thread(target=touch_loop, daemon=True).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), threaded=True)
