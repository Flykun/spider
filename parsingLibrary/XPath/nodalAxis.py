from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

html = etree.HTML(text)

result = html.xpath('//li[1]/ancestor::*')  # 返回所有祖先节点
print(result)
result = html.xpath('//li[1]/ancestor::div')  # 返回只有div的祖先节点
print(result)
result = html.xpath('//li[1]/attribute::*')  # 返回li节点的所有属性值
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')  # 选择有属性的a节点
print(result)
result = html.xpath('//li[1]/descendant::span')  # 只包含span节点, 不包含a节点
print(result)
result = html.xpath('//li[1]/following::*[2]')  # 当前节点后的所有节点
print(result)
result = html.xpath('//li[1]/following-sibling::*')  # 所有后续同级节点
print(result)