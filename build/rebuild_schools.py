# -*- coding: utf-8 -*-
import io
import json
import os
import sys

ROOT = r"D:\AI\ZCode\universities"
sys.path.insert(0, os.path.join(ROOT, "build"))
from data_985_stats import BAOYAN, APLUS
from school_content import P211, P985, major_text
import more_211_data as M211

ROWS_985 = [
    ("ruc", "中国人民大学", "人大", "RENMIN UNIVERSITY OF CHINA", "北京", "北京", "华北", "综合", 1937, ["金融学", "经济学", "人力资源管理"], "#A6192E"),
    ("bnu", "北京师范大学", "北师", "BEIJING NORMAL UNIVERSITY", "北京", "北京", "华北", "师范", 1902, ["心理学", "汉语言文学", "教育学"], "#005A9C"),
    ("buaa", "北京航空航天大学", "北航", "BEIHANG UNIVERSITY", "北京", "北京", "华北", "理工", 1952, ["计算机科学与技术", "飞行器设计与工程", "电子信息工程"], "#1F4E79"),
    ("bit", "北京理工大学", "北理", "BEIJING INSTITUTE OF TECHNOLOGY", "北京", "北京", "华北", "理工", 1940, ["车辆工程", "信息工程", "计算机科学与技术"], "#2E6B3A"),
    ("cau", "中国农业大学", "农大", "CHINA AGRICULTURAL UNIVERSITY", "北京", "北京", "华北", "农林", 1905, ["食品质量与安全", "经济学类", "食品科学与工程"], "#2F6B3F"),
    ("muc", "中央民族大学", "民大", "MINZU UNIVERSITY OF CHINA", "北京", "北京", "华北", "民族", 1951, ["民族学", "中国少数民族语言文学", "法学"], "#8C1D40"),
    ("nankai", "南开大学", "南开", "NANKAI UNIVERSITY", "天津", "天津", "华北", "综合", 1919, ["金融学", "经济学", "数学类"], "#7A1F3D"),
    ("tju", "天津大学", "天大", "TIANJIN UNIVERSITY", "天津", "天津", "华北", "理工", 1895, ["建筑学", "工程管理", "化学工程与工艺"], "#003E74"),
    ("dut", "大连理工大学", "大工", "DALIAN UNIVERSITY OF TECHNOLOGY", "大连", "辽宁", "东北", "理工", 1949, ["机械设计制造及其自动化", "土木工程", "船舶与海洋工程"], "#1F4E79"),
    ("neu", "东北大学", "东大", "NORTHEASTERN UNIVERSITY", "沈阳", "辽宁", "东北", "理工", 1923, ["自动化", "计算机科学与技术", "机械工程及自动化"], "#1F4E79"),
    ("jlu", "吉林大学", "吉大", "JILIN UNIVERSITY", "长春", "吉林", "东北", "综合", 1946, ["车辆工程", "法学", "化学"], "#1F4E79"),
    ("hit", "哈尔滨工业大学", "哈工", "HARBIN INSTITUTE OF TECHNOLOGY", "哈尔滨", "黑龙江", "东北", "理工", 1920, ["机械设计制造及其自动化", "计算机科学与技术", "焊接技术与工程"], "#1F4E79"),
    ("tongji", "同济大学", "同济", "TONGJI UNIVERSITY", "上海", "上海", "华东", "综合", 1907, ["土木工程", "建筑学", "车辆工程"], "#003E74"),
    ("ecnu", "华东师范大学", "华师", "EAST CHINA NORMAL UNIVERSITY", "上海", "上海", "华东", "师范", 1951, ["心理学", "学前教育", "汉语言文学"], "#1F4E79"),
    ("nju", "南京大学", "南大", "NANJING UNIVERSITY", "南京", "江苏", "华东", "综合", 1902, ["经济学类", "计算机科学与技术", "天文学"], "#5B2C6F"),
    ("seu", "东南大学", "东南", "SOUTHEAST UNIVERSITY", "南京", "江苏", "华东", "综合", 1902, ["建筑学", "土木工程", "信息工程"], "#1F4E79"),
    ("ustc", "中国科学技术大学", "中科", "UNIVERSITY OF SCIENCE AND TECHNOLOGY OF CHINA", "合肥", "安徽", "华东", "理工", 1958, ["物理学", "数学类", "计算机科学与技术"], "#1F4E79"),
    ("xmu", "厦门大学", "厦大", "XIAMEN UNIVERSITY", "厦门", "福建", "华东", "综合", 1921, ["会计学", "金融学", "经济学"], "#005A9C"),
    ("sdu", "山东大学", "山大", "SHANDONG UNIVERSITY", "济南", "山东", "华东", "综合", 1901, ["数学类", "电气类", "经济学类"], "#A6192E"),
    ("ouc", "中国海洋大学", "海大", "OCEAN UNIVERSITY OF CHINA", "青岛", "山东", "华东", "综合", 1924, ["港口航道与海岸工程", "水产养殖学", "海洋科学"], "#005A9C"),
    ("whu", "武汉大学", "武大", "WUHAN UNIVERSITY", "武汉", "湖北", "华中", "综合", 1893, ["测绘工程", "法学", "经济学类"], "#2F6B3F"),
    ("hust", "华中科技大学", "华科", "HUAZHONG UNIVERSITY OF SCIENCE AND TECHNOLOGY", "武汉", "湖北", "华中", "综合", 1952, ["机械设计制造及其自动化", "临床医学", "光电信息科学与工程"], "#A6192E"),
    ("csu", "中南大学", "中南", "CENTRAL SOUTH UNIVERSITY", "长沙", "湖南", "华中", "综合", 2000, ["临床医学", "材料科学与工程", "冶金工程"], "#A6192E"),
    ("hnu", "湖南大学", "湖大", "HUNAN UNIVERSITY", "长沙", "湖南", "华中", "综合", 1903, ["土木工程", "金融学", "车辆工程"], "#A6192E"),
    ("nudt", "国防科技大学", "国防", "NATIONAL UNIVERSITY OF DEFENSE TECHNOLOGY", "长沙", "湖南", "华中", "军事", 1953, ["计算机科学与技术", "飞行器设计与工程", "信息与通信工程"], "#2E6B3A"),
    ("sysu", "中山大学", "中大", "SUN YAT-SEN UNIVERSITY", "广州", "广东", "华南", "综合", 1924, ["临床医学", "金融学", "经济学"], "#2F6B3F"),
    ("scut", "华南理工大学", "华工", "SOUTH CHINA UNIVERSITY OF TECHNOLOGY", "广州", "广东", "华南", "理工", 1952, ["建筑学", "电气工程及其自动化", "土木工程"], "#A6192E"),
    ("scu", "四川大学", "川大", "SICHUAN UNIVERSITY", "成都", "四川", "西南", "综合", 1896, ["口腔医学", "临床医学", "金融学"], "#A6192E"),
    ("uestc", "电子科技大学", "电科", "UNIVERSITY OF ELECTRONIC SCIENCE AND TECHNOLOGY OF CHINA", "成都", "四川", "西南", "理工", 1956, ["通信工程", "电子信息工程", "电磁场与无线技术"], "#1F4E79"),
    ("cqu", "重庆大学", "重大", "CHONGQING UNIVERSITY", "重庆", "重庆", "西南", "综合", 1929, ["建筑学", "土木工程", "电气工程与自动化"], "#A6192E"),
    ("xjtu", "西安交通大学", "西交", "XI'AN JIAOTONG UNIVERSITY", "西安", "陕西", "西北", "综合", 1896, ["电气工程及其自动化", "能源与动力工程", "机械工程"], "#A6192E"),
    ("npu", "西北工业大学", "西工", "NORTHWESTERN POLYTECHNICAL UNIVERSITY", "西安", "陕西", "西北", "理工", 1938, ["飞行器设计与工程", "飞行器动力工程", "自动化"], "#1F4E79"),
    ("nwafu", "西北农林科技大学", "西农", "NORTHWEST A&F UNIVERSITY", "杨凌", "陕西", "西北", "农林", 1934, ["水利水电工程", "葡萄与葡萄酒工程", "农业水利工程"], "#2F6B3F"),
    ("lzu", "兰州大学", "兰大", "LANZHOU UNIVERSITY", "兰州", "甘肃", "西北", "综合", 1909, ["化学", "物理学", "大气科学"], "#1F4E79"),
]

