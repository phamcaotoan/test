from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


test_driver = webdriver.Chrome()

#Step 1: Di chuyển đến địa chỉ "https://vlogtruyen.net"
test_driver.get('https://www.nettruyenco.com')


#Step 2: Bấm vào button "Đăng nhập"
test_driver.find_element(By.CSS_SELECTOR, '#header > div > div > ul > li.login-link > a').click()

test_driver.implicitly_wait(4)

# Step 3: Nhập username
test_driver.find_element(By.XPATH, '/html/body/form/main/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div[1]/input').send_keys('toanit.uda@gmail.com')


# Step 4: Nhập password
test_driver.find_element(By.XPATH, '/html/body/form/main/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div[2]/input').send_keys('toanphamcao')

# Step 5: Bấm vào button "Đăng nhập"
test_driver.find_element(By.XPATH, '/html/body/form/main/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/input').click()


#tắt testcase
# test_driver.close()
# test_driver.quit()