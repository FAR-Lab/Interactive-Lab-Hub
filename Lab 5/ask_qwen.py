"""
Part D: ask the on-device language model a question over the Ollama HTTP API.

    python ask_qwen.py "A camera saw one person in the kitchen at 3:12 am. Is that unusual?"
    python ask_qwen.py --model qwen3:0.6b "The same question, smaller model"
    python ask_qwen.py --image snap.jpg "What is on the desk?"      # qwen3.5 can look at a photo
    python ask_qwen.py --json "Is 3 am unusual for the kitchen?"    # answer as a JSON object
    python ask_qwen.py --think "Why?"                               # let it think first (slow)

Ollama must be running (it starts at boot after Part A). Nothing leaves the Pi.
"""
import argparse
import base64
import json
import time
import sys 

import requests

sys.stdout.reconfigure(encoding="utf-8") 
parser = argparse.ArgumentParser()
parser.add_argument("question")
parser.add_argument("--model", default="qwen3.5:0.8b")
parser.add_argument("--image", help="a JPEG to send along with the question")
parser.add_argument("--json", action="store_true", help="force a JSON answer with a fixed schema")
parser.add_argument("--think", action="store_true", help="let the model think before answering")
args = parser.parse_args()

request = {
    "model": args.model,
    "prompt": args.question,
    "think": args.think,        # Qwen3 thinks before answering unless told not to
    "stream": False,
    "keep_alive": "5m",         # how long the model stays in RAM after this request
}
if args.image:
    with open(args.image, "rb") as f:
        request["images"] = [base64.b64encode(f.read()).decode()]
if args.json:
    request["format"] = {
        "type": "object",
        "properties": {"headline": {"type": "string"}, "unusual": {"type": "boolean"}},
        "required": ["headline", "unusual"],
    }

t0 = time.time()
r = requests.post("http://localhost:11434/api/generate", json=request, timeout=600)
r.raise_for_status()
reply = r.json()
if reply.get("thinking"):
    print("[thinking]", reply["thinking"].strip(), "\n")
answer = reply["response"]
print(json.dumps(json.loads(answer), indent=2) if args.json else answer)
print(f"\n[{args.model}, {time.time() - t0:.1f} s]")
