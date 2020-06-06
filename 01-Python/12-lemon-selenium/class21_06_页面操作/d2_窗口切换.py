# @Author : jiaojie
# @CreateDate : 2020/5/20 21:31
# @Description : 第76节
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 定位输入框
input_elem = driver.find_element_by_id('kw')

# 输入柠檬班
input_elem.send_keys("柠檬班")

# 定位"百度一下"按钮
driver.find_element_by_id('su').click()

#
wait = WebDriverWait(driver, 20, poll_frequency=0.2)
lemon = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"https://lemon.ke.qq.com/")))
#lemon = driver.find_element_by_partial_link_text("https://lemon.ke.qq.com/")

# lemon.click() #是因为click是新窗口打开所以定位不到吗？
# # ketang = driver.get("https://lemon.ke.qq.com/")
# # ketang.click()
# time.sleep(1)
#
# # 获取所有的窗口，这个获取所有窗口必须是click之后
# window = driver.window_handles
# driver.switch_to.window(window[1])
#
# wait = WebDriverWait(driver, 20, poll_frequency=0.2)
# teacher = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "teacher-face-a")))
# #teacher = driver.find_element_by_class_name("teacher-face-a")
# print(teacher)

windows = driver.window_handles
# 等待窗口打开
lemon.click()
wait = WebDriverWait(driver, 20)
wait.until(EC.new_window_is_opened(windows))
print(driver.window_handles)
driver.switch_to.window(windows[1])
