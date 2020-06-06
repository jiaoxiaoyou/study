# @Author : jiaojie
# @CreateDate : 2020/5/17 16:48
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

from selenium import webdriver

browser = webdriver.Chrome()

def game(a):
    if a > 5:
        print("美女")
    elif a < 0:
        print('帅哥')
    else:
        print('lalala')