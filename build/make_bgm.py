import math
import os
import random
import struct
import wave

SR = 44100
BPM = 100.0
BEAT = 60.0 / BPM
BARS = 16  # 16 bars = 64 beats = 38.4s
DUR = BARS * 4 * BEAT
N = int(SR * DUR)
buf = [0.0] * N
random.seed(7)

# C major - G major - A minor - F major (4 bars each? no: one chord per bar, loop 4 bars)
CHORDS = [
    [261.63, 329.63, 392.00],  # C
    [196.00, 246.94, 293.66],  # G
    [220.00, 261.63, 329.63],  # Am
    [174.61, 220.00, 261.63],  # F
]
ROOTS = [130.81, 98.00, 110.00, 87.31]

def add(sample_index, value):
    if 0 <= sample_index < N:
        buf[sample_index] += value

def pluck(freq, start, dur, amp=0.18, decay=7.0):
    s0 = int(start * SR)
    n = int(dur * SR)
    for i in range(n):
        t = i / SR
        env = math.exp(-decay * t) * min(1.0, t / 0.008)
        v = math.sin(2 * math.pi * freq * t) + 0.28 * math.sin(4 * math.pi * freq * t) + 0.10 * math.sin(6 * math.pi * freq * t)
        add(s0 + i, amp * env * v)

def pad(freq, start, dur, amp=0.035):
    s0 = int(start * SR)
    n = int(dur * SR)
    attack = int(0.6 * SR)
    release = int(0.5 * SR)
    for i in range(n):
        t = i / SR
        env = 1.0
        if i < attack:
            env = i / attack
        elif i > n - release:
            env = max(0.0, (n - i) / release)
        v = math.sin(2 * math.pi * freq * t) + 0.15 * math.sin(2 * math.pi * freq * 1.005 * t)
        add(s0 + i, amp * env * v)

def bass(freq, start, dur, amp=0.10):
    s0 = int(start * SR)
    n = int(dur * SR)
    for i in range(n):
        t = i / SR
        env = math.exp(-1.6 * t) * min(1.0, t / 0.01)
        v = math.sin(2 * math.pi * freq * t) + 0.2 * math.sin(4 * math.pi * freq * t)
        add(s0 + i, amp * env * v)

def shaker(start, amp=0.012):
    s0 = int(start * SR)
    n = int(0.06 * SR)
    for i in range(n):
        t = i / SR
        env = math.exp(-70 * t)
        add(s0 + i, amp * env * random.uniform(-1, 1))

for bar in range(BARS):
    chord = CHORDS[bar % 4]
    root = ROOTS[bar % 4]
    bar_start = bar * 4 * BEAT
    # pad for the bar
    for f in chord:
        pad(f * 2, bar_start, 4 * BEAT, 0.022)
    # bass: beats 1 and 3
    bass(root, bar_start, 1.6 * BEAT, 0.11)
    bass(root, bar_start + 2 * BEAT, 1.6 * BEAT, 0.09)
    # arpeggio: 8 eighth notes
    pattern = [0, 1, 2, 1, 0, 2, 1, 2]
    for j in range(8):
        note = chord[pattern[j]] * 2
        start = bar_start + j * (BEAT / 2)
        pluck(note, start, 0.55, 0.14 if j % 2 == 0 else 0.11, 6.5)
    # offbeat shaker
    for j in range(4):
        shaker(bar_start + j * BEAT + BEAT / 2, 0.010)

peak = max(abs(x) for x in buf) or 1.0
gain = 0.82 / peak
out = bytearray()
for x in buf:
    v = int(max(-1.0, min(1.0, x * gain)) * 32767)
    out += struct.pack("<h", v)

path = r"D:\AI\ZCode\universities\assets\music\bgm.wav"
os.makedirs(os.path.dirname(path), exist_ok=True)
with wave.open(path, "wb") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(bytes(out))
print(path, os.path.getsize(path), "bytes", round(DUR, 1), "s")
