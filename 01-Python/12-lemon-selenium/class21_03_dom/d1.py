# @Author : jiaojie
# @CreateDate : 2020/5/17 17:15
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
DOM：docuemnt object mode
POM: page object mode

document.title
document.URL

上一节作业
1. 用户名
2. 密码
3. 最喜欢的电影选择
4. 上传个人资料文件
5. 通过嵌入script 标签 在终端中打印用户名和选择的电影

"""

from selenium import webdriver

driver = webdriver.Chrome()

# 访问网址
url = 'http://www.baidu.com'
# 实际上是调用execute方法，通过urllib3发送http请求， --> webdriver服务器接口地址
driver.get(url)

# 获取网页的url
print(driver.current_url)

# 获取网页的标题
print(driver.title)

# 网页的源代码
print(driver.page_source)

# 最大化
driver.maximize_window()

# 最小化
driver.minimize_window()

# 设置窗口的大小
driver.set_window_size(1000, 800)

# 刷新
driver.refresh()

# 前进
driver.forward()
driver.get('https://www.cnblogs.com/qiaoyeye/p/5284232.html')

# 后退
driver.back()

elm = driver.find_element_by_id('kw')
print(elm.text)
# 退出
driver.quit()