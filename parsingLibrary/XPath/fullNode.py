from lxml import etree
from pprint import pprint


html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//*')
result = html.xpath('//li')
pprint(result)
pprint(result[0])