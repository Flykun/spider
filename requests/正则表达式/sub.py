import re

"""
去掉文本中的一部分
sub(pattern, repl, string, count=0, flags=0)
pattern: 正则出需要去掉的字符
repl: 替换成的字符串
string: 原字符串
尝试提取class为active的li节点内部的超链接包含的歌手名和歌名
"""
content = '54aK54yr5oiRE54ix32L2Gh'
html = """<div id="song-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>"""
html = re.sub('<a.*?>|</a>', '', html)

results = re.findall('<li.*?>(.*?)</li>', html, re.S)

if __name__ == '__main__':
    print(f"content: {content}")
    print(results)
    for result in results:
        print(result.strip())
