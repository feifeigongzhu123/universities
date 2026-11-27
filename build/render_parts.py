import os
import subprocess
import sys
from PIL import Image

ROOT = r"D:\AI\ZCode\universities"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
slide = sys.argv[1]
ids = sys.argv[2:]
profile = os.path.join(ROOT, "build", ".edge-parts2")
for sid in ids:
    shot = os.path.join(ROOT, "build", "%s_p%s.png" % (sid, slide))
    url = "file:///D:/AI/ZCode/universities/build/slides.html?id=%s&only=%s&v=12" % (sid, slide)
    cmd = [
        EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
        "--virtual-time-budget=3000", "--user-data-dir=" + profile,
        "--force-device-scale-factor=2", "--window-size=1080,1920",
        "--screenshot=" + shot, url,
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
    if not os.path.exists(shot):
        print("FAIL", sid)
        continue
    im = Image.open(shot).convert("RGB").resize((1080, 1920), Image.LANCZOS)
    dst = os.path.join(ROOT, "assets", "covers", sid, "0%s.png" % slide)
    im.save(dst)
    print("ok", sid, os.path.getsize(dst))
print("done")
