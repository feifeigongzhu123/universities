# -*- coding: utf-8 -*-
import io, re
s = io.open('data/schools_211.js', encoding='utf-8').read()
names = re.findall(r'"name": "([^"]+)"', s)
print(len(names), len(set(names)))
print('|'.join(sorted(set(names))))
s2 = io.open('data/schools_extra.js', encoding='utf-8').read()
names2 = re.findall(r'"name": "([^"]+)"', s2)
print('985', len(names2), len(set(names2)))
print('|'.join(sorted(set(names2))))
