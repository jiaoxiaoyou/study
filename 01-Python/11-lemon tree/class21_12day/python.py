# @Author : jiaojie
# @CreateDate : 2020/5/26 20:50
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
python 基础语法阶段复习

函数


"""


# *args 只能接受未知传参
def func(*args):
    print("args参数：",args)


#func(1, 2, 3, 4, 5)


# **kwargs 只接受关键传参
def func2(a, **kwargs):
    print("kwargs参数：",kwargs)


#func2(a=11, b=22)


def func3(a, *args, **kwargs):
    print(a)
    print("args参数：",args)
    print("kwargs参数：",kwargs)


tu = (11, 22, 33, 44)
func3(tu)
# 一个*是对元组拆解
func3(*tu)
# 两个**是对字典拆解

