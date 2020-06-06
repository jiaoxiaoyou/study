"""
@Author : jiaojie
@Time : 2020/4/5 21:15
@Desc : 
"""

"""
1. 将给定字符串的PHP替换为Python
best_language = "PHP is the best programming language in the world!"

2. 编写代码，提示用户输入1-7七个数字，分别代表周一到周日
如果输入的数据是6或7则为周末，打印输出"今天是周几"

3. 现在有一个列表li2 = [1, 2, 3, 4, 5]
第一步：请通过相关的操作改为li2 = [0, 1, 2, 3, 66, 4, 5, 11, 22, 33]
第二步：对li2进行排序处理
第三步：请写出删除列表中元素的方法，并说明每个方法的作用

4. 切片
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]请通过切片得出结果[3, 6, 9]
    s = 'python java php', 通过切片获取'java'
    tu = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']通过切片获取['g', 'b']
    
5. 写出课上讲的列表的所有方法，并说明每个方法有什么用
"""
# print("=======================第一题========================")
# best_language = "PHP is the best programming language in the world!"
# print(best_language.replace('PHP', 'Python'))
#
# print("=======================第二题========================")
# week = int(input("请输入1~7中的某个数字："))
# if week == 1:
#     print("今天是周一")
# elif week == 2:
#     print("今天是周二")
# elif week == 3:
#     print("今天是周三")
# elif week == 4:
#     print("今天是周四")
# elif week == 5:
#     print("今天是周五")
# elif week == 6:
#     print("今天是周六")
# elif week == 7:
#     print("今天是周日")
#
# weeks = ['周一', '周二', '周三', '周四', '周五', '周末', '周末']
# num= int(input("请输入1~7："))
# print('今天是：{}'.format(weeks[num-1]))

print("=======================第三题========================")
# li2 = [1, 2, 3, 4, 5]
# li2.insert(0, 0)
# print(li2)
# li2.insert(4, 66)
# print(li2)
# # li2.append(11)
# # print(li2)
# # li2.append(22)
# # print(li2)
# # li2.append(33)
# li2.extend([11, 22, 33])
# print(li2)
#
# li2.sort()
# print('排序后：',li2)

# li2.pop()
# del li2[2]
# remove
# clear

print("=======================第四题========================")
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[2::3])
s = 'python java php'
x = s.split()
print(x[1])
tu = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(tu[-2:-8:-5])

tu1 = tu[1:7:5]
tu1.reverse()
print(tu1)


print("=======================第五题========================")

# print("移除最后一个元素：pop()")
# print("分片:split()")
# print("插入：insert()")
# print("append()")
# print("删除函数：")
# print("extend()")
# print("remove()")
# print("clear()")
