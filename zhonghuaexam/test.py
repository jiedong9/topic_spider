# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2019/09/04 11:24:33
@Author  :   Axi
@Version :   1.0
@Contact :   785934566@qq.com
@Desc    :   None
'''

# here put the import lib

from requests_html import HTMLSession
session = HTMLSession()

url = 'http://www.k51.com.cn/QuestDetail/887408e6-5724-40bc-9251-8235b55c9220.html'
resp = session.get(url)

# title = ''.join(resp.html.xpath(
#     "//div[contains(@class,'newsBox')]/h2/span/text()"))
# print(title)

content = resp.html.xpath(
    "//div[contains(@class,'cont-details-cont-topic')]/ul/li//text()")
print(content)
for a in content:
    print('<p>' + a + '</p>')
