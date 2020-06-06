# @Author : jiaojie
# @CreateDate : 2020/5/20 20:29
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
 打开课堂派，通过 xpath 表达式定位元素


- 通过 f12 的 ctrl + f 输入表达式，确保元素唯一；
- 写出页面、元素和对应的表达式
- 写出 py 文件

"""
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

search_input = driver.find_element_by_id('kw')
search_input.send_keys('课堂派')

search_btn= driver.find_element_by_id('su')
search_btn.click()

sleep(1)
# 课堂派链接
#ktp_link = driver.find_element_by_link_text("https://www.ketangpai.com/")

driver.get("https://www.ketangpai.com/")

# 首页
home_page = driver.find_element_by_class_name('active')
#home_page = driver.find_element_by_xpath("//div[@id='indextop']/div[contains(@class, 'nav')]/a")

print(home_page)