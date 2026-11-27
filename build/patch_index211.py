# -*- coding: utf-8 -*-
import io
p = 'index211.html'
s = io.open(p, encoding='utf-8').read()
s = s.replace('<title>我的大学 · 985 系列</title>', '<title>我的大学 · 211 系列</title>')
s = s.replace('content:"985";', 'content:"211";')
s = s.replace('<span class="kicker">我的大学 · 985 系列</span>', '<span class="kicker">我的大学 · 211 系列</span>')
s = s.replace('<a class="hero-major" href="major.html">专业介绍样例 · 计算机科学与技术 →</a>',
              '<a class="hero-major" href="majors.html">专业目录 · 30 个通用专业 →</a>')
s = s.replace('<div class="hero-stat"><b>39</b><span>所 985 高校</span></div>', '<div class="hero-stat"><b>50</b><span>所 211 高校</span></div>')
s = s.replace('<div class="hero-stat"><b>234</b><span>个王牌专业</span></div>', '<div class="hero-stat"><b>300</b><span>个王牌专业</span></div>')
s = s.replace('<div class="hero-stat"><b>21</b><span>座城市</span></div>', '<div class="hero-stat"><b>19</b><span>座城市</span></div>')
s = s.replace('共 <b id="count">39</b> 所', '共 <b id="count">50</b> 所')
s = s.replace('从 39 所里挑一所', '从 50 所里挑一所')
s = s.replace('<a class="major-teaser" href="major.html">', '<a class="major-teaser" href="majors.html">')
s = s.replace('<div class="k">专业介绍 · SAMPLE</div>\n      <h3>计算机科学与技术</h3>\n      <p>学什么、四年怎么过、毕业做什么、适合谁。</p>',
              '<div class="k">专业目录 · 30 个</div>\n      <h3>从计算机到临床医学</h3>\n      <p>学什么、几年怎么过、毕业做什么、适合谁。</p>')
s = s.replace('39 所均不含分省录取分数。深度版含 A+、2025 届深造/就业；标准版含 2026 届保研率、A+ / 强势专业、6 个王牌专业和就业方向。',
              '50 所均不含分省录取分数。标准版含 2026 届保研率、A+ / 强势专业、6 个王牌专业和就业方向。')
s = s.replace('<script src="data/dut_rich.js"></script>', '<script src="data/dut_rich.js"></script>\n<script src="data/schools_211.js"></script>')
s = s.replace('var ids = window.SCHOOL_ORDER.filter', 'var ids = window.SCHOOL_ORDER_211.filter')
io.open(p, 'w', encoding='utf-8').write(s)
print('patched', s.count('985'), s.count('39'))
