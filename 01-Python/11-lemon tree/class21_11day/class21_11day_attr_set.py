# @Author : jiaojie
# @CreateDate : 2020/5/17 14:35
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
魔术方法：双下划线开头双下划线结尾的方法叫魔术方法

__init__：创建对象的时候，自动调用

__setattr__：

__getattr__：

__delattr__：

__new__：

魔术变量：
__main__：当前启动文件
__file__：当前文件的绝对路径
__name__：__main__


# 内置函数
setattr
getattr
delattr

"""


class Hero(object):
    attr1 = 11

h = Hero()
h.attr2 = 22

# 设置属性
setattr(h, 'name', 'Musen')

# 获取属性
res = getattr(h, 'name')
print(res)

# 删除属性
#delattr(h, 'attr2')
print(h.attr2)


print(h.name)

print(__name__)
print(__file__)
