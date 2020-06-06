"""
@Author : jiaojie
@Time : 2020/4/6 17:43
@Desc : 
"""
from random import randint

"""
1. 一家商场的在降价促销，如果购买金额50~100（包含50元和100元）之间，会给10%折扣，
如果购买金额大于100元会给20%折扣，编写一程序，询问购买价格，再显示出折扣（10%或20%）和最终价格。

2.一个5位数，判断它是不是回文数，例如12321是回文数，个位和万位相同，十位与千位相同，根据判断打印出相关信息

3. 利用random 函数生成随机函数，从1~9取出来，然后输入一个数字，来猜，如果大于，则打印随机数。小了，则打印小于随机数。如果等于，则打印等于随机数

4. 使用循环和条件语句完成剪刀石头布游戏，提示用户输入要出的拳：石头（1）/剪刀（2）/布（3）/退出（4）
电脑随机出拳比较胜负，显示用户胜，负还是平局。运行如下图所示

用户胜利
user    computer
1           2       1
2           3       1
3           1       -2

电脑胜利
user    computer
1           3       2
2           1       -1
3           2       -1

"""

'========================第一题=========================='
# money = int(input('请输入购买的金额：'))
# if money > 0 and money < 50:
#     print('没有折扣')
# elif money >= 50 or money <= 100:
#     print('折扣：10%，最终价格：{}'.format(money*0.9))
# elif money >100:
#     print('折扣：20%，最终价格：{}'.format(money*0.8))
# else:
#     print('输入的金额不正确')
#
#
# '========================第二题=========================='
# number = int(input('请输入一个5位数字：'))
# if number[4] == number[0] and number[3] == number[1]:
#     print('此数字是回文数：',number)
# else:
#     print('不是回文数')
#
#
# '========================第三题=========================='
# num = int(input('请输入一个数字：'))
# randomNum = randint(1,9)
# if num > randomNum:
#     print('大于随机数')
# elif num < randomNum:
#     print('小于随机数')
# else:
#     print('等于随机数')

'========================第四题=========================='
import random
print('---石头剪刀布游戏开始---')
print('请按下面提示出拳：')
# 创建一个列表来存储 石头 剪刀 布
li = ['石头', '剪刀', '布']
while True:
    print('石头【1】 剪刀【2】 布【3】 结束游戏【4】')
    # 用户输入数字
    user_num = int(input('请输入你的选项：'))
    # 电脑随机生成数字
    computer_num = random.randint(1,3)

    if 1 <= user_num <= 3:
        if user_num == computer_num:
            print("用户出：{0}，电脑出：{1}，平局".format(li[user_num-1], li[computer_num-1]))
        elif computer_num-user_num == 1 or computer_num-user_num == -2:
            print("用户出：{0}，电脑出：{1}，你赢了".format(li[user_num - 1], li[computer_num - 1]))
        else:
            print("用户出：{0}，电脑出：{1}，你输了".format(li[user_num - 1], li[computer_num - 1]))
    elif user_num == 4 :
        print("游戏结束")
        break
    else:
        print('您出拳有误，请按规则出拳')