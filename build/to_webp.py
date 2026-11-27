# -*- coding: utf-8 -*-
import glob
import os
from PIL import Image

root = r'D:\AI\ZCode\universities'
files = glob.glob(os.path.join(root, 'assets', 'covers', '*', '*.png')) + glob.glob(os.path.join(root, 'assets', 'majors', '*', '*.png'))
before = after = 0
for f in files:
    out = f[:-4] + '.webp'
    before += os.path.getsize(f)
    im = Image.open(f).convert('RGB')
    im.save(out, 'WEBP', quality=82, method=6)
    after += os.path.getsize(out)
print('files', len(files), 'png MB', round(before / 1048576, 1), 'webp MB', round(after / 1048576, 1))
