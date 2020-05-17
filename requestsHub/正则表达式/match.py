import re

content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}', content)
# result = re.match('^Hello\s(\d+)\s\d+\s\w+', content)
result = re.match('^Hello.*Demo$', content)
# result = re.match('^Hello\s(\d+)\s\d+\s\w+', content)

if __name__ == '__main__':
    print(len(content))  # 41
    print(result)  # <re.Match object; span=(0, 25), match='Hello 123 4567 World_This'>
    print(result.group())  # Hello 123 4567 World_This
    print(result.span())  # (0, 25)
