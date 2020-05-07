from lxml import etree

# 获取属性
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')

print(result)