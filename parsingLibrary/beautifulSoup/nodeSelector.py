from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
print(soup.title)  # 获取标题 <title>The Dormouse's story</title>
print(type(soup.title))  # 所有的都是输出Tag类型, 既包含文本, 也包含节点
print(soup.title.name)  # 获取节点名称 title
print(soup.head)  # 获取头部信息 <head><title>The Dormouse's story</title></head>
print(soup.p)  # 只显示第一个头部信息, 其他的会自动忽略  <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
print(soup.p.attrs)  # 获取节点属性 {'class': ['title'], 'name': 'dromouse'}
print(soup.p.attrs['name'])  # 获取节点属性 返回字符串 dromouse
print(soup.p['class'])  # 获取节点属性 返回列表 ['title'], 省略attrs
print(soup.p.string)  # 获取节点文本 The Dormouse's story

