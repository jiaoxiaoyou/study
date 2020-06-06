# @Author : jiaojie
# @CreateDate : 2020/5/18 20:52
# @Description : 第75节 web 页面-web页面操作（一） 47：00
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
1.selenium 是采用什么网络协议实现的框架？简书selenium 原理

答：HTTP

2. 在百度首页搜索柠檬班，进入柠檬班腾讯课堂，并定位其中的某位老师
3. 自己写一个html页面，并定位其中的元素
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('C:/Personal/Study/Python/lemon-selenium/class21_04_元素定位/first.html')




# find_element_by_id
sex = driver.find_element_by_id('sex')
print(sex)

# find_element_by_name
lastname = driver.find_element_by_name("lastname")
print(lastname)

# find_element_by_class
bike_input = driver.find_element_by_class_name('input')
print(input)

# find_element_by_tag_name
male_input = driver.find_elements_by_tag_name('input')[2]
print(male_input)

# find_element_by_partial_link_text
# a_link = driver.find_element_by_partial_link_text("这是一个链接")
# a_link.click()

# find_element_by_xpath
# firstname = driver.find_element_by_xpath("//form/input[@name='firstname']")
# print(firstname)



