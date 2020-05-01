from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

'''
在本地搭建一个代理, 运行在9743端口
使用ProxyHandler, 参数是一个字典
构造一个Opener, 发送请求
'''

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf8'))
except URLError as e:
    print(e.reason)
