# -*- coding: utf-8 -*-
"""Synthesize a calm ambient pad loop (royalty-free, generated) for BGM.

Cmaj7 -> Am7 -> Fmaj7 -> G6 progression, 8s per chord, 64s total.
Soft sine pads with slow attack/release + gentle bass. 44.1kHz stereo WAV.
"""
import math, struct, wave, os

SR = 44100
CHORD_SEC = 8.0
NOTE = {  # frequencies, octave 3-4 (Hz)
    "C3": 130.81, "E3": 164.81, "F3": 174.61, "G3": 196.00, "A3": 220.00,
    "B3": 246.94, "C4": 261.63, "D4": 293.66, "E4": 329.63, "F4": 349.23,
    "G4": 392.00, "A4": 440.00, "B4": 493.88,
}
CHORDS = [
    (["C4", "E4", "G4", "B4"], "C3"),   # Cmaj7
    (["A3", "C4", "E4", "G4"], "A3"),   # Am7
    (["F3", "A3", "C4", "E4"], "F3"),   # Fmaj7
    (["G3", "B3", "D4", "E4"], "G3"),   # G6
]

n_chord = int(CHORD_SEC * SR)
samples = []

for voices, bass in CHORDS:
    freqs = [NOTE[v] for v in voices]
    bass_f = NOTE[bass] / 2.0  # one octave down
    for i in range(n_chord):
        t = i / SR
        # slow attack (1.5s) and release (1.5s) envelope per chord
        env = min(1.0, t / 1.5) * min(1.0, (CHORD_SEC - t) / 1.5)
        # gentle amplitude LFO for breathing feel
        lfo = 1.0 + 0.08 * math.sin(2 * math.pi * 0.15 * t)
        s = 0.0
        for k, f in enumerate(freqs):
            # slight detune per voice for warmth; 1st+2nd harmonic only (soft)
            det = 1.0 + 0.0006 * (k - 1.5)
            s += 0.22 * math.sin(2 * math.pi * f * det * t)
            s += 0.05 * math.sin(2 * math.pi * f * det * 2 * t)
        s += 0.28 * math.sin(2 * math.pi * bass_f * t)
        samples.append(s * env * lfo * 0.55)

# stereo widening: right channel delayed ~11ms
delay = int(0.011 * SR)
n = len(samples)
frames = bytearray()
for i in range(n):
    l = samples[i]
    r = samples[i - delay] if i >= delay else 0.0
    frames += struct.pack("<hh", int(max(-1, min(1, l)) * 32767 * 0.9),
                          int(max(-1, min(1, r)) * 32767 * 0.9))

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bgm_pad.wav")
with wave.open(out, "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(bytes(frames))
print(out, round(n / SR, 2), "sec")
