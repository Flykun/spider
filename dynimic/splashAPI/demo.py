import requests

url = 'http://192.168.99.100:8050/render.html?url=https://www.taobao.com&wait=5'
response = requests.get(url)
print(response.text)