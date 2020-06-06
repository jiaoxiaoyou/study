# @Author : jiaojie
# @CreateDate : 2020/5/17 16:14
# @Description : 第64~66节
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
web 环境怎么安装

1. 安装selenium,怎么安装第三方库？
pip install -U selnium

2. webdriver 服务

web 自动化测试
1. 打开浏览器（驱动）
2. python 浏览器操作都是有一个东西支撑 --> 驱动
3. 驱动 --> 某种服务，HTTP接口 -->桥梁，客户端（手机，浏览器，电视） --> 服务

selenium 基于HTTP协议实现的

def get_url()  --> 服务  --> 浏览器

1. webdriver 必须和你浏览器品牌要对应
2. webdriver 必须和你的浏览器的版本要对应，

npm.taobao.org

标记语言：快速查找，精准定位

属性：
1. id   必须是唯一的
2. name
3. value
4. style
5. class
6. readonly和disabled
7. checked


window 当前浏览器窗口
document    当前窗口中显示的当前Html页面，文档

"""

from selenium import webdriver

# 初始化浏览器，打开浏览器
driver = webdriver.Chrome()
