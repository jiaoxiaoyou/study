# @Author : jiaojie
# @CreateDate : 2020/5/17 13:57
# @Description : 第18节 面向对象编程--类的继承
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
类属性：
    直接定义在类中的变量
    公有属性
    私有属性：单下划线_attr1或者双下划线__attr2 只能在类里面使用

类方法：
    通过@classmethod这个装饰器装饰的方法叫做类方法
    类方法的第一个参数为cls
    cls的是类本身

实例属性：

实例方法：

静态方法：
    @staticmethod 装饰器装饰的方法

"""

class Hero:
    # 公有属性
    attr = 100
    attr2 = 200

    # 私有属性
    _attr1 = 'aa'
    __attr2 = 'bb'

    # 类方法
    @classmethod
    def cls_func(cls, attr3):
        print('这是个类方法中的cla:',cls)
        print(cls._attr1)
        cls.attr3 = attr3

    # 静态方法：静态方法中不会使用到类属性和实例属性
    @staticmethod
    def sta_func():
        print('----静态方法----')


h = Hero()

Hero.cls_func('123')
Hero.sta_func()
h.sta_func()

Hero.cls_func()