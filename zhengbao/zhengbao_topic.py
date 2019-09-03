# coding: utf-8
"""
抓取内容：
    正保建设网试题资料抓取，包括一级建造师，二级建造师，一级造价工程师，消防工程师，监理工程师，安全工程师
抓取步骤：
    第一：构造列表页url，按照科目分类，将标题，时间存入数据库存入mongodb数据库zhengbao_topic的zhengbao_urllist表中
    第二：抓取试题详情，抓取字段，标题，时间，内容，url存入zhengbaotopic_detial表中
"""

import pymongo
import re
import time
import random
from requests_html import HTMLSession

session = HTMLSession()
sleep_time = random.randint(1, 2)
# 连接数据库
client = pymongo.MongoClient('mongodb://114.67.96.255:27017')
database = client.zhengbaotopic_detial
yijian_doc = database.zhengbao_yijian
ua_list = [
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G610M Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; SM-J111M Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; Moto E (4) Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700M Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; Redmi Note 3 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 OPR/11.2.3.102637 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-J701MT Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/56.0.2924.87 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G920F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532M Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.2 Chrome/44.0.2403.133 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G950F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.2 Chrome/51.0.2704.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; LG-M250 Build/NRD90U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-J710MN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; LG-M250 Build/NRD90U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7",
    "Mozilla/5.0 (Linux; Android 7.0; Moto G (5) Build/NPPS25.137-93-2-5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; Moto G Play Build/NPIS26.48-43-2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9515 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/LMY48B ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; ANE-LX3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Xoom Build/IML77) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Safari/535.7",
    "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI VNS-L21 Build/HUAWEIVNS-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; LG-K430 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G900F Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; Moto G (5S) Build/NPPS26.102-49-4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G930F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G975F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; Moto G (5S) Build/NPPS26.102-49-14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; MYA-L03 Build/HUAWEIMYA-L03) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; Moto G (5S)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.2; Lenovo B8080-F Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T530 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G955F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; Moto G Play Build/NPIS26.48-43-2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; TRT-L53 Build/HUAWEITRT-L53) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G800F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G935F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-G935F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
]
ua = random.choice(ua_list)
headers = {'User-Agent': ua, 'Host': 'm.jianshe99.com'}

topic_urllist = [
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_1.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_2.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_3.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_4.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_5.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_6.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_7.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_8.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_9.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_10.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_11.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_12.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_13.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_14.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_15.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_16.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_17.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_18.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_19.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_20.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_21.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_22.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_23.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_24.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_25.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_26.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_27.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_28.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_29.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_30.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_31.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_32.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_33.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_34.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_35.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_36.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_37.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_38.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_39.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_40.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_41.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_42.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_43.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_44.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_45.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_46.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_47.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_48.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_49.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_50.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_51.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_52.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_53.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_54.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_55.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_56.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_57.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_58.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_59.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_60.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_61.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_62.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_63.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_64.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_65.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_66.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_67.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_68.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_69.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_70.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_71.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_72.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_73.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_74.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_75.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_76.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_77.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_78.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_79.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_80.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_81.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_82.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_83.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_84.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_85.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_86.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_87.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_88.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_89.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_90.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_91.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_92.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_93.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_94.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_95.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_96.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_97.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_98.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_99.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_100.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_101.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_102.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_103.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_104.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_105.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_106.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_107.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_108.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_109.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_110.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_111.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_112.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_113.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_114.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_115.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_116.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_117.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_118.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_119.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_120.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_121.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_122.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_123.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_124.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_125.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_126.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_127.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_128.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_129.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_130.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_131.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_132.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_133.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_134.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_135.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_136.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_137.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_138.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_139.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_140.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_141.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_142.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_143.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_144.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_145.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_146.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_147.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_148.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_149.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_150.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_151.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_152.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_153.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_154.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_155.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_156.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_157.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_158.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_159.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_160.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_161.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_162.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_163.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_164.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_165.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_166.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_167.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_168.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_169.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_170.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_171.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_172.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_173.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_174.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_175.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_176.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_177.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_178.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_179.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_180.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_181.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_182.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_183.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_184.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_185.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_186.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_187.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_188.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_189.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_190.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_191.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_192.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_193.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_194.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_195.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_196.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_197.shtml",
    "http://m.jianshe99.com/zcms/catalog/12097/Html5/index_198.shtml",
]


def topic_url():
    """
    读取url
    :param :
    :return:
    """
    for topicurl in topic_urllist:
        try:
            r = session.get(topicurl, headers=headers)
        except Exception as e:
            print('列表页出现错误-------{}'.format(e))
        url_list = r.html.xpath("//*[@class='tex auto']/p/a")
        for url in url_list:
            url_yeild = ''.join(url.absolute_links)
            yield url_yeild


def detial_content(url_yeild):
    num = 0
    for url in url_yeild:
        time.sleep(sleep_time)
        try:
            r = session.get(url, headers=headers)
            item = {}
            item['item_title'] = ''.join(r.html.xpath(
                "//h1/text()")).replace('\u3000', '')  # 分类标题
            # print('------分类标题：' + item['item_title'])

            item['date_time'] = ''.join(
                r.html.xpath(
                    "//div[@class='news-from fl']/text()")).strip()  # 时间
            # print('------文章时间：' + item['date_time'])

            content_list = r.html.xpath(
                "//div[@class='news-con font-size32']//p/text()")
            if '建设工程教育网' in content_list[0]:
                item['title'] = content_list[1].replace('\u3000', '')  # 内容题目
                print('-------标题是{}'.format(item['title']))
            else:
                item['title'] = content_list[0].replace('\u3000', '')
                print('-------标题是{}'.format(item['title']))

            con = []
            for content in content_list:  # 内容详情
                if '建设工程教育网' in content:
                    continue
                else:
                    content = ('<p>' + content + '</p>').replace('\u3000', '')
                    content_clear = re.compile(
                        r'(?<=。)参见教材.*?(?=<)').sub('', content)  # 匹配参见教材
                    con.append(content_clear)
            item['content'] = ''.join(con)
            item['url'] = url  # 内容url
            # print(item)
            num += 1
            print('-------正在抓取第{}个'.format(num))
            yijian_doc.insert_one(item)
            print('插入数据库成功-----{}'.format(item['title']))
        except Exception as e:
            print('详情页抓取错误-------{}'.format(e))
            continue


if __name__ == '__main__':
    url_yeild = topic_url()
    detial_content(url_yeild)
