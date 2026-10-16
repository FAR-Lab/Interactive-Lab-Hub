# Soundboard

Upload up to six audio clips from a browser. Touch MPR121 pads E0–E5 and the Pi plays slots 01–06.

The web app runs on the Pi, so uploaded files go straight to `audio/` and nothing has to be fetched.

## Run it on the Pi

```bash
cd ~/Interactive-Lab-Hub/Lab\ 4/soundboard
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
sudo apt install -y ffmpeg      # provides ffplay for playback, if it isn't already installed
python app.py
```

Then open `http://<pi-ip>:5000` from any device on the same network.

## Wiring

MPR121 → Qwiic cable → Pi (through the Qwiic SHIM). Run copper tape or alligator clips from electrodes 0–5 to whatever you want people to touch.

## Sound output

The Pi 5 has no headphone jack. Pair the Bluetooth speaker from the kit, or use HDMI or USB audio:

```bash
bluetoothctl
  scan on          # wait for the speaker to appear
  pair <MAC>
  trust <MAC>
  connect <MAC>
```

## Notes

- Touching a pad stops whatever is playing and starts that slot.
- Uploading a new file to a slot replaces the old one.
- **Play on Pi** in the browser tests playback without touching the sensor.
- If the sensor isn't detected, the page shows "no touch sensor" and uploads still work.
