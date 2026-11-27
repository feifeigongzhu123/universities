# -*- coding: utf-8 -*-
import io
p = 'build/make_extra.py'
s = io.open(p, encoding='utf-8').read()
s = s.replace('from data_985_stats import BAOYAN, APLUS', 'from data_985_stats import BAOYAN, APLUS\nimport sys\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\nfrom school_content import P985, major_text')
s = s.replace('''    hook = "在%s，读一所%s强校。" % (city_text, typ)
    ap_mini = {"n": str(ap) + "个", "l": "A+ 学科"} if ap else {"n": "6个", "l": "王牌专业"}
    sub = "%s，985 高校。" % name''', '''    prof = P985.get(sid)
    hook = prof[0] if prof else "在%s，读一所%s强校。" % (city_text, typ)
    ap_mini = {"n": str(ap) + "个", "l": "A+ 学科"} if ap else {"n": "6个", "l": "王牌专业"}
    sub = prof[1] if prof else "%s，985 高校。" % name''')
s = s.replace('''    for m in major_list:
        major_objs.append({
            "name": m,
            "sub": "本科王牌专业",
            "learn": "核心课程、实验与实践",
            "go": "对口行业、科研院所、继续深造",
            "feature": "国家级或校级特色方向",
            "tags": ["王牌", "本科"]
        })''', '''    for m in major_list:
        learn, go, feature = major_text(m)
        major_objs.append({
            "name": m,
            "sub": "代表专业",
            "learn": learn,
            "go": go,
            "feature": feature,
            "tags": ["代表", "本科"]
        })''')
old_audio = '''    audio = [
        "欢迎来到%s。它位于%s，是一所%s特色的985高校。接下来，带你认识%s。" % (name, city_text, typ, nick),
        "先看专业。%s的王牌专业包括%s。" % (name, "、".join(major_list)),
        "%s 2026届保研率约%s%%；%s；毕业生主要去%s。" % (
            name, by,
            ("A+学科%s个，包括%s" % (ap, "、".join(ap_names))) if ap_names else "暂无A+学科，但6个王牌专业值得看",
            "、".join(industries(major_list))
        ),
        "最后看看校园。%s这座城市，加上%s的校园，值得你亲自走一趟。大学之道，在明明德。下一站，%s。" % (city_text, name, nick)
    ]'''
new_audio = '''    guide = prof[2] if prof else ["校园通常很大，自行车是刚需。", "图书馆和自习室，开学先踩点。", "食堂和周边，先逛一圈再办卡。"]
    quote = prof[3] if prof else "大学之道，在明明德。"
    audio = [
        "%s。%s" % (name, sub),
        "先看专业。%s的 6 个代表专业是%s。比如%s，主要学%s，毕业去%s。" % (
            name, "、".join(major_list), major_list[0], major_text(major_list[0])[0], major_text(major_list[0])[1]),
        "%s 2026届保研率约%s%%；%s；毕业生主要去%s。" % (
            name, by,
            ("A+学科%s个，包括%s" % (ap, "、".join(ap_names))) if ap_names else "6个代表专业值得看",
            "、".join(industries(major_list))
        ),
        "最后看看校园。%s%s 校训是“%s”。下一站，%s。" % (guide[0], guide[2], quote, nick)
    ]'''
if old_audio not in s:
    print('AUDIO MISS')
s = s.replace(old_audio, new_audio)
s = s.replace('''            "guide": [
                "校园通常很大，自行车是刚需。",
                "图书馆和自习室，开学先踩点。",
                "食堂和周边，先逛一圈再办卡。"
            ],
            "alumni": "从这里出发的人，正在各个行业里做事。",
            "quote": "大学之道，在明明德。",
            "quoteBy": "《大学》"''', '''            "guide": guide,
            "alumni": "毕业生主要流向：" + "、".join(industries(major_list)) + "。",
            "quote": quote,
            "quoteBy": prof[4] if prof else "《大学》"''')
io.open(p, 'w', encoding='utf-8').write(s)
print('ok')
