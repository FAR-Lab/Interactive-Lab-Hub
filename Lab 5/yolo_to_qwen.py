"""
Part E: the pipeline. YOLO watches for a while, an interpreter turns boxes into
readings in words, the readings become a log, and Qwen answers a question about it.
Headless, so it runs over plain ssh.

    python yolo_to_qwen.py                               # watch 60 s, then ask the default question
    python yolo_to_qwen.py --seconds 300                 # watch longer
    python yolo_to_qwen.py --question "Did anyone leave?"
    python yolo_to_qwen.py --every                       # log every reading, not only changes
    python yolo_to_qwen.py --json                        # ask for a structured answer
    python yolo_to_qwen.py --log watch_log.txt           # skip the camera, reason over a saved log

Each run saves its log to watch_log.txt. Edit that file by hand and feed it back
with --log to see whether the model notices contradictions.

overnight.py imports interpret() and model from this file, so keep them at the top level.
"""
import argparse
import datetime
import time

import cv2
import requests
from ultralytics import YOLO

model = YOLO("yolo26n_ncnn_model")


def interpret(r):
    """The interpreter: turn one YOLO result into one short reading in words.

    This is the most important design decision in the pipeline. The language model
    never sees pixels, only the words chosen here. Change it and the model's world changes.
    """
    h, w = r.orig_shape
    people, others = [], set()
    for box in r.boxes:
        name = model.names[int(box.cls)]
        if name != "person":
            others.add(name)
            continue
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        cx = (x1 + x2) / 2
        side = "left" if cx < w / 3 else "right" if cx > 2 * w / 3 else "center"
        dist = "close" if (y2 - y1) > 0.6 * h else "far"
        people.append(f"{side}/{dist}")
    reading = f"{len(people)} person(s) at {', '.join(people)}" if people else "nobody"
    if others:
        reading += "; also " + ", ".join(sorted(others))
    return reading


def watch(seconds, every=False, interval=0.5):
    """Watch the webcam for `seconds`. Returns the log as a list of 'HH:MM:SS reading' lines."""
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    log, last = [], None
    t_end = time.time() + seconds
    while time.time() < t_end:
        ok, frame = cap.read()
        if not ok:
            time.sleep(1)
            continue
        r = model.predict(frame, imgsz=320, conf=0.4, verbose=False)[0]
        reading = interpret(r)
        if every or reading != last:
            log.append(f"{datetime.datetime.now():%H:%M:%S} {reading}")
            print(log[-1], flush=True)
            last = reading
        time.sleep(interval)
    cap.release()
    return log


def ask(log, question, seconds, llm="qwen3.5:0.8b", every=False, as_json=False):
    """The reasoner: give the model the log and the question, nothing else."""
    how = "every half second" if every else "only when the reading changed"
    log_text = "\n".join(log)
    prompt = f"""You are the reasoning part of an observant device. A camera watched a room for {seconds} seconds.
Below is the detector's log. A line was written {how}.

{log_text}

Question: {question}
Answer in at most three sentences. Only use what is in the log. If the log does not say, say so."""
    request = {
        "model": llm,
        "prompt": prompt,
        "think": False,
        "stream": False,
        "options": {"temperature": 0.2},
    }
    if as_json:
        request["format"] = {
            "type": "object",
            "properties": {
                "people": {"type": "integer"},
                "activity": {"type": "string"},
                "unusual": {"type": "boolean"},
            },
            "required": ["people", "activity", "unusual"],
        }
    t0 = time.time()
    r = requests.post("http://localhost:11434/api/generate", json=request, timeout=600)
    r.raise_for_status()
    return r.json()["response"], time.time() - t0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=60, help="how long to watch")
    parser.add_argument("--question",
                        default="How many people were there, what were they doing, and did anything change?")
    parser.add_argument("--model", default="qwen3.5:0.8b")
    parser.add_argument("--every", action="store_true", help="log every reading, not only changes")
    parser.add_argument("--json", action="store_true", help="ask for a structured JSON answer")
    parser.add_argument("--log", help="reason over this saved log instead of watching")
    args = parser.parse_args()

    if args.log:
        log = [line.rstrip("\n") for line in open(args.log) if line.strip()]
    else:
        log = watch(args.seconds, every=args.every)
        with open("watch_log.txt", "w") as f:
            f.write("\n".join(log) + "\n")
        print(f"\n{len(log)} lines saved to watch_log.txt")

    answer, took = ask(log, args.question, args.seconds, llm=args.model,
                       every=args.every, as_json=args.json)
    print(f"\nQwen ({took:.1f} s):\n{answer}")
