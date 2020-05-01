from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

'''
在打开时弹出提示框, 验证用户名和密码后才能查看页面
1. 实例化HTTPBasicAuthHandler对象
2. 利用add_password()添加用户名和密码
'''
username = 'username'
password = 'password'
url = 'http://localhost:5000'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf8')
    print(html)

except URLError as e:
    print(e.reason)
