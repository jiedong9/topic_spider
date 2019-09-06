from requests_html import HTMLSession
import re

session = HTMLSession()
headers = {
    'Host':
    'www.51zhishang.com',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
}
# url = 'https://www.51zhishang.com/shiti/tk-st-67956.html'
url = 'https://www.51zhishang.com/shiti/tk-st-178944.html'

resp = session.get(url, headers=headers, allow_redirects=False)
print(resp.status_code)

title = resp.html.xpath(
    "//div[contains(@class,'i-panel')]/div[2]/div/div/p/span/text() | //div[contains(@class,'i-panel')]/div[2]/div/p//text() | //div[contains(@class,'i-panel')]/div[2]/div/div[1]//text()"
)
print(title)

print('-------------------------------------------------------')
number = resp.html.xpath(
    "//div[contains(@class,'i-panel')]/div[2]/div/ul[1]/li/span/text() | //div[contains(@class,'i-panel')]/div[2]/div/div[2]/div/div[1]//text()"
)

option = resp.html.xpath(
    "//div[contains(@class,'i-panel')]/div[2]/div/ul[1]/li/div//text() | //div[contains(@class,'i-panel')]/div[2]/div/div[2]/div/div[2]//text()"
)

print(number)
print('-------------------------------------------------------')
print(option)

answer = ''.join(
    resp.html.xpath("//div[contains(@id,'i-tab-content')]/text()")).replace(
        '\n', '').replace(' ', '')
print(answer)

analysis_re = ''.join(
    resp.html.xpath(
        "//div[contains(@id,'i-tab-content2')]/p/text() | //div[contains(@class,'KeyAalysisCenter')]//text()"
    )).replace('\u3000', '').replace('\xa0', '')
analysis_re = re.compile(r'【(.*?)】').sub('', analysis_re)
print(analysis_re)