# -*- encoding: utf-8 -*-
'''
@File    :   xindongfang_topic.py
@Time    :   2019/09/05 09:37:51
@Author  :   Axi
@Version :   1.0
@Contact :   785934566@qq.com
@Desc    :   新东方在线爬虫
'''

# here put the import lib
import random
import time
import re

import pymongo
from requests.packages import urllib3
from requests_html import HTMLSession

urllib3.disable_warnings()

session = HTMLSession()
sleep_time = random.randint(1, 2)
# 连接数据库
client = pymongo.MongoClient('mongodb://114.67.96.255:27017')
database = client.xindongfang
yijian_insert = database.kuangye_xindongfangyijian
ua_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko)',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)',
    'Mozilla/5.0 (X11; U; Linux Core i7-4980HQ; de; rv:32.0; compatible; JobboerseBot; http://www.jobboerse.com/bot.htm) Gecko/20100101 Firefox/38.0',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
]
ua = random.choice(ua_list)

headers = {
    'Host': 'www.51zhishang.com',
    'user-agent': ua,
}

topic_urllist = [
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-1.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-2.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-3.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-4.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-5.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-6.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-7.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-8.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-9.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-10.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-11.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-12.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-13.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-14.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-15.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-16.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-17.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-18.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-19.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-20.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-21.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-22.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-23.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-24.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-25.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-26.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-27.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-28.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-29.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-30.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-31.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-32.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-33.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-34.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-35.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-36.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-37.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-38.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-39.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-40.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-41.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-42.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-43.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-44.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-45.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-46.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-47.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-48.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-49.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-50.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-51.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-52.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-53.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-54.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-55.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-56.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-57.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-58.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-59.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-60.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-61.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-62.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-63.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-64.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-65.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-66.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-67.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-68.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-69.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-70.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-71.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-72.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-73.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-74.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-75.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-76.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-77.html",
    "https://www.51zhishang.com/shiti/tk-7-39-2899-0-78.html",
]


def topic_url():
    for topic_url in topic_urllist:
        try:
            resp = session.get(
                topic_url,
                headers=headers,
            )
            time.sleep(sleep_time)
        except Exception as e:
            print('列表页出现错误-------{}'.format(e))
        url_list = resp.html.xpath("//div[@class='footer']/a")
        for url in url_list:
            url_yield = ''.join(url.absolute_links)
            yield url_yield


def detial_content(url_yeild):
    num = 0
    for url in url_yeild:
        print('正在抓取的列表页是-----{}'.format(url))
        start_time = time.perf_counter()
        try:
            resp = session.get(url, headers=headers)
            time.sleep(sleep_time)
            item = {}
            # 标题
            item['title'] = ''.join(
                resp.html.xpath(
                    "//div[contains(@class,'i-panel')]/div[2]/div/div/p/span/text() | //div[contains(@class,'i-panel')]/div[2]/div/p//text() | //div[contains(@class,'i-panel')]/div[2]/div/div[1]//text()"
                )).replace('\u3000', '').replace('\xa0', '').replace(' ', '')
            # 主体内容
            number = resp.html.xpath(
                "//div[contains(@class,'i-panel')]/div[2]/div/ul[1]/li/span/text() | //div[contains(@class,'i-panel')]/div[2]/div/div[2]/div/div[1]//text()"
            )

            option = resp.html.xpath(
                "//div[contains(@class,'i-panel')]/div[2]/div/ul[1]/li/div//text() | //div[contains(@class,'i-panel')]/div[2]/div/div[2]/div/div[2]//text()"
            )
            body_list = []
            for (n, o) in zip(number, option):
                content = '<p>' + n + ' ' + o + '</p>'
                body_list.append(content)
            body_list = '<p>' + item['title'] + '</p>' + ''.join(body_list)
            # 答案
            answer = ''.join(
                resp.html.xpath(
                    "//div[contains(@id,'i-tab-content')]/text()")).replace(
                        '\n', '').replace(' ', '')
            answer = '<p>' + '答案：' + answer + '</p>'

            # 解析
            analysis_re = ''.join(
                resp.html.xpath(
                    "//div[contains(@id,'i-tab-content2')]/p/text() | //div[contains(@class,'KeyAalysisCenter')]//text()"
                )).replace('\u3000', '').replace('\xa0', '')
            analysis_re = re.compile(r'【(.*?)】').sub('', analysis_re)
            analysis = '<p>' + '解析：' + analysis_re + '</p>'

            item['content'] = body_list + answer + analysis

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
        all_time = time.perf_counter() - start_time
        print('抓取用时{}'.format(all_time))
        print(
            '-------------------------------------------------------------------'
        )


if __name__ == "__main__":
    url_yeild = topic_url()
    detial_content(url_yeild)
