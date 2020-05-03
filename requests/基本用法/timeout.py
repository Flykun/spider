import requests

# 请求分两个阶段, 请求连接, 请求读取
# timeout是读取和连接的总和, 可以用元组表示
# 默认情况下, 永远不会返回超时错误, 永久等待
r = requests.get('https://www.taobao.com', timeout=1)
# r = requests.get('https://www.taobao.com', timeout=(5, 30))
print(r.status_code)