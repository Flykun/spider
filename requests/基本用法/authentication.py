import requests
from requests_auth.authentication import OAuth2

# 使用Oauth验证
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
r = requests.get(url=url, auth=OAuth2())
