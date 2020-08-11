from selenium import webdriver


proxy = '127.0.0.1:9743'
chrome_options = webdriver.FirefoxOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Firefox(options=chrome_options)
browser.get('http://httpbin.org/get')