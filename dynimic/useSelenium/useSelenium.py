from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_index = browser.find_element_by_id('q')  # 查找单个节点
# input = browser.find_element(By.ID, 'q')  # 同上
# li = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
input_index.send_keys('头盔')
input_index.send_keys(Keys.ENTER)
time.sleep(3)

browser.close()
