from lxml import etree
from pprint import pprint

# 用@符号进行属性过滤
# 选取class为item-0的li节点
html = etree.parse('./test.html', etree.HTMLParser())

result = html.xpath('//li[@class="item-0"]')

pprint(result)
