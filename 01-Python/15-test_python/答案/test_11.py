# @Author : 强小林
# @CreateDate : 2020/5/20 15:16
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription : 

"""
python打卡第十一天
1、定义一个测试用例类，初始化四个实例属性：url地址、请求参数、预期结果、实际结果，并创建一个实例对象
2、定义一个手机的基类，有打电话、发短信两个功能，有手机名一个属性；再分别定义两个类，苹果手机和华为手机，这两个手机都有基类的所有功能和属性，而且苹果手机有语言助手sir功能，华为手机有拍照功能

"""

print("-------------------第1题-------------------")


class TestCase(object):

    def __init__(self, url, request, exc_res, act_res):
        self.url = url  # url地址
        self.request = request  # 请求参数
        self.exc_res = exc_res  # 预期结果
        self.act_res = act_res  # 实际结果


test_01 = TestCase("https://baike.baidu.com/", "post", "预期结果：正确进入网页", "实际结果：正确进入网页")

print("-------------------第2题-------------------")


# 手机基类
class Phone_V1(object):
    def __init__(self, name):
        self.name = name

    def call_phone(self):
        print("【{}】原始手机：有事没事多给家里打打电话".format(self.name))

    def send_message(self):
        print("【{}】原始手机：不方便打电话可以发发短信问候".format(self.name))


# 华为手机
class Phone_Huawei(Phone_V1):
    def camera(self):
        print("【{}】拍照手机：照亮你的美".format(self.name))


# 苹果手机
class Phone_Iphone(Phone_V1):
    def sir(self):
        print("【{}】sir：主人，您才是世界上最美的女人".format(self.name))


huawei = Phone_Huawei("华为手机")  # 必须同V1指定名字，否则会报错
iphone = Phone_Iphone("苹果手机")  # 必须同V1指定名字，否则会报错

# 华为手机
huawei.call_phone()  # 继承V1
huawei.send_message()  # 继承V1
huawei.camera()  # 自己特有的功能

# 苹果手机
iphone.call_phone()  # 继承V1
iphone.send_message()  # 继承V1
iphone.sir()  # 自己特有的功能