EXTRA985 = {
    "ruc": ["法学", "新闻学", "社会学"], "bnu": ["数学与应用数学", "地理科学", "历史学"],
    "buaa": ["自动化", "材料科学与工程", "软件工程"], "bit": ["武器系统与工程", "自动化", "材料科学与工程"],
    "cau": ["农学", "动物医学", "生物科学"], "muc": ["社会学", "历史学", "新闻学"],
    "nankai": ["化学", "统计学", "历史学"], "tju": ["机械设计制造及其自动化", "电气工程及其自动化", "土木工程"],
    "dut": ["化学工程与工艺", "计算机科学与技术", "工程力学"], "neu": ["材料科学与工程", "冶金工程", "采矿工程"],
    "jlu": ["临床医学", "数学与应用数学", "考古学"], "hit": ["飞行器设计与工程", "自动化", "土木工程"],
    "tongji": ["城乡规划", "环境工程", "交通工程"], "ecnu": ["数学与应用数学", "地理科学", "软件工程"],
    "nju": ["物理学", "化学", "汉语言文学"], "seu": ["电子科学与技术", "自动化", "交通工程"],
    "ustc": ["化学", "地球物理学", "生物科学"], "xmu": ["化学", "海洋科学", "法学"],
    "sdu": ["临床医学", "材料科学与工程", "中国语言文学"], "ouc": ["大气科学", "环境科学", "食品科学与工程"],
    "whu": ["遥感科学与技术", "计算机科学与技术", "口腔医学"], "hust": ["计算机科学与技术", "电气工程及其自动化", "预防医学"],
    "csu": ["计算机科学与技术", "土木工程", "矿业工程"], "hnu": ["工业设计", "化学", "电气工程及其自动化"],
    "nudt": ["光学工程", "管理科学与工程", "软件工程"], "sysu": ["计算机科学与技术", "法学", "哲学"],
    "scut": ["计算机科学与技术", "材料科学与工程", "食品科学与工程"], "scu": ["汉语言文学", "化学工程与工艺", "计算机科学与技术"],
    "uestc": ["计算机科学与技术", "微电子科学与工程", "人工智能"], "cqu": ["机械设计制造及其自动化", "计算机科学与技术", "临床医学"],
    "xjtu": ["计算机科学与技术", "临床医学", "工商管理"], "npu": ["计算机科学与技术", "材料科学与工程", "船舶与海洋工程"],
    "nwafu": ["农学", "林学", "动物医学"], "lzu": ["草业科学", "生态学", "历史学"],
}

