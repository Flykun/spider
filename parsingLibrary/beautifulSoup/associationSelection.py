from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
# print(soup.p.contents) # 选择p元素的直接子节点
#
# print('----------------')
# for i, child in enumerate(soup.p.children):
#     # 直接子节点的列表
#     print(i, child)
#
# for i, child in enumerate(soup.p.descendants):
#     # 获取所有子孙节点
#     print(i, child)
#
# print(soup.a.parent)  # 获取a节点的父节点元素
# print(list(enumerate(soup.a.parents)))  # 获取所有祖先元素
# print(list(soup.a.parents)[0])  # 获取祖先元素中的第0个
# print(list(soup.a.parents)[0].attrs['class'])  # 获取元素属性
# print('Next Sibling', soup.a.next_sibling)  # 获取a的下一个兄弟元素
print(soup.a.next_sibling.string)  # 获取文本
# print('Prev Sibling', soup.a.previous_sibling)  # 获取a的上一个元素

