"""
@Author : jiaojie
@Time : 2020/4/19 18:12
@Desc : 
"""

"""
函数：

自己定义函数
关键字def:定义函数
函数的作用：用来封装功能,提高代码的复用性

关键字return：用来给函数定义返回值，只能用在函数体当中
一个函数里面只要执行到return，那么这个函数就运行结束

return = 0, 返回None
return = 1, 返回object
return > 1, 返回tuple


#内置函数
type()
id()
range()


"""
# 函数的定义
def add():
    a = 100
    b = 200
    c = a + b
    d = a - b
    return c,d
    # print(a + b)

# 函数的调用
# 拆包
aa, bb = add()
print(add())
print(aa, bb)

print('--------------------------')


li = [11,22,33,44]
# res = li.remove(11)
# print(res)

res = li.pop(0)
print(res)





res = type(7)
print(res)