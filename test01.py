from select import select

from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
test_driver = webdriver.Chrome()

# Di chuyển đến địa chỉ "http://www.nettruyenmoi.com/"
test_driver.get('http://www.nettruyenmoi.com/')

test_driver.implicitly_wait(8)          #chờ ngầm định

test_driver.find_element(By.CSS_SELECTOR, '#header > div > div > ul > li.login-link > a').click()

test_driver.implicitly_wait(4)

test_driver.find_element(By.XPATH, '/html/body/form/main/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/input').click()

