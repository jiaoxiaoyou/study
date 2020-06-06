# @Author : jiaojie
# @CreateDate : 2020/5/17 0:45
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
面向对象：
万物皆对象：

类：
关键字：class
语法：class 类名：

类名的规范：大写字母开头（如果由多个单词组成，那么每一个单词的第一个字母大写）

class 类名(object):
类中可以描述这一类事物的特征和行为
属性：
    类属性：每一个实例对象都有，而且值是一样的，指定定义在类里面的变量
    实例对象属性：通过实例对象，属性名进行赋值的属性叫实例属性，实例属性是该实例对象独有的，其它的对象获取不到
    类属性和实例属性的访问：
        类属性可以通过实例对象去获取
        类属性也可以通过类直接去访问

        实例属性：只能通过实例对象访问
方法：定义在类中的函数
    实例方法
    类方法



对象：
"""

class Dog(object):
    attr1 = '四条腿'
    attr2 = '尾巴'
    # name = '小黄黄'
    # gender = '公'

    def skill1(self):
        print('看家')

d1 = Dog()
d2 = Dog()

# 通过实例对象来调用实例方法
d1.skill1()

# 通过类来调用实例方法:需要传入一个实例对象
Dog.skill1(d1)


print(d1.attr1)
print(d1.attr2)

# 实例属性
d1.name = '小黑黑'
print(d1.name)

print('-----------------d2-----------------')
print(d2.attr1)
print(d2.attr2)
d2.name = '小黄花'
print(d2.name)
d2.skill1()
