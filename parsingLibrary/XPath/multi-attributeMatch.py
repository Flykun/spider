from lxml import etree

# 获取多个属性
text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''

html = etree.HTML(text)

result = html.xpath('//li[contains(@class, li) and @name="item"]/a/text()')
print(result)