# spider  

## 基本库的使用  

### urllib  

1. 发送请求
    1. urlopen()
    2. data参数
    3. timeout参数
    4. [Request](urllib/发送请求/useRequest.py)
    5. 高级用法
        * HTTPDefaultErrorHandler: 处理错误响应
        * HTTPRedirectHandler: 处理重定向
        * HTTPCookieProcessor: 处理Cookie
        * ProxyHandler: 设置代理
        * HTTPPasswordMgr: 管理密码
        * HTTPBasicAuthHandler: 管理认证
    
        1. [验证](urllib/发送请求/advanceCheck.py)  
        2. [代理](urllib/发送请求/advanceAgent.py)  
        3. [Cookies](urllib/发送请求/advanceCookies.py)  
            1. 获取Cookies
            2. 构造Handler
            3. 保存Cookies
            4. 生成Cookies文件
            5. 读取Cookies文件
2. 异常处理
    1. [URLError](urllib/处理异常/URLError.py)
    2. [HTTPError](urllib/处理异常/HTTPError.py)
    3. [异常判断](urllib/处理异常/timeoutError.py)
3. 解析链接
    1. **urlparse()**: 实现URL的识别和分段
        
        1. 返回对象
            返回的结果是一个ParseResult类型的对象
            
            得出一个标准链接格式`scheme://netloc/path;params?query#fragment` 
            
            包含六个部分
            
            1. scheme: 协议
            2. netloc: 域名
            3. path: 访问路径
            4. params: 参数
            5. query: 查询条件, 一般用于get请求
            5. fragment: 锚点, 定位页面的下拉位置
            ```python
            from urllib.parse import urlparse
            result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
            print(type(result), result)
            '''
            <class 'urllib.parse.ParseResult'>
            ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
            '''
            ```
            
        2. 参数
            1. urlstring: 必填项, 待解析的URL
        
            2. scheme: 默认协议
        
            3. allow_fragments: 是否忽略fragment, 如果被忽略, 则会被解析为path, params或query的一部分
        
               ```python
               from urllib.parse import urlparse
               result = urlparse('www.baidu.com/index.html;user?id=5#comment', 			scheme='https', allow_fragments=False)
               print(result)
               
               # ParseResult(scheme='https', netloc='', path='www.baidu.com/index.html', params='user', query='id=5#comment', fragment='')
               ```
        
    2. urlunparse()
    
        urlparse()的对立方法, 用于构造URL
    
        ```python
        print(urlunparse(['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']))
        ```
    
    3. urlsplit()
    
        非常类似于urlparse, 区别是只返回5个结果, 不再单独解析params, 将params合并于path
    
    4. urlunsplit()
    
        类似于urlunparse, 只接受长度为5的列表或元组(不用params)
    
    5. **urljoin()**
    
        类似于urlunparse(), 最少需要两个参数就可以构造URL, 其他的可以自动补充
    
        ```python
        from urllib.parse import urljoin
        print(urljoin('http://www.baidu.com', 'FAQ.html'))
        ```
    
    6. **urlencode()**
    
        构造GET请求参数非常有用
    
        ```python
        params = {
            'name': 'yong',
            'age': 22
        }
        base_url = 'http://www.baidu.com'
        url = base_url + urlencode(params)
        print(url)
        ```
    
        
    
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
        
