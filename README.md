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
        print('http://www.baidu.com' + urlencode(params))
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
    
### requests
1. 基本用法
    1. 准备工作
    
       安装requests库
    
    2. [实例引入](requests/基本用法/example.py)
    
    3. GET请求
        * [基本实例](requests/基本用法/example.py)
        * [抓取网页](requests/基本用法/page.py)
        * [抓取二进制数据](requests/基本用法/binary.py)
        * 添加headers
        ```python
           headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) 			AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 		  Safari/537.36'
           }
       ```
       
    4. [POST请求](requests/基本用法/postRequest.py)
    
    5. 响应
    
        [错误状态码](https://www.cnblogs.com/zhang12138/p/7711254.html)
2. 高级用法
    1. [文件上传](requests/高级用法/fileUpload.py)
    2. [Cookies](requests/基本用法/response.py)
    3. [会话维持](requests/高级用法/session.py)
    4. [SSL证书验证](requests/高级用法/SSL.py): verify参数
    5. [代理设置](requests/高级用法/proxies.py): proxies参数
    6. [超时设置](requests/高级用法/timeout.py)
    7. [身份验证](requests/高级用法/authentication.py)
    8. [**Prepared Request**](requests/高级用法/preparedRequest.py)
3. 正则表达式
    1. 实例引入  
        正则表达式测试工具 http://tool.oschina.net/regex/
    
    |  模式  |                          描述                          |
    | :----: | :----------------------------------------------------: |
    |   \w   |                 匹配字母, 数字及下划线                 |
    |   \W   |            匹配不是字母, 数字及下划线的字符            |
    |   \s   |                    匹配任意空白字符                    |
    |   \S   |                    匹配任意非空字符                    |
    |   \d   |               匹配任意数字, 等价于[0-9]                |
    |   \D   |                   匹配任意非数字字符                   |
    |   \A   |                     匹配字符串开头                     |
    |   \Z   | 匹配字符串结尾, 如果存在换行, 只匹配到换行前的结束字符 |
    |   \z   |      匹配字符串结尾, 如果存在换行, 还会匹配换行符      |
    |   \G   |                 匹配最后完成匹配的位置                 |
    |   \n   |                       匹配换行符                       |
    |   \t   |                       匹配制表符                       |
    |   ^    |                  匹配一行字符串的开头                  |
    |   $    |                  匹配一行字符串的结尾                  |
    |   .    |                匹配任意字符, 除了换行符                |
    | [...]  |                      表示一组字符                      |
    | [^...] |                     不在[]中的字符                     |
    |   *    |                 匹配0个或以上的表达式                  |
    |   +    |                 匹配1个或以上的表达式                  |
    |   ?    |                       非贪婪模式                       |
    |  {n}   |               精确匹配到n个前面的表达式                |
    | n, m)  |       匹配n到m次由正则表达式定义的片段, 贪婪模式       |
    |  a\|b  |                        匹配a或b                        |
    |   ()   |          匹配()内的表达式, 表示一个组group()           |
    
    2. [**match()**](requests/正则表达式/match.py)  
       
       从字符串的开头开始匹配, 开头不匹配, 整个匹配失败, 适用于检测
       匹配返回结果, 不匹配返回None
       
       * 匹配目标
       用()将要提取的内容括起来, 调用group()传入分组索引, 提取结果
       * 通用匹配
    万能匹配 '.*' , 代表无限次任意字符(换行符除外)
       * [贪婪与非贪婪](requests/正则表达式/greedyMatch.py)
       * 修饰符: 
       * 转移匹配: 遇到用于正则匹配模式的特殊字符时, 前面加反斜线\
       
    3. [search()](requests/正则表达式/search.py)
    
       搜索整个文本
    
    4. [findall()](requests/正则表达式/findall.py)
    
       返回匹配的所有内容
    
    5. [sub()](requests/正则表达式/sub.py)
    
       ```txt
       sub(pattern, repl, string, count=0, flags=0)
       pattern: 正则出需要去掉的字符
       repl: 替换成的字符串
       string: 原字符串
       ```
    
    6. [complie()](requests/正则表达式/compile.py)
    
       将正则字符串编译成正则表达式对象, 以便在后面的匹配中复用
4. [抓取猫眼电影排行](requests/抓取猫眼/maoyan.py)
    1. 目标
    2. 准备工作
    3. 抓取分析
    4. 抓取首页
    5. 正则提取
    6. 写入文件
    7. 整合代码
    8. 分页爬取
    9. 运行结果
    10. 代码

    

