from urllib import request, error

'''
URLError是HTTPError的父类
输入一个不存在的页面, 捕获URLError异常
'''

try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)
