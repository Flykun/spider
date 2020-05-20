import requests
from urllib.parse import urlencode
from multiprocessing.pool import Pool
import os
from hashlib import md5

GROUP_START = 1
GROUP_END = 20


def get_page(offset):
    # 加载单个Ajax请求
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '3'
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    # 提取每条数据中的图片链接, 返回图片链接和所属标题
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_detail')
            for image in images:
                yield {
                    'image': image.get('url'),
                    'title': title
                }


def save_image(item):
    # 根据title创建文件夹, 请求图片链接, 获取图片的二进制数据, 以二进制形式写入文件
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = f"{item.get('title')}/{md5(response.content).hexdigest()}.{'jpg'}"
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Download', file_path)
    except requests.ConnectionError:
        print('Filed to Save Image')


def main(offset):
    # 遍历offset, 提取图片链接, 并下载
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()