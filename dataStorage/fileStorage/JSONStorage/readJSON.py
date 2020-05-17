import json

# 千万注意JSON字符串需要用"", 否则loads()会解析失败
str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
data = json.loads(str)
with open('data.json', 'w') as file:
    file.write(json.dumps(data, indent=2))