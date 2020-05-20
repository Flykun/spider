"""
首先，这里定义了 base_url 来表示请求的 URL 的前半部分。接下来，构造参数字典，其中 type、value 和 containerid 是固定参数，page 是可变参数。
接下来，调用 urlencode 方法将参数转化为 URL 的 GET 请求参数，即类似于
type=uid&value=2145291155&containerid=1076032145291155&page=2 这样的形式。
随后，base_url 与参数拼合形成一个新的 URL。接着，我们用 requests 请求这个链接，加入 headers 参数。
然后判断响应的状态码，如果是 200，则直接调用 json 方法将内容解析为 JSON 返回，否则不返回任何信息。
如果出现异常，则捕获并输出其异常信息。
"""

import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

client = MongoClient()
db = client['weibo']
collection = db['weibo']
max_page = 10


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json(), page
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json, page: int):
    if json:
        items = json.get('data').get('cards')
        for index, item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
                item = item.get('mblog', {})
                weibo = {}
                weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                yield weibo


def save_to_mongo(result):
    if collection.insert(result):
        print('Saved to Mongo')


if __name__ == '__main__':
    for page in range(1, max_page + 1):
        json = get_page(page)
        results = parse_page(*json)
        for result in results:
            print(result)
            save_to_mongo(result)
