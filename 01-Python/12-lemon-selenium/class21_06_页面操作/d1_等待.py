# @Author : jiaojie
# @CreateDate : 2020/5/20 21:17
# @Description : 第76节
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
1. 强制等待
2. 隐式等待
全局的监控，初始化一次浏览器的时候，只需要设置一次（初始化浏览器之后，添加）
查找元素
3. 显示等待


"""

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# 隐式等待
driver.implicitly_wait(5)
driver.get('http://www.baidu.com')

#搜索框（部分元素，异步请求，ajax）
# 显示等待
# 初始化一个计时器
# alt + enter 快速导入
wait = WebDriverWait(driver, 5, poll_frequency=0.2)
#elem = driver.find_element_by_id('kw')
try:
    elem = wait.until(EC.visibility_of_element_located("id", "kw"))
except TimeoutException:
    print("超时，没有找到")



