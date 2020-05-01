from urllib import request, parse

"""
# 请求对象与urlopen不同
request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read())
"""

# 传入多个参数的Request
url = 'http://httpbin.org/post'
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
print(response.read())
