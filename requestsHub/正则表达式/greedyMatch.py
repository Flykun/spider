import re

# string中尽量做非贪婪陪陪, 用.*?代替.*, 避免出现匹配结果缺失的情况
# 如果匹配的结果在字符串结尾, .*?可能匹配不到任何结果, 这时候需要贪婪匹配
content1 = 'Hello 1234567 World_This is a Regex Demo'
content2 = 'http://weibo.com/comment/kEraCN'
result1 = re.match('^He.*(\d+).*Demo$', content1)  # 贪婪匹配
result2 = re.match('^He.*?(\d+).*Demo$', content1)  # 非贪婪匹配
result3 = re.match('^http.*?/comment/(.*?)', content2)
result4 = re.match('^http.*?/comment/(.*)', content2)
if __name__ == '__main__':
    print(result1.group())
    print(result1.group(1))  # 7
    print(result2.group())
    print(result2.group(1))  # 1234567
    print(result3.group())
    print(result3.group(1))
    print(result4.group())
    print(result4.group(1))