ROWS_211 = [
    ("bjtu", "北京交通大学", "北交", "BEIJING JIAOTONG UNIVERSITY", "北京", "北京", "华北", "理工", 1896, ["交通运输", "系统科学与工程", "通信工程", "计算机科学与技术", "电气工程及其自动化", "土木工程"], "#1F4E79"),
    ("ustb", "北京科技大学", "北科", "UNIVERSITY OF SCIENCE AND TECHNOLOGY BEIJING", "北京", "北京", "华北", "理工", 1952, ["冶金工程", "材料科学与工程", "科学技术史", "机械工程", "自动化", "计算机科学与技术"], "#8C1D40"),
    ("bupt", "北京邮电大学", "北邮", "BEIJING UNIVERSITY OF POSTS AND TELECOMMUNICATIONS", "北京", "北京", "华北", "理工", 1955, ["通信工程", "信息工程", "计算机科学与技术", "电子科学与技术", "人工智能", "软件工程"], "#1F4E79"),
    ("buct", "北京化工大学", "北化", "BEIJING UNIVERSITY OF CHEMICAL TECHNOLOGY", "北京", "北京", "华北", "理工", 1958, ["化学工程与工艺", "高分子材料与工程", "材料科学与工程", "生物工程", "过程装备与控制工程", "计算机科学与技术"], "#2E6B3A"),
    ("bjfu", "北京林业大学", "北林", "BEIJING FORESTRY UNIVERSITY", "北京", "北京", "华北", "农林", 1952, ["林学", "风景园林", "园林", "水土保持与荒漠化防治", "木材科学与工程", "生物科学"], "#2F6B3F"),
    ("bucm", "北京中医药大学", "北中医", "BEIJING UNIVERSITY OF CHINESE MEDICINE", "北京", "北京", "华北", "医药", 1956, ["中医学", "中药学", "针灸推拿学", "中西医临床医学", "药学", "护理学"], "#7A1F3D"),
    ("bfsu", "北京外国语大学", "北外", "BEIJING FOREIGN STUDIES UNIVERSITY", "北京", "北京", "华北", "语言", 1941, ["英语", "翻译", "外交学", "法语", "西班牙语", "日语"], "#003E74"),
    ("cuc", "中国传媒大学", "中传", "COMMUNICATION UNIVERSITY OF CHINA", "北京", "北京", "华北", "综合", 1954, ["新闻学", "广播电视编导", "播音与主持艺术", "传播学", "广告学", "数字媒体艺术"], "#A6192E"),
    ("cufe", "中央财经大学", "央财", "CENTRAL UNIVERSITY OF FINANCE AND ECONOMICS", "北京", "北京", "华北", "财经", 1949, ["金融学", "会计学", "财政学", "经济学", "统计学", "保险学"], "#A6192E"),
    ("uibe", "对外经济贸易大学", "贸大", "UNIVERSITY OF INTERNATIONAL BUSINESS AND ECONOMICS", "北京", "北京", "华北", "财经", 1951, ["国际经济与贸易", "金融学", "法学", "会计学", "商务英语", "金融工程"], "#1F4E79"),
    ("cupl", "中国政法大学", "政法", "CHINA UNIVERSITY OF POLITICAL SCIENCE AND LAW", "北京", "北京", "华北", "政法", 1952, ["法学", "政治学与行政学", "国际政治", "社会学", "英语", "新闻学"], "#8C1D40"),
    ("ncepu", "华北电力大学", "华电", "NORTH CHINA ELECTRIC POWER UNIVERSITY", "北京", "北京", "华北", "理工", 1958, ["电气工程及其自动化", "能源与动力工程", "新能源科学与工程", "自动化", "核工程与核技术", "计算机科学与技术"], "#1F4E79"),
    ("lnu", "辽宁大学", "辽大", "LIAONING UNIVERSITY", "沈阳", "辽宁", "东北", "综合", 1948, ["经济学", "法学", "金融学", "国际经济与贸易", "工商管理", "新闻学"], "#8C1D40"),
    ("dmu", "大连海事大学", "海事", "DALIAN MARITIME UNIVERSITY", "大连", "辽宁", "东北", "理工", 1909, ["航海技术", "轮机工程", "交通运输", "法学", "物流管理", "船舶电子电气工程"], "#003E74"),
    ("ybu", "延边大学", "延大", "YANBIAN UNIVERSITY", "延吉", "吉林", "东北", "综合", 1949, ["朝鲜语", "汉语言文学", "临床医学", "法学", "药学", "护理学"], "#2F6B3F"),
    ("nenu", "东北师范大学", "东北师大", "NORTHEAST NORMAL UNIVERSITY", "长春", "吉林", "东北", "师范", 1946, ["教育学", "心理学", "汉语言文学", "数学与应用数学", "英语", "思想政治教育"], "#005A9C"),
    ("hrbeu", "哈尔滨工程大学", "哈工程", "HARBIN ENGINEERING UNIVERSITY", "哈尔滨", "黑龙江", "东北", "理工", 1953, ["船舶与海洋工程", "轮机工程", "自动化", "水声工程", "计算机科学与技术", "核工程与核技术"], "#1F4E79"),
    ("neau", "东北农业大学", "东北农大", "NORTHEAST AGRICULTURAL UNIVERSITY", "哈尔滨", "黑龙江", "东北", "农林", 1948, ["农学", "动物医学", "食品科学与工程", "园艺", "农业机械化及其自动化", "生物科学"], "#2F6B3F"),
    ("nefu", "东北林业大学", "东北林大", "NORTHEAST FORESTRY UNIVERSITY", "哈尔滨", "黑龙江", "东北", "农林", 1952, ["林学", "木材科学与工程", "森林保护", "园林", "野生动物与自然保护区管理", "土木工程"], "#2F6B3F"),
    ("ecust", "华东理工大学", "华理", "EAST CHINA UNIVERSITY OF SCIENCE AND TECHNOLOGY", "上海", "上海", "华东", "理工", 1952, ["化学工程与工艺", "应用化学", "材料科学与工程", "制药工程", "生物工程", "计算机科学与技术"], "#1F4E79"),
    ("dhu", "东华大学", "东华", "DONGHUA UNIVERSITY", "上海", "上海", "华东", "理工", 1951, ["纺织工程", "服装设计与工程", "材料科学与工程", "轻化工程", "视觉传达设计", "计算机科学与技术"], "#7A1F3D"),
    ("sufe", "上海财经大学", "上财", "SHANGHAI UNIVERSITY OF FINANCE AND ECONOMICS", "上海", "上海", "华东", "财经", 1917, ["金融学", "会计学", "经济学", "财政学", "统计学", "法学"], "#A6192E"),
    ("shu", "上海大学", "上大", "SHANGHAI UNIVERSITY", "上海", "上海", "华东", "综合", 1922, ["社会学", "美术学", "数字媒体艺术", "计算机科学与技术", "通信工程", "机械工程"], "#5B2C6F"),
    ("shisu", "上海外国语大学", "上外", "SHANGHAI INTERNATIONAL STUDIES UNIVERSITY", "上海", "上海", "华东", "语言", 1949, ["英语", "翻译", "德语", "法语", "西班牙语", "国际经济与贸易"], "#003E74"),
    ("suda", "苏州大学", "苏大", "SOOCHOW UNIVERSITY", "苏州", "江苏", "华东", "综合", 1900, ["材料科学与工程", "软件工程", "设计学", "临床医学", "法学", "汉语言文学"], "#8C1D40"),
    ("nuaa", "南京航空航天大学", "南航", "NANJING UNIVERSITY OF AERONAUTICS AND ASTRONAUTICS", "南京", "江苏", "华东", "理工", 1952, ["飞行器设计与工程", "飞行器动力工程", "自动化", "机械工程", "电气工程及其自动化", "计算机科学与技术"], "#1F4E79"),
    ("njust", "南京理工大学", "南理工", "NANJING UNIVERSITY OF SCIENCE AND TECHNOLOGY", "南京", "江苏", "华东", "理工", 1953, ["武器系统与工程", "自动化", "电子信息工程", "计算机科学与技术", "材料科学与工程", "机械工程"], "#2E6B3A"),
    ("hhu", "河海大学", "河海", "HOHAI UNIVERSITY", "南京", "江苏", "华东", "理工", 1915, ["水利水电工程", "水文与水资源工程", "港口航道与海岸工程", "土木工程", "环境工程", "电气工程及其自动化"], "#003E74"),
    ("jiangnan", "江南大学", "江南", "JIANGNAN UNIVERSITY", "无锡", "江苏", "华东", "综合", 1958, ["食品科学与工程", "生物工程", "工业设计", "轻化工程", "计算机科学与技术", "自动化"], "#7A1F3D"),
    ("njau", "南京农业大学", "南农", "NANJING AGRICULTURAL UNIVERSITY", "南京", "江苏", "华东", "农林", 1902, ["农学", "园艺", "动物医学", "食品科学与工程", "土地资源管理", "生物科学"], "#2F6B3F"),
    ("cpu", "中国药科大学", "药大", "CHINA PHARMACEUTICAL UNIVERSITY", "南京", "江苏", "华东", "医药", 1936, ["药学", "中药学", "药物制剂", "临床药学", "生物制药", "药事管理"], "#2E6B3A"),
    ("zzu", "郑州大学", "郑大", "ZHENGZHOU UNIVERSITY", "郑州", "河南", "华中", "综合", 1956, ["临床医学", "材料科学与工程", "化学", "法学", "土木工程", "计算机科学与技术"], "#8C1D40"),
    ("whut", "武汉理工大学", "武理工", "WUHAN UNIVERSITY OF TECHNOLOGY", "武汉", "湖北", "华中", "理工", 1948, ["材料科学与工程", "船舶与海洋工程", "车辆工程", "交通运输", "机械工程", "计算机科学与技术"], "#1F4E79"),
    ("ccnu", "华中师范大学", "华中师大", "CENTRAL CHINA NORMAL UNIVERSITY", "武汉", "湖北", "华中", "师范", 1903, ["教育学", "心理学", "汉语言文学", "数学与应用数学", "英语", "政治学与行政学"], "#005A9C"),
    ("zuel", "中南财经政法大学", "中南财", "ZHONGNAN UNIVERSITY OF ECONOMICS AND LAW", "武汉", "湖北", "华中", "财经", 1948, ["法学", "金融学", "会计学", "经济学", "财政学", "工商管理"], "#A6192E"),
    ("hzau", "华中农业大学", "华中农", "HUAZHONG AGRICULTURAL UNIVERSITY", "武汉", "湖北", "华中", "农林", 1898, ["农学", "园艺", "动物医学", "食品科学与工程", "生物科学", "农业资源与环境"], "#2F6B3F"),
    ("hunnu", "湖南师范大学", "湖南师大", "HUNAN NORMAL UNIVERSITY", "长沙", "湖南", "华中", "师范", 1938, ["汉语言文学", "英语", "教育学", "数学与应用数学", "临床医学", "法学"], "#A6192E"),
    ("ncu", "南昌大学", "南昌大学", "NANCHANG UNIVERSITY", "南昌", "江西", "华中", "综合", 1921, ["食品科学与工程", "材料科学与工程", "临床医学", "计算机科学与技术", "电气工程及其自动化", "法学"], "#8C1D40"),
    ("jnu", "暨南大学", "暨大", "JINAN UNIVERSITY", "广州", "广东", "华南", "综合", 1906, ["新闻学", "金融学", "会计学", "临床医学", "法学", "汉语言文学"], "#A6192E"),
    ("scnu", "华南师范大学", "华南师大", "SOUTH CHINA NORMAL UNIVERSITY", "广州", "广东", "华南", "师范", 1933, ["心理学", "教育学", "计算机科学与技术", "数学与应用数学", "汉语言文学", "物理学"], "#005A9C"),
    ("gxu", "广西大学", "广西大学", "GUANGXI UNIVERSITY", "南宁", "广西", "华南", "综合", 1928, ["土木工程", "电气工程及其自动化", "农学", "计算机科学与技术", "法学", "新闻学"], "#2F6B3F"),
    ("hainu", "海南大学", "海南大学", "HAINAN UNIVERSITY", "海口", "海南", "华南", "综合", 1958, ["农学", "法学", "旅游管理", "计算机科学与技术", "食品科学与工程", "国际经济与贸易"], "#005A9C"),
    ("fzu", "福州大学", "福大", "FUZHOU UNIVERSITY", "福州", "福建", "华东", "理工", 1958, ["化学", "电气工程及其自动化", "土木工程", "计算机科学与技术", "机械设计制造及其自动化", "会计学"], "#A6192E"),
    ("swu", "西南大学", "西南大学", "SOUTHWEST UNIVERSITY", "重庆", "重庆", "西南", "综合", 1906, ["教育学", "心理学", "农学", "汉语言文学", "计算机科学与技术", "食品科学与工程"], "#2F6B3F"),
    ("swjtu", "西南交通大学", "西南交大", "SOUTHWEST JIAOTONG UNIVERSITY", "成都", "四川", "西南", "理工", 1896, ["交通运输", "土木工程", "车辆工程", "电气工程及其自动化", "机械设计制造及其自动化", "计算机科学与技术"], "#1F4E79"),
    ("swufe", "西南财经大学", "西财", "SOUTHWESTERN UNIVERSITY OF FINANCE AND ECONOMICS", "成都", "四川", "西南", "财经", 1925, ["金融学", "会计学", "经济学", "财务管理", "统计学", "法学"], "#A6192E"),
    ("ynu", "云南大学", "云大", "YUNNAN UNIVERSITY", "昆明", "云南", "西南", "综合", 1922, ["民族学", "生态学", "汉语言文学", "计算机科学与技术", "法学", "新闻学"], "#2F6B3F"),
    ("nwu", "西北大学", "西北大学", "NORTHWEST UNIVERSITY", "西安", "陕西", "西北", "综合", 1902, ["考古学", "经济学", "化学", "汉语言文学", "计算机科学与技术", "地质学"], "#5B2C6F"),
    ("xidian", "西安电子科技大学", "西电", "XIDIAN UNIVERSITY", "西安", "陕西", "西北", "理工", 1931, ["电子信息工程", "通信工程", "计算机科学与技术", "微电子科学与工程", "人工智能", "软件工程"], "#1F4E79"),
    ("snnu", "陕西师范大学", "陕师大", "SHAANXI NORMAL UNIVERSITY", "西安", "陕西", "西北", "师范", 1944, ["汉语言文学", "教育学", "数学与应用数学", "英语", "心理学", "物理学"], "#005A9B"),
]

