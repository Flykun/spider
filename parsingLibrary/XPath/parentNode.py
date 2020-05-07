from lxml import etree
from pprint import pprint


# 获取父节点, /../ 或者 /parent::*/
html = etree.parse('./test.html', etree.HTMLParser())

result = html.xpath('//a[@href="link4.html"]/../@class')
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
pprint(result)