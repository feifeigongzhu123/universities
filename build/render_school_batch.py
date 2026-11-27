# -*- coding: utf-8 -*-
import io
import json
import os
import re
import subprocess
import sys
import tempfile
from PIL import Image

ROOT = r"D:\AI\ZCode\universities"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
profile = tempfile.mkdtemp(prefix="edge_s_")
ids = sys.argv[1:]
if not ids:
    ids = []
    for fn in ["schools_211.js", "schools_extra.js"]:
        t = io.open(os.path.join(ROOT, "data", fn), encoding="utf-8").read()
        d = json.loads(re.search(r"var extra = (\{[\s\S]*?\});", t).group(1))
        ids += list(d.keys())
for sid in ids:
    png = os.path.join(ROOT, "build", "school_" + sid + ".png")
    url = "file:///D:/AI/ZCode/universities/build/slides.html?id=" + sid + "&v=3"
    cmd = [
        EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
        "--virtual-time-budget=2500", "--user-data-dir=" + profile,
        "--force-device-scale-factor=1", "--window-size=1080,7680",
        "--screenshot=" + png, url,
    ]
    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=45)
    except Exception as e:
        print("FAIL", sid, type(e).__name__)
        continue
    if not os.path.exists(png):
        print("FAILED", sid)
        continue
    im = Image.open(png).convert("RGB")
    dst = os.path.join(ROOT, "assets", "covers", sid)
    os.makedirs(dst, exist_ok=True)
    for i in range(4):
        im.crop((0, i * 1920, 1080, (i + 1) * 1920)).save(os.path.join(dst, "0%d.png" % (i + 1)))
    print("ok", sid)
