#!/usr/bin/env python3
"""Point to one of four words on the semicircle board.

Press Enter to choose a random word. The voice trigger can replace Enter later.
"""

import random
import re
import sys
import threading
import time
from pathlib import Path

import numpy as np
import pi_servo_hat
import sherpa_onnx
import sounddevice as sd
from faster_whisper import WhisperModel
from piper import PiperVoice

SERVO_CHANNEL = 0
SAFE_MIN = 10
SAFE_MAX = 110
MOVE_STEP = 2
MOVE_DELAY = 0.02
WANDER_COUNT = 5
SAMPLE_RATE = 16000
TRIGGER_ALIASES = ("go", "boring", "drink", "eat", "hungry", "food")
MIN_SILENCE = 0.15
MIN_SPEECH = 0.10
ECHO_GUARD = 1.0
SPEAKER_GAIN = 1.2
MIC_LOG_INTERVAL = 1.0

LAB4_DIR = Path(__file__).resolve().parent
LAB3_DIR = LAB4_DIR.parent / "Lab 3"
VAD_MODEL = LAB3_DIR / "models" / "silero_vad.onnx"
VOICE_MODEL = LAB3_DIR / "voices" / "en_US-lessac-medium.onnx"

# Calibrate these four angles against the physical labels on the board.
WORDS = (
    ("Eat More", 110),
    ("Really?", 77),
    ("Too Much!", 43),
    ("Cheers!", 10),
)


def move_smoothly(servo, start: int, target: int) -> None:
    step = MOVE_STEP if target >= start else -MOVE_STEP
    for angle in range(start, target, step):
        servo.move_servo_position(SERVO_CHANNEL, angle)
        time.sleep(MOVE_DELAY)
    servo.move_servo_position(SERVO_CHANNEL, target)


def wander_then_stop(servo, start: int, target: int) -> None:
    current = start
    for _ in range(WANDER_COUNT):
        wander_target = random.randint(SAFE_MIN, SAFE_MAX)
        move_smoothly(servo, current, wander_target)
        current = wander_target
    move_smoothly(servo, current, target)


def build_vad():
    config = sherpa_onnx.VadModelConfig()
    config.silero_vad.model = str(VAD_MODEL)
    config.silero_vad.min_silence_duration = MIN_SILENCE
    config.silero_vad.min_speech_duration = MIN_SPEECH
    config.sample_rate = SAMPLE_RATE
    return (sherpa_onnx.VoiceActivityDetector(config, buffer_size_in_seconds=30),
            config.silero_vad.window_size)


def speak(text: str, voice: PiperVoice) -> None:
    for chunk in voice.synthesize(text):
        samples = np.frombuffer(chunk.audio_int16_bytes, dtype=np.int16)
        louder = np.clip(samples.astype(np.float32) * SPEAKER_GAIN,
                          -32768, 32767).astype(np.int16)
        sd.play(louder, samplerate=chunk.sample_rate)
        sd.wait()


def heard_trigger(text: str) -> bool:
    normalized = re.sub(r"[^a-z']+", " ", text.lower()).strip()
    padded = f" {normalized} "
    return any(f" {alias} " in padded for alias in TRIGGER_ALIASES)


def start_keyboard_listener(trigger_event: threading.Event) -> None:
    def read_keyboard() -> None:
        for _ in sys.stdin:
            trigger_event.set()
            print("keyboard trigger accepted")

    threading.Thread(target=read_keyboard, daemon=True).start()


def listen_for_trigger(recognizer, vad, window,
                       keyboard_event: threading.Event) -> None:
    """Wait for Enter or recognize one of the configured voice triggers."""
    buffer = np.empty(0, dtype=np.float32)
    samples_per_read = int(0.1 * SAMPLE_RATE)

    print(f"Listening for voice: {', '.join(TRIGGER_ALIASES)} | press Enter")
    with sd.InputStream(channels=1, dtype="float32", samplerate=SAMPLE_RATE) as stream:
        last_mic_log = 0.0
        while True:
            chunk, _ = stream.read(samples_per_read)
            if keyboard_event.is_set():
                keyboard_event.clear()
                return
            now = time.monotonic()
            if now - last_mic_log >= MIC_LOG_INTERVAL:
                level = float(np.abs(chunk).mean())
                peak = float(np.abs(chunk).max())
                print(f"[mic] level={level:.4f} peak={peak:.4f}")
                last_mic_log = now
            buffer = np.concatenate([buffer, chunk.reshape(-1)])

            while len(buffer) > window:
                vad.accept_waveform(buffer[:window])
                buffer = buffer[window:]

            while not vad.empty():
                utterance = np.array(vad.front.samples, dtype=np.float32)
                vad.pop()
                print(f"speech detected ({len(utterance) / SAMPLE_RATE:.2f}s)")
                segments, _ = recognizer.transcribe(
                    utterance,
                    beam_size=1,
                    language="en",
                    condition_on_previous_text=False,
                    without_timestamps=True,
                )
                heard = " ".join(s.text.strip() for s in segments).lower()
                print(f'heard: "{heard}"')
                if heard_trigger(heard):
                    print("voice trigger accepted")
                    return
                print("voice trigger not detected")

                buffer = np.empty(0, dtype=np.float32)
                if hasattr(vad, "reset"):
                    vad.reset()


def main() -> None:
    if not VAD_MODEL.is_file():
        sys.exit(f"VAD model not found: {VAD_MODEL}")
    if not VOICE_MODEL.is_file():
        sys.exit(f"Piper voice not found: {VOICE_MODEL}")

    print("Loading speech model...")
    recognizer = WhisperModel("tiny.en", device="cpu", compute_type="int8")
    vad, window = build_vad()
    voice = PiperVoice.load(str(VOICE_MODEL))
    keyboard_event = threading.Event()
    start_keyboard_listener(keyboard_event)
    servo = pi_servo_hat.PiServoHat()
    servo.restart()
    current_angle = (SAFE_MIN + SAFE_MAX) // 2
    servo.move_servo_position(SERVO_CHANNEL, current_angle)

    try:
        while True:
            listen_for_trigger(recognizer, vad, window, keyboard_event)
            word, target_angle = random.choice(WORDS)
            print(f"{word} -> {target_angle} degrees")
            wander_then_stop(servo, current_angle, target_angle)
            current_angle = target_angle
            speak(word, voice)
            time.sleep(ECHO_GUARD)
    except KeyboardInterrupt:
        print("\nStopping at the center position.")
        move_smoothly(servo, current_angle, (SAFE_MIN + SAFE_MAX) // 2)


if __name__ == "__main__":
    main()
