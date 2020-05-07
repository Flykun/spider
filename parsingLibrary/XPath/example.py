from lxml import etree
import  pprint


text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

# 使用etree.tostring()进行代码补全
# html = etree.HTML(text)
# result = etree.tostring(html)
# pprint.pprint(result.decode('utf8'))

# 直接读取文本进行解析
html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf8'))
