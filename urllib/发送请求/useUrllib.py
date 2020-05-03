import urllib.request
import urllib.parse
import socket
import urllib.error

"""
# 发送请求
response = urllib.requests.urlopen('https://www.python.org')
print(response.status)  # 响应状态码
print(response.getheaders())  # 响应头信息
print(response.getheader('Server'))  # 响应服务器
"""

"""
# data参数
# 模拟表单提交
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.requests.urlopen('http://httpbin.org/post', data=data)
print(response.read())
"""

# timeout 参数 --超时

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.2)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('连接超时')