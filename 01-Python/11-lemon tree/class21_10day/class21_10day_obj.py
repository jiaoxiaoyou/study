# @Author : jiaojie
# @CreateDate : 2020/5/17 12:57
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
实例属性初始化方法：
__init__:

"""

class Car:
    leg = '有四条腿'
    tail = '有长尾巴'

    def __init__(self):
        # 初始化方法，在创建对象的时候会自动调用
        print('__init__调用了')

# Kt猫
kt = Car()