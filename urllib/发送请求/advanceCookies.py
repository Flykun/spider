import http.cookiejar, urllib.request

# 生成Cookie文件
filename = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

'''
# 读取Cookie文件
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.requests.HTTPCookieProcessor(cookie)
opener = urllib.requests.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf8'))
'''