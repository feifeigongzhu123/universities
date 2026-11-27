# -*- coding: utf-8 -*-
import os, subprocess, time, tempfile
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
OUT_DIR = os.path.join(ROOT, "assets", "majors", "cs")
os.makedirs(OUT_DIR, exist_ok=True)

prof = tempfile.mkdtemp(prefix="edge_major_")
png = os.path.join(tempfile.gettempdir(), "major_full.png")
if os.path.exists(png):
    os.remove(png)

url = "file:///" + os.path.join(ROOT, "build", "major_slides.html").replace("\\", "/") + "?v=16"
cmd = [
    EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars",
    "--force-device-scale-factor=2", "--window-size=1080,7680",
    "--user-data-dir=" + prof,
    "--screenshot=" + png,
    "--virtual-time-budget=8000",
    url,
]
subprocess.run(cmd, check=True, timeout=120)
time.sleep(0.3)

im = Image.open(png)
print("raw", im.size)
w, h = im.size
unit = h // 4
for i in range(4):
    part = im.crop((0, i * unit, w, (i + 1) * unit)).resize((1080, 1920), Image.LANCZOS)
    part.save(os.path.join(OUT_DIR, "0%d.png" % (i + 1)), optimize=True)
    print("saved", i + 1, part.size)
