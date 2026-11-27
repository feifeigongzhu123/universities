# -*- coding: utf-8 -*-
import io
s = io.open('data/schools_211.js', encoding='utf-8').read()
for p in ['读一所', '本科王牌专业', '核心课程、实验与实践', '对口行业、科研院所、继续深造',
          '国家级或校级特色方向', '把大学读成自己的作品', '校园通常很大，自行车是刚需',
          '图书馆和自习室，开学先踩点', '食堂和周边，先逛一圈再办卡', '从这里出发的人，正在各个行业里做事']:
    print(p, s.count(p))
s2 = io.open('data/schools_extra.js', encoding='utf-8').read()
print('--- 985 extra')
for p in ['读一所', '本科王牌专业', '核心课程、实验与实践', '把大学读成自己的作品', '校园通常很大，自行车是刚需']:
    print(p, s2.count(p))
