"""
Part B: find people in the webcam feed in real time with YOLO.

    python yolo_person.py                 # people only, with a window (needs VNC)
    python yolo_person.py --conf 0.2      # show what the model is unsure about
    python yolo_person.py --imgsz 640     # look at a bigger frame: more accurate, slower
    python yolo_person.py --all           # all 80 COCO classes, not just people
    python yolo_person.py --headless      # no window, so it works over plain ssh

Press q in the window to quit (Ctrl-C when headless).
"""
import argparse

import cv2
from ultralytics import YOLO

parser = argparse.ArgumentParser()
parser.add_argument("--conf", type=float, default=0.4, help="minimum confidence, 0 to 1")
parser.add_argument("--imgsz", type=int, default=320, help="frame size the model looks at")
parser.add_argument("--all", action="store_true", help="detect all 80 classes, not just people")
parser.add_argument("--headless", action="store_true", help="do not open a window")
args = parser.parse_args()

model = YOLO("yolo26n_ncnn_model")          # exported once in Part A
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
classes = None if args.all else [0]         # class 0 is "person" in COCO

try:
    while True:
        ok, frame = cap.read()
        if not ok:
            print("could not read from the camera")
            break
        r = model.predict(frame, imgsz=args.imgsz, conf=args.conf, classes=classes, verbose=False)[0]
        for box, cls, conf in zip(r.boxes.xyxy, r.boxes.cls, r.boxes.conf):
            x1, y1, x2, y2 = box.tolist()
            print(f"{model.names[int(cls)]} at x={int((x1 + x2) / 2)}, "
                  f"height={int(y2 - y1)} px, conf={conf:.2f}", end=" | ")
        print(f"{len(r.boxes)} object(s)", flush=True)
        if not args.headless:
            cv2.imshow("YOLO", r.plot())
            if cv2.waitKey(1) == ord("q"):
                break
except KeyboardInterrupt:
    pass
finally:
    cap.release()
    cv2.destroyAllWindows()
