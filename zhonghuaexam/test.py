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

url = 'https://m.examw.com/shiti/55419618/'
resp = session.get(url, verify=False)

title = ''.join(resp.html.xpath(
    "//div[contains(@class,'newsBox')]/h2/span/text()"))
print(title)

content = resp.html.xpath(
    "//*[contains(@id,'Tiku')]//text()")
for a in content:
    a = a.replace('查看试题解析', '').replace('进入焚题库', '')
    if a == '\n' or a == '\xa0' or a == '':
        continue
    else:
        print('<p>' + a + '</p>')
