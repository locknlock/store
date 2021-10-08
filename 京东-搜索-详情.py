import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.jd.com")
time.sleep(5)
driver.maximize_window()
driver.find_element_by_id("key").send_keys("电脑")
driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a']").click()
time.sleep(10)
current_window = driver.current_window_handle
print("current_window:: ",current_window)
driver.find_element_by_xpath("//*[@class='gl-i-wrap']").click()
time.sleep(10)
all_window=driver.window_handles
print("all_window:: ",all_window)
for window in all_window:      #通过遍历判断要切换的窗口
 print("window:: ",window)
if window != current_window:
 driver.switch_to.window(window) 
 current_window = driver.current_window_handle
print("current_window:: ",current_window)
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
time.sleep(5)
driver.quit()
