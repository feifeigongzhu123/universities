# -*- coding: utf-8 -*-
import io
p = 'build/slides.html'
s = io.open(p, encoding='utf-8').read()
s = s.replace('我的大学 · 985 系列', "我的大学 · '+series+' 系列")
s = s.replace('#985</span>', "#'+series+'</span>")
io.open(p, 'w', encoding='utf-8').write(s)
print('985系列', s.count('985 系列'), '#985', s.count('#985'))
