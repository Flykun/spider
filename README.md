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


## 解析库的使用

### XPath

1. 概览

   字符串, 时间, 数值的匹配以及节点, 序列的处理

2. 常用规则

   |  表达式  |           描述           |
   | :------: | :----------------------: |
   | nodename |   选取此节点的所有节点   |
   |    /     | 从当前节点选取直接子节点 |
   |    //    |  从当前节点选取子孙节点  |
   |    .     |       选取当前节点       |
   |    ..    |   选取当前节点的父节点   |
   |    @     |         选取属性         |

3. 准备工作

   安装lxml库

4. [实例引入](parsingLibrary/XPath/example.py)

   调用etree模块自动修正或读取HTML文本

5. [所有节点](parsingLibrary/XPath/fullNode.py)

   以 // 开头的规则选取所有符合要求的节点

6. [子节点](parsingLibrary/XPath/childNode.py)

   通过 / 或 // 查找元素的子节点或子孙节点

7. [父节点](parsingLibrary/XPath/parentNode.py)

   .. 或者 parent::*

8. [属性匹配](parsingLibrary/XPath/attributeMatch.py)

   [@class="xx"]

9. [文本获取](parsingLibrary/XPath/getText.py)

   /text()

10. [属性获取](parsingLibrary/XPath/getAttributes.py)

    /@href

11. [属性多值匹配](parsingLibrary/XPath/attributeMulti-valueMatch.py)

    contains()

12. [多属性匹配]()

    匹配多个属性

    | 运算符 |   描述   |        实例        |    返回值     |
    | :----: | :------: | :----------------: | :-----------: |
    |   or   |    或    |  age=19 or age=20  | True or False |
    |  and   |    和    | age> 19 and age<22 | True or False |
    |  mod   |   余数   |      5 mod 2       |       1       |
    |   \|   |  节点集  |   //book \| //cd   |     合集      |
    |   +    |   加法   |        6+4         |      10       |
    |   -    |   减法   |        6-4         |       2       |
    |   *    |   乘法   |        6*4         |      24       |
    |  div   |   除法   |      8 div 4       |       2       |
    |   =    |   等于   |       age=19       | True or False |
    |   !=   |  不等于  |      age!=19       | True or False |
    |   <    |   小于   |       age<19       | True or False |
    |   <=   | 小于等于 |      age<=19       | True or False |
    |   >    |   大于   |       age>19       | True or False |
    |   >=   | 大于等于 |      age>=19       | True or False |

13. [按序选择](parsingLibrary/XPath/sock.py)

    利用中括号传入索引

14. [节点轴选择](parsingLibrary/XPath/nodalAxis.py)

15. 结语

    熟练使用

### 使用Beautiful Soup

1. 简介
2. 准备工作
3. 解析器
4. 基本用法
5. [节点选择器](parsingLibrary/beautifulSoup/nodeSelector.py)
   * 选择元素
   * 提取信息
     1. 获取名称
     2. 获取属性
   * 嵌套选择
   * [关联选择](parsingLibrary/beautifulSoup/associationSelection.py)
     1. 子节点和子孙节点
     2. 父节点和祖先节点
     3. 兄弟节点
     4. 提取信息
6. 方法选择器
   * find_all()  
     fand_all(name, attrs, recursive, text, **kwargs)
     * name: 根据节点名查询元素
     * attrs: 根据属性查询元素
     * text: 匹配文本
   * find()
7. CSS选择器
   * 嵌套选择
   * 获取属性
   * 获取文本

### 使用pyquery

1. 准备工作
2. 初始化
   * 字符串初始化
   * URL初始化
   * 文件初始化
3. 基本CSS选择器
4. 查找结点
   * 子节点
   * 父节点
   * 兄弟节点
5. 遍历
6. 获取信息
   * 获取属性
   * 获取文本
7. 节点操作
   * addClass和removeClass
   * attr text和html
   * remove
8. 伪类选择器

## 数据存储

### 文件存储

1. [TXT文本存储](dataStorage/fileStorage/TXTStorage/example.py)

   1. 本节目标

   2. 基本实例

   3. 打开方式

   4. 简化写法

2. [JSON文件存储](dataStorage/fileStorage/JSONStorage/readJSON.py)

   1. 对象和数组
   2. 读取JSON
   3. 输出JSON

3. CSV文件存储

   1. [写入](dataStorage/fileStorage/CSVStorage/readData.py)
   2. [读取](dataStorage/fileStorage/CSVStorage/writeData.py)

