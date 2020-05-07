from lxml import etree
from pprint import pprint

html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li/a')  # 获取li下的子元素a
result = html.xpath('//li//a')  # 获取li下的子孙元素a
# result = html.xpath('//ul/a')  # []
pprint(result)
