from requests import Request, Session

# 将请求表示为数据结构
url = 'http://httpbin.org/post'
data = {
    'name': 'wong'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36',
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)

if __name__ == '__main__':
    print(r.text)

