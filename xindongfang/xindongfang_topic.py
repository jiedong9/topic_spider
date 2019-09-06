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
yijian_fagui = database.fagui_xindongfangyijian
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
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-140.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-141.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-142.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-143.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-144.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-145.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-146.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-147.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-148.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-149.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-150.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-151.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-152.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-153.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-154.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-155.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-156.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-157.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-158.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-159.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-160.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-161.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-162.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-163.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-164.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-165.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-166.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-167.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-168.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-169.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-170.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-171.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-172.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-173.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-174.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-175.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-176.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-177.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-178.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-179.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-180.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-181.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-182.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-183.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-184.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-185.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-186.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-187.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-188.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-189.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-190.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-191.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-192.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-193.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-194.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-195.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-196.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-197.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-198.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-199.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-200.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-201.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-202.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-203.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-204.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-205.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-206.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-207.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-208.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-209.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-210.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-211.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-212.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-213.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-214.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-215.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-216.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-217.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-218.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-219.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-220.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-221.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-222.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-223.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-224.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-225.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-226.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-227.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-228.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-229.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-230.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-231.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-232.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-233.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-234.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-235.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-236.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-237.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-238.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-239.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-240.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-241.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-242.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-243.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-244.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-245.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-246.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-247.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-248.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-249.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-250.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-251.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-252.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-253.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-254.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-255.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-256.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-257.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-258.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-259.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-260.html",
    "https://www.51zhishang.com/shiti/tk-7-39-210-0-261.html",
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
            yijian_fagui.insert_one(item)
            print('{} ---插入数据库成功'.format(item['title']))
        except Exception as e:
            print('详情页抓取错误-------{}'.format(e))
            continue
        all_time = time.perf_counter() - start_time
        print('抓取用时{}'.format(all_time))


if __name__ == "__main__":
    url_yeild = topic_url()
    detial_content(url_yeild)
