# @Author : jiaojie
# @CreateDate : 2020/5/18 20:55
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
2. 在百度首页搜索柠檬班，进入柠檬班腾讯课堂，并定位其中的某位老师
"""
import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 定位输入框
input_elem = driver.find_element_by_id('kw')

# 输入柠檬班
input_elem.send_keys("柠檬班")

# 定位"百度一下"按钮
driver.find_element_by_id('su').click()

#
time.sleep(1)
lemon = driver.find_element_by_partial_link_text("https://lemon.ke.qq.com/")

#lemon.click() 是因为click是新窗口打开所以定位不到吗？
driver.get("https://lemon.ke.qq.com/")

teacher = driver.find_element_by_class_name("teacher-face-a")
print(teacher)
