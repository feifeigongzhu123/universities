# -*- coding: utf-8 -*-
import io
p = 'build/major_slides.html'
s = io.open(p, encoding='utf-8').read()
repl = [
('.linecard{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--purple);padding:22px 20px;}', '.linecard{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--purple);padding:26px 22px;}'),
('.courses{margin-top:22px;background:var(--card);border:1px solid var(--line);padding:24px 26px;}', '.courses{margin-top:22px;background:var(--card);border:1px solid var(--line);padding:28px 26px;}'),
('.note{margin-top:18px;background:var(--lilac-pale);border-left:5px solid var(--purple);padding:16px 22px;font-size:18px;line-height:1.8;color:var(--soft);}', '.note{margin-top:18px;background:var(--lilac-pale);border-left:5px solid var(--purple);padding:18px 22px;font-size:19px;line-height:1.8;color:var(--soft);}'),
('.order div{background:var(--card);border:1px solid var(--line);border-top:3px solid var(--gold);padding:16px 18px;}', '.order div{background:var(--card);border:1px solid var(--line);border-top:3px solid var(--gold);padding:18px 20px;}'),
('.myths div{background:var(--card);border:1px solid var(--line);padding:14px 16px;}', '.myths div{background:var(--card);border:1px solid var(--line);padding:17px 18px;}'),
('.myths span{font-size:13px;line-height:1.65;color:var(--soft);}', '.myths span{font-size:14px;line-height:1.65;color:var(--soft);}'),
('.prep{margin-top:16px;background:var(--card);border:1px solid var(--line);padding:16px 20px;display:grid;grid-template-columns:150px 1fr;gap:16px;}', '.prep{margin-top:16px;background:var(--card);border:1px solid var(--line);padding:20px 22px;display:grid;grid-template-columns:150px 1fr;gap:16px;}'),
('.year{background:var(--card);border:1px solid var(--line);border-top:3px solid var(--purple);padding:20px 22px;}', '.year{background:var(--card);border:1px solid var(--line);border-top:3px solid var(--purple);padding:24px 24px;}'),
('.fitcard{border:1px solid var(--line);padding:18px 20px;background:var(--card);}', '.fitcard{border:1px solid var(--line);padding:22px 22px;background:var(--card);}'),
('.works div{background:var(--card);border:1px solid var(--line);padding:16px 18px;font-size:14px;line-height:1.7;color:var(--soft);}', '.works div{background:var(--card);border:1px solid var(--line);padding:20px 20px;font-size:14px;line-height:1.7;color:var(--soft);}'),
('.advice{margin-top:18px;background:var(--lilac-pale);border-left:5px solid var(--purple);padding:16px 20px;font-size:15px;line-height:1.8;color:var(--soft);}', '.advice{margin-top:18px;background:var(--lilac-pale);border-left:5px solid var(--purple);padding:20px 22px;font-size:15px;line-height:1.8;color:var(--soft);}'),
('.holiday div{background:var(--card);border-left:4px solid var(--gold);padding:14px 16px;font-size:13px;line-height:1.65;color:var(--soft);}', '.holiday div{background:var(--card);border-left:4px solid var(--gold);padding:18px 18px;font-size:13px;line-height:1.65;color:var(--soft);}'),
('.portfolio div{background:var(--card);border:1px solid var(--line);padding:14px 16px;font-size:13px;line-height:1.65;color:var(--soft);}', '.portfolio div{background:var(--card);border:1px solid var(--line);padding:18px 18px;font-size:13px;line-height:1.65;color:var(--soft);}'),
('.career{background:var(--card);border:1px solid var(--line);padding:20px 22px;position:relative;overflow:hidden;}', '.career{background:var(--card);border:1px solid var(--line);padding:24px 24px;position:relative;overflow:hidden;}'),
('.day div{background:var(--card);border:1px solid var(--line);border-top:3px solid var(--purple);padding:14px 16px;font-size:13px;line-height:1.65;color:var(--soft);}', '.day div{background:var(--card);border:1px solid var(--line);border-top:3px solid var(--purple);padding:18px 18px;font-size:13px;line-height:1.65;color:var(--soft);}'),
('.path div{background:var(--card);border-left:4px solid var(--gold);padding:14px 16px;font-size:13px;line-height:1.65;color:var(--soft);}', '.path div{background:var(--card);border-left:4px solid var(--gold);padding:18px 18px;font-size:13px;line-height:1.65;color:var(--soft);}'),
('.seclabel{font-family:var(--serif);font-size:26px;font-weight:400;color:var(--deep);margin:24px 0 10px;display:flex;align-items:center;gap:10px;}', '.seclabel{font-family:var(--serif);font-size:26px;font-weight:400;color:var(--deep);margin:30px 0 12px;display:flex;align-items:center;gap:10px;}'),
('min-height:190px;', 'min-height:240px;'),
('.closing{margin-top:auto;margin-bottom:58px;background:linear-gradient(150deg,#3B0846,#220529);color:#FFF7EA;padding:28px 30px;display:flex;justify-content:space-between;align-items:center;gap:18px;}', '.closing{margin-top:auto;margin-bottom:58px;background:linear-gradient(150deg,#3B0846,#220529);color:#FFF7EA;padding:28px 30px;min-height:260px;display:flex;justify-content:space-between;align-items:center;gap:18px;}'),
('.industries span{font-size:13px;color:var(--purple);background:var(--lilac-pale);border:1px solid rgba(91,12,102,.14);padding:5px 9px;}', '.industries span{font-size:13px;color:var(--purple);background:var(--lilac-pale);border:1px solid rgba(91,12,102,.14);padding:5px 9px;}\n  .donts{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;}\n  .donts div{background:var(--card);border-left:4px solid var(--red);padding:14px 18px;font-size:13px;line-height:1.7;color:var(--soft);}\n  .donts b{color:var(--red);}'),
]
for a, b in repl:
    if a not in s:
        print('MISS', a[:80])
    s = s.replace(a, b)
io.open(p, 'w', encoding='utf-8').write(s)
print('done')
