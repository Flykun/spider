#spider  

##基本库的使用  

###urllib  

1. 发送请求
    1. urlopen()
    2. data参数
    3. timeout参数
    4. [Request](./urllib/useRequest.py)
    5. 高级用法
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
2. 异常处理
    1. URLError
    2. HTTPError
3. 解析链接
    1. urlparse()
        1. urlstring:
        2. scheme
        3. allow_fragments
    2. urlunparse()
    3. urlsplit()
    4. urlunsplit()
    5. urljoin()
    6. urlencode()
    7. parse_qs()
    8. parse_qsl()
    9. quote()
    10. unquote()
4. 分析Robots协议
    1. Robots协议
    2. 爬虫名称
    3. robotparse
        * set_url()
        * read()
        * parse()
        * can_fetch()
        * mtime()
        * modified()