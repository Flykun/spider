# spider  

## 基本库的使用  

### urllib  

1. 发送请求
    1. urlopen()
    
        最基本的GET请求抓取
    
        ```python
        response = urllib.request.urlopen('http://www.python.org')
        print(response.read(), decode('utf8'))
        ```
    
    2. data参数
    
        最基本的POST请求抓取, 可选参数
    
        ```python
        data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
        response = urllib.request.urlopen('http://httpbin.org/post', data=data)
        print(response.read())
        ```
    
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
    
        反序列化, 将GET请求参数转回字典
    
        ```python
        print(parse_qs('name=wong&age=22'))
        # {'name': ['wong'], 'age': 22}
        ```
    
    8. parse_qsl()
    
        反序列化, 将参数转化为元组组成的列表
    
        ```python
        print(parse_qsl('name=wong&age=22'))
        # [('name', 'wong'), ('age', 22)]
        ```
    
    9. quote()
    
        将内容转化为URL编码
    
        ```python
        url = 'https://www.baidu.com/s?wd=' + quote('壁纸')
        print(url)
        # https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8
        ```
    
    10. unquote()
    
        URL解码
    
        ```python
        url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
        print(unquote())
        # 'https://www.baidu.com/s?wd=' + quote('壁纸')
        ```
4. 分析Robots协议
    1. Robots协议
    
        爬虫协议, 一般有robots.txt文件, 放在网站根目录下
    
        ```txt
        User-agent: *
        Disallwo: /
        Allow: /public/
        ```
    
    2. 爬虫名称
    
        |  爬虫名称   |  名称   |      网站      |
        | :---------: | :-----: | :------------: |
        |   Google    |  百度   | www.baidu.com  |
        | BaiduSpider |  谷歌   | www.google.com |
        |  360Spider  | 360搜索 |   www.so.com   |
    
    3. robotparse
    
        解析robots.txt, 只需要将robots.txt链接传入
    
        ```python
        urllib.robotparse.RobotFileParser(url='')
        ```
    
        * set_url()
    
          设置robots.txt链接
    
        * **read()**
    
          读取文件并分析, 一定要调用
    
        * parse()
    
          解析文件
    
        * can_fetch()
    
          传入两个参数, User-agent, URL, 返回是否可以抓取
    
        * **mtime()**
    
          返回分析时间, 很有必要
    
        * modified()
    
          将当前时间设置为抓取和分析时间
    
        