BAOYAN211 = {
    "bjtu": 20, "ustb": 22, "bupt": 24, "buct": 18, "bjfu": 20, "bucm": 20, "bfsu": 24, "cuc": 20,
    "cufe": 20, "uibe": 20, "cupl": 22, "ncepu": 20, "lnu": 14, "dmu": 18, "ybu": 12, "nenu": 24,
    "hrbeu": 22, "neau": 15, "nefu": 18, "ecust": 20, "dhu": 18, "sufe": 20, "shu": 16, "shisu": 20,
    "suda": 18, "nuaa": 22, "njust": 22, "hhu": 20, "jiangnan": 18, "njau": 20, "cpu": 20, "zzu": 15,
    "whut": 18, "ccnu": 20, "zuel": 18, "hzau": 20, "hunnu": 15, "ncu": 14, "jnu": 18, "scnu": 18,
    "gxu": 12, "hainu": 12, "fzu": 15, "swu": 18, "swjtu": 20, "swufe": 20, "ynu": 14, "nwu": 18,
    "xidian": 22, "snnu": 18,
}

APLUS211 = {
    "bjtu": (1, ["系统科学"]), "ustb": (2, ["冶金工程", "科学技术史"]), "bupt": (1, ["信息与通信工程"]),
    "bjfu": (2, ["林学", "风景园林学"]), "bucm": (2, ["中医学", "中西医结合"]), "bfsu": (1, ["外国语言文学"]),
    "cuc": (2, ["新闻传播学", "戏剧与影视学"]), "cufe": (1, ["应用经济学"]), "cupl": (1, ["法学"]),
    "nenu": (1, ["马克思主义理论"]), "hrbeu": (1, ["船舶与海洋工程"]), "ecust": (1, ["化学工程与技术"]),
    "dhu": (1, ["纺织科学与工程"]), "shisu": (1, ["外国语言文学"]), "njust": (1, ["兵器科学与技术"]),
    "hhu": (1, ["水利工程"]), "jiangnan": (2, ["食品科学与工程", "轻工技术与工程"]),
    "njau": (2, ["作物学", "农业资源与环境"]), "cpu": (1, ["药学"]), "whut": (1, ["材料科学与工程"]),
    "hzau": (3, ["园艺学", "畜牧学", "兽医学"]), "scnu": (1, ["心理学"]), "swjtu": (1, ["交通运输工程"]),
    "ynu": (1, ["民族学"]), "nwu": (1, ["考古学"]), "xidian": (1, ["电子科学与技术"]),
}

