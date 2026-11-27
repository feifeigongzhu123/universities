# -*- coding: utf-8 -*-
import io
for p in ['school.html', 'major.html']:
    s = io.open(p, encoding='utf-8').read()
    s = s.replace("'.png'", "'.webp'")
    io.open(p, 'w', encoding='utf-8').write(s)
print('ok')
