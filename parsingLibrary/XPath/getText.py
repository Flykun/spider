from lxml import etree
from pprint import pprint


# 获取文本, text()
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()')

pprint(result)