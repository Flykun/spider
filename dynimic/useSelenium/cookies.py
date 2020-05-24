from selenium import webdriver

# cookies操作
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com')
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
