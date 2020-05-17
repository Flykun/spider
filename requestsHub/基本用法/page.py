import requests
import re

# 如果不加headers, 返回400
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36'
}
r = requests.get("http://www.zhihu.com/explore", headers=headers)
print(r.text)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# title = re.findall(pattern, r.text)
# print(title)