INDUSTRY_RULES = [
    (["计算机", "软件", "人工智能", "电子", "通信", "自动化", "微电子", "光电", "信息"], ["互联网", "芯片", "智能制造"]),
    (["机械", "车辆", "航空", "飞行器", "能源", "动力", "船舶", "海洋", "兵器", "武器", "核"], ["装备制造", "航空航天", "能源电力"]),
    (["材料", "化工", "化学", "环境", "生物", "食品", "药学", "临床", "口腔", "中医", "中药", "护理"], ["材料化工", "医药健康", "新能源"]),
    (["土木", "建筑", "水利", "交通", "城乡规划", "航海", "轮机"], ["建筑基建", "设计院", "交通运输"]),
    (["经济", "金融", "会计", "管理", "工商", "统计", "财政", "保险", "贸易"], ["金融", "咨询", "央企"]),
    (["法学", "新闻", "中文", "外语", "哲学", "历史", "社会学", "民族", "政治"], ["法律", "媒体", "公共部门"]),
    (["农学", "林学", "动物", "草业", "生态", "水产", "园艺"], ["农业", "食品", "生物科技"]),
]


def industries(majors):
    text = "".join(majors)
    out = []
    for keys, tags in INDUSTRY_RULES:
        if any(k in text for k in keys):
            for t in tags:
                if t not in out:
                    out.append(t)
    return out[:5]


