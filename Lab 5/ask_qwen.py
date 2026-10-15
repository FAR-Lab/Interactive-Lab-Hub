"""
Part D: ask the on-device language model a question over the Ollama HTTP API.

    python ask_qwen.py "Tell me a bit about the history of Roosevelt Island."
    python ask_qwen.py --model qwen3:0.6b "The same question, smaller model"
    python ask_qwen.py --image snap.jpg "What is in this photo?"    # qwen3.5 can look at a photo (snap.py takes one)
    python ask_qwen.py --json "Someone was at the door at 3 am. Is that unusual?"   # answer as a JSON object
    python ask_qwen.py --max-tokens 400 "Why?"                      # allow a longer answer
    python ask_qwen.py --think "Why?"                               # let it think first (slow)

Two things keep the answer short, because a small model left to itself writes an essay:
a system prompt asks for at most three sentences, and num_predict (--max-tokens) cuts the
model off after that many tokens. Thinking is off unless you pass --think.

Ollama must be running (it starts at boot after Part A). Nothing leaves the Pi.
"""
import argparse
import base64
import json
import sys
import time

import requests

sys.stdout.reconfigure(encoding="utf-8")
parser = argparse.ArgumentParser()
parser.add_argument("question")
parser.add_argument("--model", default="qwen3.5:0.8b")
parser.add_argument("--image", help="a JPEG to send along with the question")
parser.add_argument("--json", action="store_true", help="force a JSON answer with a fixed schema")
parser.add_argument("--max-tokens", type=int, default=120, help="hard cap on the length of the answer")
parser.add_argument("--think", action="store_true", help="let the model think before answering (slow)")
args = parser.parse_args()

request = {
    "model": args.model,
    "system": "You are a small bedside device. Answer in at most three short sentences.",
    "prompt": args.question,
    "think": args.think,        # False unless --think: Qwen3 reasons at length before answering if you let it
    "stream": False,
    "keep_alive": "5m",         # how long the model stays in RAM after this request
    "options": {"temperature": 0.3},
}
if not args.think:              # the cap would eat the thinking trace, so only cap plain answers
    request["options"]["num_predict"] = args.max_tokens
if args.image:
    with open(args.image, "rb") as f:
        request["images"] = [base64.b64encode(f.read()).decode()]
if args.json:
    request["system"] = "You are a small bedside device. Fill in the fields; keep the headline under fifteen words."
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
answer = reply["response"].strip()
if args.json:
    try:
        answer = json.dumps(json.loads(answer), indent=2)
    except json.JSONDecodeError:
        pass                    # cut off mid-object: print it as it came
print(answer)
note = ", cut off by --max-tokens" if reply.get("done_reason") == "length" else ""
print(f"\n[{args.model}, {time.time() - t0:.1f} s{note}]")