### 关系型数据库存储

1. [MySQL的存储](dataStorage/fileStorage/mysqlStorage/connection.py)
   1. 准备工作
   2. 连接数据库
   3. 创建表
   4. 插入数据
   5. 更新数据
   6. 删除数据
   7. 查询数据

### 非关系型数据库存储

1. [MongoDB存储](dataStorage/fileStorage/mongodaStorage/mongoClient.py)
   1. 准备工作
   2. 连接MongoDB
   3. 指定数据库
   4. 指定集合
   5. 插入数据
   6. 查询
   7. 计数
   8. 排序
   9. 偏移
   10. 更新
   11. 删除
   12. 其他操作
2. Redis存储
   1. 准备工作
   2. Redis 和 StrictRedis
   3. 连接Redis
   4. 键操作
   5. 字符串操作
   6. 列表操作
   7. 集合操作
   8. 有序集合操作
   9. 散列操作
   10. RedisDump
       * redis-dump
       * redis-load

## Ajax 数据爬取

### 什么是Ajax  
异步的JavaScript和XML. 保证页面不被刷新, 页面链接不改变的情况下与服务器交换数据

1. 实例引入  
https://m.weibo.cn/u/2830678474
2. 基本原理
   1. [发送请求](ajaxSpider/weibo.js)
   
   2. 解析内容
   
      得到响应后, onreadystatechange属性对应的方法会被触发, 此时利用xmlhttp的responseText属性就可得到响应内容
   
      类似于python中利用requests向服务器发送请求, 然后得到响应的过程
   
   3. 渲染网页

### [Ajax分析方法](ajaxSpider/weibo.py)

1. 查看请求
2. 过滤请求

### [Ajax结果提取](ajaxSpider/weiboSpider.py)

1. 分析请求
2. 分析响应
3. 实战演练

### [分析Ajax爬取今日头条街拍美图](ajaxSpider/toutiao.py)

1. 准备工作
2. 抓取分析
3. 实战演练

## 动态渲染页面爬取

### Selenium的使用

1. 准备工作

   安装Selenium

2. [基本使用](dynimic/useSelenium/useSelenium.py)

3. [声明浏览器对象](dynimic/useSelenium/useSelenium.py)

4. [访问页面](dynimic/useSelenium/useSelenium.py)

5. [查找节点](dynimic/useSelenium/useSelenium.py)
   * 单个节点
   * 多个节点

6. [节点交互](dynimic/useSelenium/useSelenium.py)

7. [动作链](dynimic/useSelenium/actionChain.py)

8. [执行JavaScript](dynimic/useSelenium/javaScript.py)

9. [获取节点信息](dynimic/useSelenium/getNodeInfo.py)
   * 获取属性
   * 获取文本值
   * 获取id, 位置, 标签名和大小

10. [切换Frame](dynimic/useSelenium/cutFrame.py)

11. [延时等待](dynimic/useSelenium/backOrder.py)
    * 隐式等待
    * 显式等待

12. 前进和后退

    forward(): 前进

    back(): 后退

13. [Cookies](dynimic/useSelenium/cookies.py)

14. [选项卡管理](dynimic/useSelenium/tabControl.py)

15. [异常处理](dynimic/useSelenium/exceptionHandling.py)

### Splash的使用

JavaScript渲染服务, 是一个带有HTTP API服务的轻量级浏览器, 对接了Python中的Twisted和QT库

1. 功能介绍

   * 异步处理多个网页渲染过程
   * 获取渲染后的代码
   * 关闭图片渲染
   * 执行JavaScript脚本
   * 执行lua脚本
   * 获取渲染的详细过程

2. 准备工作

   安装Splash

3. 实例引入

   ```lua
   function main(splash, args)
     assert(splash:go(args.url))
     assert(splash:wait(0.5))
     return {
       html = splash:html(),
       png = splash:png(),
       har = splash:har(),
     }
   end
   ```

   

4. Splash Lua脚本

   基本实例

   ```lua
   function main(splash, args)
     splash:go("http://www.baidu.com")
     splash:wait(0.5)
     local title = splash:evaljs("document.title")
     return {
       title = title
     }
   end
   ```

   

   * 入口及返回值
   * 异步处理

5. Splash对象属性
   * args
   * js_enabled
   * resource_timeout
   * images_enabled
   * plugins_enabled
   * scroll_position

