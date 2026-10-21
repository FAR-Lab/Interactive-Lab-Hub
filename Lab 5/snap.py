"""
Take one photo with the webcam and save it. Part A runs YOLO on it, Part D shows it to Qwen.

    python snap.py                 # saves snap.jpg
    python snap.py desk.jpg        # choose the file name
    python snap.py --delay 3       # three seconds to get into the frame

No window, so it works over plain ssh. The photo is 640x480.
"""
import argparse
import time

import cv2

parser = argparse.ArgumentParser()
parser.add_argument("file", nargs="?", default="snap.jpg", help="where to save the photo")
parser.add_argument("--delay", type=float, default=0, help="seconds to wait before the shot")
args = parser.parse_args()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
if not cap.isOpened():
    raise SystemExit("no webcam found: is it plugged in?")
if args.delay:
    print(f"taking the photo in {args.delay:g} s", flush=True)

# Keep reading while we wait: the first frames are dark until the camera adjusts its exposure.
ok, frame = False, None
t_end = time.time() + max(args.delay, 0.5)
while time.time() < t_end:
    ok, frame = cap.read()
cap.release()
if not ok:
    raise SystemExit("could not read a frame from the webcam")
cv2.imwrite(args.file, frame)
print(f"saved {args.file}")
