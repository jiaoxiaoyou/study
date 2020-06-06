"""
@Author : JJ
@Time : 2020/4/24 23:01
@Desc : 
"""

"""
1. 列表和元组的区别
2. 访问列表的最后一个元素（该问题源于range函数遍历列表长度时有时候数据会少有时候越界的迷茫）
"""

print("---------------------第一题---------------------")
# 列表和元祖的区别
list1 = [11, 22, 33, 44, 55]

print("列表：是可变的,内容和长度都可变")
list1[3] = 66
print(list1)
list1.append(77)
print(list1)
"""
打印结果：
列表：是可变的,内容和长度都可变
[11, 22, 33, 66, 55]
[11, 22, 33, 66, 55, 77]
"""
print('********************')

tuple1 = ('aa', 'bb', 'cc', 'dd', 'ee')
tuple2 = (11, 22, 33, 44)
tuple3 = ([111, 222, 333], 'a', 'b')

print("元组：是不可变的")
#tuple1[1] = 22
#print('tuple1')

"""
修改元组内容会报错
Traceback (most recent call last):
  File "C:/2020-04-24.py", line 31, in <module>
    tuple1[1] = 22
TypeError: 'tuple' object does not support item assignment
"""

tuple4 = tuple1 + tuple2
print(tuple4)
# 给元组内的列表新增元素
tuple3[0].append(999)
print(tuple3)


print("---------------------第二题---------------------")
# 访问列表的最后一个元素
list2 = [99, 88, 77, 66]

length = len(list2)-1
print('方法一：',list2[length])

print('方法二：',list2[-1:][0])

list2.reverse()
print('方法三：',list2[0])
