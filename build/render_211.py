# -*- coding: utf-8 -*-
import os
import re
import io
import subprocess
import shutil
import tempfile
from PIL import Image

ROOT = r"D:\AI\ZCode\universities"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
data = io.open(os.path.join(ROOT, "data", "schools_211.js"), encoding="utf-8").read()
ids = re.findall(r'"id": "([a-z]+)"', data)
# only top-level ids are all unique school ids
print("render", len(ids), ids)
profile = os.path.join(ROOT, "build", ".edge-211")
if os.path.isdir(profile):
    shutil.rmtree(profile, ignore_errors=True)
os.makedirs(profile, exist_ok=True)

for sid in ids:
    out_png = os.path.join(ROOT, "build", sid + "_211_2x.png")
    url = "file:///D:/AI/ZCode/universities/build/slides.html?id=" + sid + "&v=211"
    cmd = [
        EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--no-first-run", "--virtual-time-budget=3000",
        "--user-data-dir=" + profile,
        "--force-device-scale-factor=2", "--window-size=1080,7680",
        "--screenshot=" + out_png, url,
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    if not os.path.exists(out_png):
        print("FAILED", sid)
        continue
    im = Image.open(out_png).convert("RGB")
    dst = os.path.join(ROOT, "assets", "covers", sid)
    os.makedirs(dst, exist_ok=True)
    for i in range(4):
        slide = im.crop((0, i * 3840, 2160, (i + 1) * 3840)).resize((1080, 1920), Image.LANCZOS)
        slide.save(os.path.join(dst, "0%d.png" % (i + 1)))
    print("ok", sid)
print("done")
