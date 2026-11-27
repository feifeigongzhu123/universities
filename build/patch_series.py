# -*- coding: utf-8 -*-
import io
p = 'build/slides.html'
s = io.open(p, encoding='utf-8').read()
s = s.replace("var s = window.SCHOOLS[id];", "var s = window.SCHOOLS[id];\n  var series = s.series || '985';")
s = s.replace("'我的大学 · 985 系列'", "'我的大学 · '+series+' 系列'")
s = s.replace(
    "'<div class=\"cover-right\"><b>985</b><span>首批 · 2026</span></div></div>'",
    "'<div class=\"cover-right\"><b>'+series+'</b><span>'+(series==='211'?'工程 · 2026':'首批 · 2026')+'</span></div></div>'"
)
s = s.replace("'#'+s.short+' #985'", "'#'+s.short+' #'+series")
io.open(p, 'w', encoding='utf-8').write(s)
print('patched', s.count("985 系列"), s.count("#985"))
