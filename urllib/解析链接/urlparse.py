from urllib.parse import urlparse

result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https', allow_fragments=False)

if __name__ == '__main__':
    print(result)

'''
<class 'urllib.parse.ParseResult'>
ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', 
params='user', query='id=5', fragment='comment')
'''
