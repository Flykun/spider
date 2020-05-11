from bs4 import BeautifulSoup

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
# findall(name, attrs, recursive, text, **kwargs)

# # name
# soup = BeautifulSoup(html, 'lxml')
# # print(soup.find_all(name='ul'))  # 根据节点选择元素
# # print(soup.find_all(name='ul')[0]) # 根据节点选择元素
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):
#         print(li.string)

# attrs

# 根据属性查询
soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(attrs={'id': 'list-1'}))
# print(soup.find_all(id='list-1'))  # 同上
# print(soup.find_all(attrs={'name': 'elements'}))
# print(soup.find_all(class_='element'))  # 同上, 避开关键字
