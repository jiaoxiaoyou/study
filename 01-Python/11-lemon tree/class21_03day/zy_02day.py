"""
Author : jiaojie
Time : 
Email : 15202938614@163.com
"""

import random

# print("-----------第一题---------------")
# num = input("请输入一个数字：")
#
# num = int(num)
#
# if (num % 2 == 0):
#     print("True")
# else:
#     print("False")
#
# print("-----------第二题---------------")
# price = float(input("请输入橘子的价格："))
# print("支付金额为：",price * random.randint(5,10))


print("-----------第三题---------------")
li = ['hello', 'python','!']
print(li[0],li[1],'18',li[2])
str1 = " "
print(str1.join(li))



print("-----------第四题---------------")
str1 = "python hello aaa 123123aabb"

count_a = str1.count('a')
print(count_a)
print("123的下标起始位置：",str1.find('123'))

print("o a的结果：",'o a' in str1)
print("he的结果：",'he' in str1)
print("ab的结果：",'ab' in str1)