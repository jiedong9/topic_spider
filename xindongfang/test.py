import re

a = '降低工程质量标准，造成重大安全事故的。【题库维护老师ChenJ】'

b = re.compile(r'【(.*?)】').sub('', a)
print(b)
