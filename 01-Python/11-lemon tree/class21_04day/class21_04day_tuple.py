"""
@Author : jiaojie
@Time : 2020/4/5 22:40
@Desc : 
"""

"""
元组
元组的定义：用（）表示
元组是不可变类型的数据，定义了之后不能对里面的元素进行修改

元组的方法：
count():用来计算指定元素的个数
index():查找指定元素的下标

元组可以下标取值和切片

注意点：

1.空元组定义：()
2.元组中只要一个元素：(xxx,)或者(xxx),

元组内部元素修改：特殊情况

元组内部有可变类型的元素的时候，内部的可变类型是可以修改


"""

tu = ()

print(type(tu))

tu1 = (11, 22, 33, 'a', 'bb')

print(tu1[2])
print(tu1[0:3])

tu2 = (111,)
print(tu2)


tu3 = ([111, 222, 333], 'a', 'b')
print(tu3)
print(id(tu3))
print(id(tu3[0]))
print(id(tu3[1]))
print(id(tu3[2]))

tu3[0].append(999)
print(tu3)

print(id(tu3))
print(id(tu3[0]))
print(id(tu3[1]))
print(id(tu3[2]))