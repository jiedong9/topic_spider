# -*- encoding: utf-8 -*-
'''
@File    :   zhonghua_topic.py
@Time    :   2019/09/04 08:55:40
@Author  :   Axi
@Version :   1.0
@Contact :   785934566@qq.com
@Desc    :   中华考试网考试题爬虫
'''

# here put the import lib

import random
import time

import pymongo
from requests.packages import urllib3
from requests_html import HTMLSession

urllib3.disable_warnings()

session = HTMLSession()
sleep_time = random.randint(1, 2)
# 连接数据库
client = pymongo.MongoClient('mongodb://114.67.96.255:27017')
database = client.zhonghuaexam
yijian_insert = database.zhonghuayijian_tongxin
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

headers = {
    'user-agent': ua,
}

topic_urllist = [
    "https://m.examw.com/jzs1/tongxin/kaodian/index.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-2.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-3.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-4.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-5.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-6.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-7.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-8.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-9.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-10.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-11.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-12.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-13.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-14.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-15.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-16.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-17.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-18.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-19.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-20.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-21.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-22.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-23.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-24.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-25.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-26.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-27.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-28.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-29.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-30.html",
    "https://m.examw.com/jzs1/tongxin/kaodian/index-31.html",
]


def topic_url():
    for topic_url in topic_urllist:
        try:
            resp = session.get(
                topic_url,
                headers=headers,
                verify=False,
            )
            time.sleep(sleep_time)
            resp.encoding = 'gb2312'
        except Exception as e:
            print('列表页出现错误-------{}'.format(e))
        url_list = resp.html.xpath(
            "//div[contains(@class,'categoryBox')]/ul/li/a")
        for url in url_list:
            url_yield = ''.join(url.absolute_links)
            yield url_yield


def detial_content(url_yeild):
    num = 0
    for url in url_yeild:
        try:
            resp = session.get(url, headers=headers, verify=False)
            time.sleep(sleep_time)
            item = {}
            # 标题
            item['title'] = ''.join(
                resp.html.xpath(
                    "//div[contains(@class,'newsBox')]/h2/span/text()"))
            # 时间
            item['datetime'] = ''.join(
                resp.html.xpath("//*[contains(@class,'time')]/span[2]/text()"))

            # 内容
            content_list = resp.html.xpath("//*[contains(@id,'Tiku')]//text()")
            con = []
            for content in content_list:
                content = content.replace('查看试题解析', '').replace('进入焚题库', '')
                if content == '\n' or content == '\xa0' or content == '':
                    continue
                else:
                    content = '<p>' + content + '</p>'
                    con.append(
                        content.replace('\u3000', '').replace('\xa0', ''))
                item['content'] = ''.join(con)
            # url
            item['url'] = url
            print(item)
            num += 1
            print('=======正在抓取的是第 {} 个========='.format(num))
            yijian_insert.insert_one(item)
            print('{} ---插入数据库成功'.format(item['title']))
        except Exception as e:
            print('详情页抓取错误-------{}'.format(e))
            continue


if __name__ == "__main__":
    url_yeild = topic_url()
    detial_content(url_yeild)
