from selenium import webdriver
import time
chromeDriver = webdriver.Chrome()
chromeDriver.get("http://www.baidu.com")
chromeDriver.maximize_window()
chromeDriver.find_element_by_id("kw").send_keys("秋裤")
chromeDriver.find_element_by_id("su").click()
time.sleep(3)
chromeDriver.quit()
