from urllib import request, error

'''
HTTPError是URLError的子类
输入一个不存在的页面, 捕获HTTPError异常
返回状态码, 原因, 请求头
'''
'''
try:
    response = requests.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
'''
# 更好的写法
# 先捕获子类的异常, 再捕获父类的异常
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except  error.URLError as e:
    print(e.reason)
else:
    print('请求成功')
