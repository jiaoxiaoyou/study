# @Author : jiaojie
# @CreateDate : 2020/5/17 19:20
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
测试流程：
1. 打开网站
2. 执行测试步骤
3. 断言

元素定位的方式去获取要操作的元素，然后才能进去点击，等操作
通过js的DOM，document.getElementById
selenium 封装了对应的方法 --> dom

"""

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

# 1. 定位
e = driver.find_element_by_id('kw')

# name
e = driver.find_element_by_name('wd')

# class_name
e = driver.find_element_by_class_name('s_lpt')

# tagname
e = driver.find_element_by_tag_name('input')

# link_text
e = driver.find_element_by_link_text()

# partial_link_text
e = driver.find_element_by_partial_link_text()

# xpath
# css_selector

"""
总结
selenium 原理
service, 
remoteconnection, 
subprocess()

get
find_element
execute() 访问webdriver 服务
"""


