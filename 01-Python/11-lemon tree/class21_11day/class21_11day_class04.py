# @Author : jiaojie
# @CreateDate : 2020/5/17 14:21
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
重写
子类的对象调用和父类同名的方法时，优先调用自身有的方法和属性

"""

class BasePhone(object):
    pass

class NewPhone1(BasePhone):
    def func(self):
        print('NewPhone1')

class NewPhone2(NewPhone1):
    def func(self):
        # 方法1   父类名.方法名(self)
        # NewPhone1.func(self)

        # 方法2   super().方法名
        super().func()
        print('NewPhone2')

# 在子类调用父类同名的方法



v2 = NewPhone2()
v2.func()



