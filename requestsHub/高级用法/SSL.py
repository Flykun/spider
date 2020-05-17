import requests
from requests import packages

# 可以使用, 如果提示证书验证错误, 则需要传入verify参数, 检查证书, 默认为True
response = requests.get('https://www.12306.cn')
package
print(response.status_code)

#