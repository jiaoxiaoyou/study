# @Author : jiaojie
# @CreateDate : 2020/5/19 21:15
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
python打卡第11天
1、定义一个测试用例类，初始化四个实例属性：url地址、请求参数、预期结果、实际结果，并创建一个实例对象
2、定义一个手机的基类，有打电话、发短信两个功能，有手机名一个属性；再分别定义两个类，苹果手机和华为手机，
这两个手机都有基类的所有功能和属性，而且苹果手机有语言助手sir功能，华为手机有拍照功能

"""

class TestCase(object):
    def __init__(self, url, para, expected_res, actual_res):
        self.url = url
        self.para = para
        self.expected_res = expected_res
        self.actual_res = actual_res

# 实例化类
test_01 = TestCase("https://baike.baidu.com/", "post", "预期结果：正确进入网页", "实际结果：正确进入网页")

class Phone(object):
    def __init__(self, name):
        self.name = name

    def call(self):
        print("打电话")

    def send(self):
        print("发短信")

class ApplePhone(Phone):
    def sir(self):
        print("hi sir")

class  HuaweiPhone(Phone):
    def takePic(self):
        print('take a picture')

apple = ApplePhone("苹果手机")
huawei = HuaweiPhone("华为手机")

apple.call()
apple.send()
apple.sir()

huawei.call()
huawei.send()
huawei.takePic()