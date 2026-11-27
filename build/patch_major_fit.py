# -*- coding: utf-8 -*-
import io
p = 'build/render_majors.py'
s = io.open(p, encoding='utf-8').read()
s = s.replace("        '<div class=\"ability-foot\">能力账本（示意），不是对个人的评估。</div>'\n", "")
io.open(p, 'w', encoding='utf-8').write(s)
p2 = 'build/major_slides.html'
t = io.open(p2, encoding='utf-8').read()
t = t.replace('.career{background:var(--card);border:1px solid var(--line);padding:20px 22px;', '.career{background:var(--card);border:1px solid var(--line);padding:18px 22px;')
io.open(p2, 'w', encoding='utf-8').write(t)
print('ok')
