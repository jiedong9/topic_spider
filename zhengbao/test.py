# coding: utf-8

import re
# from requests_html import HTMLSession

# session = HTMLSession()

# url = 'http://m.jianshe99.com/jianzao/moniti/zh1509186348.shtml'
# r = session.get(url)
# item_title = ''.join(r.html.xpath("//h1/text()"))
# print(item_title)
# date_time = ''.join(
#     r.html.xpath("//div[@class='news-from fl']/text()")).strip()
# print(date_time)

# content = r.html.xpath("//div[@class='news-con font-size32']//p/text()")
# # print(content)
# if '建设工程教育网' in content[0]:
#     title = content[1]
#     print('-------标题是{}'.format(title))
# else:
#     title = content[0]
#     print(title)

# for a in content:
#     # a = a.strip().replace('\n', '')
#     if '建设工程教育网' in a:
#         pass
#     else:
#         print('<p>' + a + '</p>')

a = '<p>【单选题】实物量法编制施工图预算所用的材料单价应采用（）。</p><p>A.网上咨询厂家的报价</p><p>B.编制预算定额时采用的单价</p><p>C.当时当地的实际价格</p><p>D.预算定额中采用的单价加上运杂费</p><p>『正确答案』C</p><p>『答案解析』本题考查的是实物量法。采用实物量法编制施工图预算，需要全面收集各种人工、材料、机械的当时当地的实际价格。参见教材P222。</p>'

b = re.compile(r'(?<=。)参见教材.*?(?=<)').sub('', a)
# b = re.sub(r'^参见.*?。$', ' ', a)
print(b)
