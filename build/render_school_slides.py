# -*- coding: utf-8 -*-
import io
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = r"D:\AI\ZCode\universities"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
profile = tempfile.mkdtemp(prefix="edge_slide_")
ids = sys.argv[1:]
if not ids:
    for fn in ["schools_211.js", "schools_extra.js"]:
        t = io.open(os.path.join(ROOT, "data", fn), encoding="utf-8").read()
        d = json.loads(re.search(r"var extra = (\{[\s\S]*?\});", t).group(1))
        ids += list(d.keys())
for sid in ids:
    dst = os.path.join(ROOT, "assets", "covers", sid)
    os.makedirs(dst, exist_ok=True)
    for i in range(1, 5):
        out = os.path.join(dst, "0%d.png" % i)
        url = "file:///D:/AI/ZCode/universities/build/slides.html?id=%s&only=%d&v=4" % (sid, i)
        cmd = [
            EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
            "--virtual-time-budget=1800", "--user-data-dir=" + profile,
            "--force-device-scale-factor=1", "--window-size=1080,1920",
            "--screenshot=" + out, url,
        ]
        try:
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=30)
        except Exception as e:
            print("FAIL", sid, i, type(e).__name__)
    print("ok", sid)
