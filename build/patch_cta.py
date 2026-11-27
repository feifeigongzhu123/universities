# -*- coding: utf-8 -*-
import io
p = 'build/slides.html'
s = io.open(p, encoding='utf-8').read()
s = s.replace('<div class="cover-kicker">一所大学，四个侧面</div>', '<div class="cover-kicker">\'+s.type+\' · \'+s.city+\'</div>')
line = "+'<div class=\"camp-cta\"><p>把这张图转给正在填志愿的人。<br><b>评论区点名下一位。</b></p><div class=\"next\">'+s.en+'<br>SAVE · SHARE · ASK</div></div>'"
if line not in s:
    print('CTA MISS')
s = s.replace(line, '')
io.open(p, 'w', encoding='utf-8').write(s)
print('ok')
