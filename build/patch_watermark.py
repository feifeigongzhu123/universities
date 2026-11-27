# -*- coding: utf-8 -*-
import io
p = 'build/slides.html'
s = io.open(p, encoding='utf-8').read()
s = s.replace('content:"985";', 'content:attr(data-series);')
s = s.replace('<div class="out-bottom">', '<div class="out-bottom" data-series="\'+series+\'">')
io.open(p, 'w', encoding='utf-8').write(s)
print('out-bottom', s.count('data-series'))