def dark(hex_color, f=0.32):
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return "#%02X%02X%02X" % (int(r * f), int(g * f), int(b * f))


def make(rec, profiles, series, by_map, ap_map):
    sid, name, short, en, city, province, region, typ, year, majors, color = rec
    by = by_map.get(sid, 20)
    ap, ap_names = ap_map.get(sid, (0, []))
    prof = profiles.get(sid)
    hook = prof[0] if prof else "在%s，读一所%s强校。" % (city, typ)
    sub = prof[1] if prof else "%s，%s 高校。" % (name, series)
    guide = prof[2] if prof else ["校园通常很大，自行车是刚需。", "图书馆和自习室，开学先踩点。", "食堂和周边，先逛一圈再办卡。"]
    quote = prof[3] if prof else "把大学读成自己的作品。"
    quote_by = prof[4] if prof else ("校训" if series == "211" else "《大学》")
    objs = []
    for m in majors:
        learn, go, feature = major_text(m)
        objs.append({"name": m, "sub": "代表专业", "learn": learn, "go": go, "feature": feature, "tags": ["代表", "本科"]})
    inds = industries(majors)
    ap_mini = {"n": str(ap) + "个", "l": "A+ 学科"} if ap else {"n": "6个", "l": "代表专业"}
    audio = [
        "%s。%s" % (name, sub),
        "先看专业。%s的 6 个代表专业是%s。比如%s，主要学%s，毕业去%s。" % (
            name, "、".join(majors), majors[0], major_text(majors[0])[0], major_text(majors[0])[1]),
        "%s 2026届保研率约%s%%；%s；毕业生主要去%s。" % (
            name, by, ("A+学科%s个，包括%s" % (ap, "、".join(ap_names))) if ap_names else "6个代表专业值得看", "、".join(inds)),
        "最后看看校园。%s%s 校训是“%s”。下一站，%s。" % (guide[0], guide[2], quote, short),
    ]
    return {
        "id": sid, "name": name, "short": short, "nick": short, "place": short, "en": en,
        "city": city, "province": province, "region": region, "type": typ,
        "series": series, "tags": [series], "color": color, "dark": dark(color),
        "accent": "#C9A063", "paper": "#F5F0E6", "ink": "#241A26", "standard": True, "ap": ap,
        "emblem": {"type": "mono", "text": short, "sub": str(year), "color": color}, "landmark": "standard",
        "hook": hook, "sub": sub,
        "stats": [
            {"n": "6", "u": "个", "l": "代表专业", "s": "本科特色"},
            {"n": str(by), "u": "%", "l": "2026届保研率", "s": "第三方统计"},
            {"n": str(year), "u": "", "l": "建校", "s": "年"},
            {"n": typ, "u": "", "l": "类型", "s": "%s 高校" % series},
        ],
        "majors": objs,
        "outcome": {
            "big": str(by), "unit": "%", "label": "2026届保研率", "note": "第三方统计口径",
            "minis": ([ap_mini, {"n": "6个", "l": "代表专业"}, {"n": str(year), "l": "建校"}] if ap else
                      [{"n": "6个", "l": "代表专业"}, {"n": str(year), "l": "建校"}, {"n": typ, "l": "类型"}]),
            "companies": ap_names if ap_names else majors,
            "quote": ("A+ 学科：" + "、".join(ap_names)) if ap_names else "6 个代表专业：" + "、".join(majors),
            "source": "学科评估 / 2026届保研统计 / 就业方向", "industries": inds,
        },
        "scores": [],
        "campus": {
            "facts": [{"n": str(year), "l": "建校"}, {"n": "6", "l": "代表专业"}, {"n": typ, "l": "类型"}, {"n": series, "l": "工程"}],
            "keywords": [city, "校园", "图书馆", "校门"], "guide": guide,
            "alumni": "毕业生主要流向：" + "、".join(inds) + "。",
            "quote": quote, "quoteBy": quote_by,
        },
        "audioScript": audio,
    }