6. Splash对象的方法
   * go()
   * wait()
   * jsfunc()
   * evaljs()
   * runjs()
   * autoload()
   * call_later()
   * http_get()
   * http_post()
   * set_content()
   * html()
   * png()
   * jpeg()
   * har()
   * url()
   * get_cookies()
   * add_cookie()
   * clear_cookies()
   * get_viewport_size()
   * set_viewport_size()
   * set_viewport_full()
   * set_user_agent()
   * set_custom_headers()
   * select()
   * select_all()
   * mouse_click()

7. Splash API的使用
   * render.html
   * render.png
   * render.jpeg
   * render.har
   * render.json
   * execute

### Splash 负载均衡配置

1. 配置Splash服务
2. 配置负载均衡
3. 配置认证
4. 测试

### 使用Selenium爬取淘宝商品

1. 本节目标
2. 准备工作
3. 接口分析
4. 页面分析
5. 获取商品列表
6. 解析商品列表
7. 保存到mongodb
8. 遍历每页
9. 运行
10. Chrome Headless模式
11. 对接Firefox
12. 对接Phantom JS

## 模拟登录

### 模拟登录并爬取Github  
模拟登录后的页面抓取内容, 维护Cookies

1. 本节目标  
实现模拟登录, 爬取登录后的页面信息
2. 环境准备  
安装requests和lxml库
3. 分析登录过程  
如果已经登录, 退出, 清除cookies
4. 代码实战
5. 运行
6. 代码仓库
7. 结语
### Scrapy框架的使用

基于Twisted的异步处理框架

#### Scrapy框架介绍

1. 架构介绍

   ![spider](D:\spider\hub\scrapy.webp)

   * Engine. 引擎, 处理系统的数据流, 触发事务, 核心
   * Item. 项目, 定义爬取结构, 数据被赋值为该Item对象
   * Scheduler. 调度器, 接受引擎发过来的请求并将其加入队列中, 在引擎再次请求的时候将请求提供给引擎
   * Downloader. 下载器, 下载网页内容, 将内容返回Spider
   * Spiders. 定义爬取逻辑和网页的解析规则, 解析响应, 生成结果和新的请求
   * Item Pipeline. 管道, 清洗, 验证, 和存储数据
   * DownLoder Middlewares. 下载中间件
   * Spider Middleware. 蜘蛛中间件

2. 数据流

   Scrapy中的数据流由引擎控制, 过程如下

   1. Engine打开一个网站, 找到处理该网站的Spider, 请求要爬取的URL
   2. Engine从Spider中获取到第一个要爬取的URL, 并通过scheduler以Request的形式调度
   3. Engine向Scheduler请求下一个要爬取的URL
   4. Scheduler返回下一个要爬取的URL给Engine, 通过URL转发给Downloader下载
   5. 一旦页面下载完毕, Downloader生成该页面的Response, 发送给引擎
   6. Engine从下载器接受response, 发给Spider处理
   7. Spider处理Response, 提取Item及新的Request给Engine
   8. Engine将Spider返回的Item给Item Pipeline, 将新的Request给Scheduler
   9. 重复2-8, 直到结束

3. 项目结构

   * scrapy.cfg: 配置文件, 定义项目的配置文件路径, 部署相关信息
   * Items.py: 定义Item数据结构
   * Pipelines.py: 定义Item Pipeline的实现
   * settings.py: 定义项目的全局配置
   * middlewares.py: 中间件的实现
   * spiders: 爬虫

4. 结语

   基本架构, 数据流, 及项目结构

#### Scrapy入门

1. 本节目标

   * 创建一个Scrapy项目
   * 创建一个spider来抓取站点和处理数据
   * 通过命令行将内容导出
   * 将抓取的内容保存到mongodb

2. 准备工作

   安装scrapy

3. 创建项目

   ```commonlisp
   scrapy startproject tutorial
   ```

   

4. 创建Spider

   ```commonlisp
   cd tutorial
       scrapy genspider example example.com
   ```

   

5. 创建Item

   ```python
   import scrapy
   class QuoteItem(scrapy.Item):
       # define the fields for your item here like:
       text = scrapy.Field()
       author = scrapy.Field()
       tags = scrapy.Field()
   ```

   

6. 解析Response

7. 使用Item

8. 后续Request

9. 运行

10. 保存到文件

11. 使用Item Pipeline

12. 源代码

13. 结语 