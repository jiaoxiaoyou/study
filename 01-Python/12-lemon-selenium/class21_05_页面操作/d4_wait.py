# @Author : jiaojie
# @CreateDate : 2020/5/18 21:27
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
1. 强制等待
time.sleep()

2. 隐式等待
智能等待，每初始化一次浏览器，只需要设置一次
implicitly_wait()

3. 显示等待
WebDriverWait(driver, 20).until(
EC.visibility_element_located(By.XPATH, '//*[contains(text(),"lemon.ke.qq.com/")]')
)

"""
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EC.visibility_of_element_located()
EC.presence_of_element_located()
EC.element_to_be_clickable()

def wait_element_id(driver,id_value,timeout,frequency=0.1):
    time_start = 0
    while time_start < timeout:
        try:
            e = driver.find_element_by_id(id_value)
            return e
        except:
            time.sleep(frequency)
            time_start += frequency