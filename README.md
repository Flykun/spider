#spider  

##基本库的使用  

###urllib  

1. 发送请求

    urlopen()
    data参数
    timeout参数
2. [Request](./urllib/useRequest.py)

`url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Flykun'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read())`

3. 高级用法
    * HTTPDefaultErrorHandler: 处理错误响应
    * HTTPRedirectHandler: 处理重定向
    * HTTPCookieProcessor: 处理Cookie
    * ProxyHandler: 设置代理
    * HTTPPasswordMgr: 管理密码
    * HTTPBasicAuthHandler: 管理认证
    
    1. [验证](urllib/advanceCheck.py)  
    2. [代理](urllib/advanceAgent.py)  
    3. [Cookies](urllib/advanceCookies.py)  
        1. 获取Cookies
        2. 构造Handler
        3. 保存Cookies
        4. 生成Cookies文件
        5. 读取Cookies文件
    
    
    
