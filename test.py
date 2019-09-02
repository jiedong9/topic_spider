# coding: utf-8

from requests_html import HTMLSession

session = HTMLSession()

url = 'http://m.jianshe99.com/jianzao/moniti/zh1509186348.shtml'
r = session.get(url)
item_title = ''.join(r.html.xpath("//h1/text()"))
print(item_title)
date_time = ''.join(
    r.html.xpath("//div[@class='news-from fl']/text()")).strip()
print(date_time)

content = r.html.xpath("//div[@class='news-con font-size32']//p/text()")
# print(content)
if '建设工程教育网' in content[0]:
    title = content[1]
    print('-------标题是{}'.format(title))
else:
    title = content[0]
    print(title)

for a in content:
    # a = a.strip().replace('\n', '')
    if '建设工程教育网' in a:
        pass
    else:
        print('<p>' + a + '</p>')