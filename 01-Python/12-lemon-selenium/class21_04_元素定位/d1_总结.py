# @Author : jiaojie
# @CreateDate : 2020/5/17 19:37
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
id 元素
1. 唯一的
2. id是动态变化的，尽量不要使用id做定位
3. 不规则，编码后的

"""

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 通过id 进行元素定位
elem = driver.find_element_by_id('kw')
print(elem)

elems = driver.find_elements_by_id('kw')
print(elems)