ROWS_211 += M211.ROWS
P211.update(M211.PROFILES)
BAOYAN211.update(M211.BAOYAN)
APLUS211.update(M211.APLUS)
d211 = {rec[0]: make(rec, P211, "211", BAOYAN211, APLUS211) for rec in ROWS_211}
d985 = {rec[0]: make(rec, P985, "985", BAOYAN, APLUS) for rec in ROWS_985}
# 985 standard: 6 majors = 3 base + 3 extra
for sid, rec in [(r[0], r) for r in ROWS_985]:
    base = rec[9] + EXTRA985.get(sid, [])
    d985[sid]["majors"] = d985[sid]["majors"][:3]
    for m in base[3:6]:
        learn, go, feature = major_text(m)
        d985[sid]["majors"].append({"name": m, "sub": "代表专业", "learn": learn, "go": go, "feature": feature, "tags": ["代表", "本科"]})
    majors = [m["name"] for m in d985[sid]["majors"]]
    inds = industries(majors)
    d985[sid]["outcome"]["industries"] = inds
    d985[sid]["outcome"]["companies"] = d985[sid]["outcome"]["companies"] if d985[sid]["ap"] else majors
    d985[sid]["campus"]["alumni"] = "毕业生主要流向：" + "、".join(inds) + "。"
    if not d985[sid]["ap"]:
        d985[sid]["outcome"]["quote"] = "6 个代表专业：" + "、".join(majors)
    d985[sid]["audioScript"][1] = "先看专业。%s的 6 个代表专业是%s。比如%s，主要学%s，毕业去%s。" % (
        d985[sid]["name"], "、".join(majors), majors[0], major_text(majors[0])[0], major_text(majors[0])[1])


def write(path, data, order, var):
    body = "/* %s 逐校内容；不含分省分数 */\n" % ("50 所 211" if var.endswith("211") else "34 所标准版 985")
    body += "(function(){\n  var extra = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n"
    body += "  Object.assign(window.SCHOOLS, extra);\n"
    body += "  window.%s = %s;\n})();\n" % (var, json.dumps(order, ensure_ascii=False))
    io.open(path, "w", encoding="utf-8").write(body)
    print("wrote", path, len(data))


write(os.path.join(ROOT, "data", "schools_211.js"), d211, [r[0] for r in ROWS_211], "SCHOOL_ORDER_211")
write(os.path.join(ROOT, "data", "schools_extra.js"), d985, ["tsinghua", "pku", "fudan", "sjtu", "zju"] + [r[0] for r in ROWS_985], "SCHOOL_ORDER")
