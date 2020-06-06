# @Author : jiaojie
# @CreateDate : 2020/5/18 20:24
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
轴定位
//input//parent::span

//input[@id="kw"]//ancestor::form[@id="form"]

child
descendant
preceding-sibling
following-sibling
//input[@name="ie"]//following-sibling::input

//input[@name="ie"]//following-sibling::input[@name="f"]



"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
