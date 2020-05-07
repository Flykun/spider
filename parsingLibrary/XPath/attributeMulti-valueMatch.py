from lxml import etree

# 属性多值匹配, 如果需要只匹配'class="li li-first"'中的'class=li', 需要使用contains(@class, li)
text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)

result = html.xpath('//li[contains(@class, li)]/a/text()')

print(result)
