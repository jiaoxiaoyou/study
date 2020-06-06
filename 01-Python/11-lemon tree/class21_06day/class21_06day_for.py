"""
@Author : jiaojie
@Time : 2020/4/7 23:09
@Desc : 
"""

"""
for循环：

for x in xxx:
    pass

"""

li = [11, 22, 33, 44, 55]

for i in li:
    print(i)

# 内置函数：range()
# range(x)--->返回一个可迭代对象，可迭代对象中有0，1，2，3，x-1这么些内容
# 可迭代对象：能够被for循环变量的就叫做可迭代对象
# range ：可以传一个参数，两个参数，三个参数

for i in range(1,10,3):
    print(i)

# 遍历字典
dict1 = {'a':66, 'b':77, 'c':88}
for i in dict1:
    print(i)

for i in dict1.values():
    print(i)

for i in dict1:
    print(dict1.get(i))

for i in dict1.items():
    print(i)

# for 循环中的break
# break :中止循环
# continue:中止当前这一轮循环，开启下一轮循环
# else:在for结束的情况下会执行，如果是break结束循环则不执行
for i in range(10):
    if i==5:
        #break
        continue
    print(i)
else:
    print("-------else-------")

# for 循环的嵌套使用

for i in range(5):
    print((i+1)*"* ")

print('-------------------------------')

for i in range(5):
    for j in range(i+1):
        print("* ",end='')
    print('')