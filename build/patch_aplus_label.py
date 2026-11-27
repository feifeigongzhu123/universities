# -*- coding: utf-8 -*-
import io
p = 'build/slides.html'
s = io.open(p, encoding='utf-8').read()
s = s.replace('>A+ 学科 / 强势专业<', ">'+(s.ap ? 'A+ 学科 / 强势专业' : '强势专业')+'<")
io.open(p, 'w', encoding='utf-8').write(s)
print('ok')
