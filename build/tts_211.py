# -*- coding: utf-8 -*-
import asyncio
import io
import json
import os
import re

import edge_tts

ROOT = r"D:\AI\ZCode\universities"
DATA_FILE = os.path.join(ROOT, "data", "schools_211.js")
VOICE = "zh-CN-XiaoxiaoNeural"
RATE = "+4%"
PITCH = "+2Hz"

text = io.open(DATA_FILE, encoding="utf-8").read()
pattern = re.compile(r'"?id"?\s*:\s*"([a-z]+)"[\s\S]*?"?audioScript"?\s*:\s*(\[[\s\S]*?\])\s*,?\s*\n\s*\}', re.M)
matches = list(dict(pattern.findall(text)).items())
print("schools found:", len(matches))

jobs = []
for sid, raw in matches:
    try:
        scripts = json.loads(raw)
    except Exception as exc:
        print("JSON ERR", sid, exc)
        continue
    os.makedirs(os.path.join(ROOT, "audio", sid), exist_ok=True)
    for i, script in enumerate(scripts, start=1):
        jobs.append((sid, i, script))

async def one(sid, i, script, sem):
    out = os.path.join(ROOT, "audio", sid, "0%d.mp3" % i)
    if os.path.exists(out) and os.path.getsize(out) > 2000:
        print("skip", sid, i)
        return
    async with sem:
        for attempt in range(3):
            try:
                comm = edge_tts.Communicate(script, VOICE, rate=RATE, pitch=PITCH)
                await comm.save(out)
                print("ok", sid, i, os.path.getsize(out))
                return
            except Exception as exc:
                print("retry", sid, i, attempt + 1, type(exc).__name__, exc)
                await asyncio.sleep(1.5)
        print("FAIL", sid, i)

async def main():
    sem = asyncio.Semaphore(3)
    await asyncio.gather(*(one(sid, i, script, sem) for sid, i, script in jobs))

asyncio.run(main())
print("done", len(jobs))
