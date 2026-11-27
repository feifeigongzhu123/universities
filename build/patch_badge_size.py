# -*- coding: utf-8 -*-
import io
p = 'build/render_majors.py'
s = io.open(p, encoding='utf-8').read()
s = s.replace(
    "'<div class=\"badge-row\"><div class=\"badge\">%s</div><div class=\"kicker\">UNDERGRADUATE MAJOR · NO.01</div></div>'",
    "'<div class=\"badge-row\"><div class=\"badge\" style=\"font-size:%dpx\">%s</div><div class=\"kicker\">UNDERGRADUATE MAJOR · NO.01</div></div>'"
)
s = s.replace(
    ') % (m["badge"], m["degree"], m["badge"], m["name"], m["en"], m["def"], m["sub"], tags, facts)',
    ') % (m["badge"], m["degree"], (54 if len(m["badge"]) <= 2 else (40 if len(m["badge"]) == 3 else 30)), m["badge"], m["name"], m["en"], m["def"], m["sub"], tags, facts)'
)
io.open(p, 'w', encoding='utf-8').write(s)
print('ok')
