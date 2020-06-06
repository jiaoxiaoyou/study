# @Author : jiaojie
# @CreateDate : 2020/5/20 21:54
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
iframe
1. 索引
2. name属性
3. iframe WebElement

从iframe切换到默认的HTML
switch_to.default_content()

"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://ke.qq.com/webcourse/index.html#cid=290702&term_id=100495449&taid=3338113007251342&vid=5285890794846834967')



