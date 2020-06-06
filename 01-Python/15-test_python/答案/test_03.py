# @Author : 强小林
# @CreateDate : 2020/5/8 14:07
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

import random
import re

print("=" * 10, "python打卡第三天", "=" * 10)

"""
python打卡第三天
1、卖橘子的计算器：提示用户输入橘子的价格，然后随机生成购买的斤数（5到10斤之间），最后计算出应该支付的金额！
2、现在有字符串：str1 = 'python hello aaa 123123aabb'
（1）请计算字符串中有多少个'a'
（2）请找出字符串中'123'的下标起始位置
（3）请分别判断 'o a' 'he' 'ab' 'nh' 是否是该字符串中的成员？

说明：
1、给出的参考答案有些超纲，主要看核心实现就行，有兴趣的支持无限扩展
2、想说明的问题：写出优秀的代码是一项持续学习的过程，可以从基本实现、容错机制、代码效率、代码简洁、多种实现方式等等多方面角度考虑
"""

print("=" * 10, "第一题", "=" * 10)

# 思考：
# 1、橘子的单价，最多是两位小数
# 2、橘子的斤数，不一定是整数，一般生活常识是保留到小数点后一位吧
# 3、橘子的总价，最多是两位小数

str_price = input("请输入橘子的单价：")
is_float = re.match(r'^\d+(\.\d{1,2})?$', str_price)  # 匹配到小数点后两位，可以输入类似：1、0.9、0.99

if is_float:
    num = round((random.random() + 1) * 5, 1)  # 斤数为5-10之间保留到小数点后一位的小数
    money = round((num * float(str_price)), 2)  # 价格=斤数*单价，但只能保留到小数点后2位
    print("您购买了{0}斤橘子，共需支付{1}元".format(num, money))
else:
    print("您输入的橘子单价不符合生活常识要求，请重新输入")

print("=" * 10, "第二题", "=" * 10)

str1 = 'python hello aaa 123123aabb'

# 1、字符串中有多少个'a'

print("字符串str1中有{}个a".format(str1.count('a')))

# 2、字符串中'123'的下标起始位置
# 思考：题目要求输出'123'的下标位置，不能直接用find方法，只能返回第1个子串的起始位置下标，即17，所以考虑使用正则寻找
count_123 = str1.count('123')
# count_123 = str1.index('123')  # find和index的区别：find找不到返回-1，index找不到抛异常
str1_1 = re.finditer('123', str1)

print("在str1中共找到{}处子串'123'，它们的下标起始位置分别是：".format(count_123))
for match in str1_1:
    print(match.start())

# 3、分别判断'o a'、'he'、'ab' 是否是该字符串中的成员？
question = ['o a', 'he', 'ab', 'nh']

# 方法1：用成员运算符
for item in question:
    if item in str1:
        print("{}是str1字符串的成员".format(item))
    else:
        print("{}不是str1字符串的成员".format(item))

# 方法2：用find函数
for item in question:
    if str1.find(item) == -1:
        print("{}不是str1字符串的成员".format(item))
    else:
        print("{}是str1字符串的成员".format(item))

