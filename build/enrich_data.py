# -*- coding: utf-8 -*-
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'build'))
from school_content import P211, P985, major_text


def load(path):
    s = io.open(path, encoding='utf-8').read()
    m = re.search(r'var extra = (\{[\s\S]*?\});\s*\n\s*Object\.assign', s)
    if not m:
        raise SystemExit('cannot parse ' + path)
    data = json.loads(m.group(1))
    order = re.search(r'window\.SCHOOL_ORDER(?:_211)? = (\[[\s\S]*?\]);', s)
    return data, json.loads(order.group(1)) if order else list(data.keys())


def enrich(data, profiles, series):
    for sid, s in data.items():
        prof = profiles.get(sid)
        if prof:
            s['hook'], s['sub'] = prof[0], prof[1]
            s['campus']['guide'] = prof[2]
            s['campus']['quote'] = prof[3]
            s['campus']['quoteBy'] = prof[4]
        for m in s.get('majors', []):
            learn, go, feature = major_text(m['name'])
            m['sub'] = '代表专业'
            m['learn'], m['go'], m['feature'] = learn, go, feature
            m['tags'] = ['代表', '本科']
        inds = s.get('outcome', {}).get('industries', [])
        if inds:
            s['campus']['alumni'] = '毕业生主要流向：' + '、'.join(inds) + '。'
        # labels
        for st in s.get('stats', []):
            if st.get('l') == '王牌专业':
                st['l'] = '代表专业'
        for f in s.get('campus', {}).get('facts', []):
            if f.get('l') == '王牌专业':
                f['l'] = '代表专业'
        for mini in s.get('outcome', {}).get('minis', []):
            if mini.get('l') == '王牌专业':
                mini['l'] = '代表专业'
        # audio
        majors = [m['name'] for m in s.get('majors', [])]
        if majors:
            first = majors[0]
            mt = major_text(first)
            guide = s['campus']['guide']
            s['audioScript'] = [
                '%s。%s' % (s['name'], s['sub']),
                '先看专业。%s的 6 个代表专业是%s。比如%s，主要学%s，毕业去%s。' % (
                    s['name'], '、'.join(majors), first, mt[0], mt[1]),
                s['audioScript'][2],
                '最后看看校园。%s%s 校训是“%s”。下一站，%s。' % (
                    guide[0], guide[2], s['campus']['quote'], s.get('short', s['name'])),
            ]
        s['series'] = series
    return data


def save(path, data, order, var_order):
    body = '/* %s */\n' % ('50 所 211：逐校内容；不含分省分数' if len(data) == 50 else '34 所标准版 985：逐校内容；不含分省分数')
    body += '(function(){\n'
    body += '  var extra = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n'
    body += '  Object.assign(window.SCHOOLS, extra);\n'
    body += '  window.%s = %s;\n' % (var_order, json.dumps(order, ensure_ascii=False))
    body += '})();\n'
    io.open(path, 'w', encoding='utf-8').write(body)
    print('wrote', path, len(data))


d211, o211 = load(os.path.join(ROOT, 'data', 'schools_211.js'))
d985, o985 = load(os.path.join(ROOT, 'data', 'schools_extra.js'))
save(os.path.join(ROOT, 'data', 'schools_211.js'), enrich(d211, P211, '211'), o211, 'SCHOOL_ORDER_211')
save(os.path.join(ROOT, 'data', 'schools_extra.js'), enrich(d985, P985, '985'), o985, 'SCHOOL_ORDER')
