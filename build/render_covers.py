import os
import subprocess
from PIL import Image

ROOT = r"D:\AI\ZCode\universities"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
import sys
ids = sys.argv[1:] or ["tsinghua", "pku", "fudan", "sjtu", "zju", "ruc", "bnu", "buaa", "bit", "cau", "muc", "nankai", "tju", "dut", "neu", "jlu", "hit", "tongji", "ecnu", "nju", "seu", "ustc", "xmu", "sdu", "ouc", "whu", "hust", "csu", "hnu", "nudt", "sysu", "scut", "scu", "uestc", "cqu", "xjtu", "npu", "nwafu", "lzu"]

for sid in ids:
    out_png = os.path.join(ROOT, "build", sid + "_2x.png")
    url = "file:///D:/AI/ZCode/universities/build/slides.html?id=" + sid
    cmd = [
        EDGE,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--no-first-run",
        "--virtual-time-budget=3000",
        "--user-data-dir=" + os.path.join(ROOT, "build", ".edge-profile"),
        "--force-device-scale-factor=2",
        "--window-size=1080,7680",
        "--screenshot=" + out_png,
        url,
    ]
    print("render", sid)
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    if not os.path.exists(out_png):
        print("  FAILED: no screenshot")
        continue
    im = Image.open(out_png).convert("RGB")
    print("  deck", im.size)
    dst = os.path.join(ROOT, "assets", "covers", sid)
    os.makedirs(dst, exist_ok=True)
    for i in range(4):
        slide = im.crop((0, i * 3840, 2160, (i + 1) * 3840))
        slide = slide.resize((1080, 1920), Image.LANCZOS)
        path = os.path.join(dst, f"0{i+1}.png")
        slide.save(path)
        print("  ", path, os.path.getsize(path))
print("done")
