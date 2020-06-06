"""
@Author : jiaojie
@Time : 2020/4/5 22:52
@Desc : 
"""

"""
元组  列表   字符串

统称为序列类型：有下标索引，可以切片


序列类型通用操作：
1. 索引取值，可以切片
2. len()获取序列的长度
3. 序列类型之间的相互转换
str()
list()
tuple()

"""

str1 = 'abcdef'
li1 = [11, 22, 33, 44, 55]
tu1 = (11, 22, 33)

print(len(str1))
print(len(li1))
print(len(tu1))

# list() : 把字符串转换成列表
# print(list(str1))
# print(list(tu1))

# tuple()
# print(tuple(str1))
# print(tuple(li1))

# str()
print(str(li1))
print(type(str(li1)))