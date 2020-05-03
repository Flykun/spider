import requests

data = {
    'name': 'wong',
    'age': 22
}
r = requests.get('http://www.httpbin.org/get', params=data)

print(r.text)
print(r.json())
