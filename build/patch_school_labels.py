# -*- coding: utf-8 -*-
import io
p = 'build/slides.html'
s = io.open(p, encoding='utf-8').read()
s = s.replace("var sub = '6 个方向：学什么、有什么特色、毕业去哪儿。';", "var sub = s.name + ' 的 6 个代表专业：学什么、有什么特色、毕业去哪儿。';")
s = s.replace("? '这里列的是 6 个王牌专业。<br>'+s.name+'还有更多方向，等你去看。'", "? '这里列的是 '+s.name+' 的 6 个代表专业。<br>更多方向在本科招生网。'")
s = s.replace(": (s.rich ? '这里列的是 6 个王牌专业。<br>'+s.name+'有 7 个 A 类学科。'", ": (s.rich ? '这里列的是 6 个代表专业。<br>'+s.name+'有 7 个 A 类学科。'")
s = s.replace("<h2 class=\"m-title\">王牌专业地图</h2>", "<h2 class=\"m-title\">专业地图</h2>")
s = s.replace("<div class=\"m-note\"><b>选专业提醒：</b>名字好听 ≠ 适合你。先看培养方案里的必修课，再看近三届毕业生的去向。</div>", "<div class=\"m-note\"><b>看专业：</b>'+s.name+' 的强项、课程和毕业去向，要放在一起看。</div>")
s = s.replace("<div class=\"out-majorlabel\">6 个王牌专业</div>", "<div class=\"out-majorlabel\">'+s.name+' 的 6 个代表专业</div>")
s = s.replace("<div class=\"out-bhead\"><h2>就业与专业</h2><span>6 个王牌专业</span></div>", "<div class=\"out-bhead\"><h2>就业与专业</h2><span>6 个代表专业</span></div>")
s = s.replace("<span>左滑看王牌专业 →</span>", "<span>左滑看专业 →</span>")
io.open(p, 'w', encoding='utf-8').write(s)
print('ok')
