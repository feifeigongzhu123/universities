import asyncio
import io
import json
import os
import re

import edge_tts

ROOT = r"D:\AI\ZCode\universities"
DATA_FILES = [os.path.join(ROOT, "data", "schools.js"), os.path.join(ROOT, "data", "schools_extra.js"), os.path.join(ROOT, "data", "dut_rich.js")]
VOICE = "zh-CN-XiaoxiaoNeural"
RATE = "+4%"
PITCH = "+2Hz"

text = "\n".join(io.open(f, encoding="utf-8").read() for f in DATA_FILES)
pattern = re.compile(r'"?id"?\s*:\s*"([a-z]+)"[\s\S]*?"?audioScript"?\s*:\s*(\[[\s\S]*?\])\s*,?\s*\n\s*\}', re.M)
matches = pattern.findall(text)
seen = {}
for sid, raw in matches:
    seen[sid] = raw
matches = list(seen.items())
print("schools found:", [m[0] for m in matches])

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
    out = os.path.join(ROOT, "audio", sid, f"0{i}.mp3")
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
