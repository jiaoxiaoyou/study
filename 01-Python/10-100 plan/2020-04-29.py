"""
@Author : JJ
@Time : 2020/4/29 14:56
@Desc : 
"""

"""

1、剪刀石头布游戏：
游戏开始，输入数字表示选项：退出【0】石头【1】剪刀【2】布【3】
游戏结束，计算游戏者的胜率
提示：人机游戏，机器可随机出拳

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

2、封装一个计算器函数
计算器功能：仅支持加减乘除运算

"""

print("---------------------第一题---------------------")
import random
print('---石头剪刀布游戏开始---')
print('请按下面提示出拳：')
li = ['石头', '剪刀', '布']
while True:
    print('退出【0】石头【1】剪刀【2】布【3】')
    user_input = int(input('请输入你的选项：'))
    computer_input = random.randint(1,3)

    if 1 <= user_input <= 3:
        if user_input == computer_input:
            print('你：{0}，电脑：{1}，平局'.format(li[user_input-1], li[computer_input-1]))
        elif computer_input-user_input == 1 or computer_input-user_input == -2:
            print('你：{0}，电脑：{1}，你赢了'.format(li[user_input-1], li[computer_input-1]))
        else:
            print('你：{0}，电脑：{1}，你输了'.format(li[user_input-1], li[computer_input-1]))
    elif user_input == 0:
        print('退出游戏')
    else:
        print('你出的拳有误，请按规则出拳')


print("---------------------第二题---------------------")
import re

def add(a, b):
    """
    计算两个数相加
    :param a:
    :param b:
    :return:
    """
    return a + b


def sub(a, b):
    """
    计算两个数相减
    :param a:
    :param b:
    :return:
    """
    return a - b


def mul(a, b):
    """
    计算两个数相乘
    :param a:
    :param b:
    :return:
    """
    return a * b


def div(a, b):
    """
    计算两个数相除
    :param a:
    :param b:
    :return:
    """
    return a / b


def counter():
    """
    计算器：支持加减乘除运算，浮点数小数点后不限制位数，支持负数运算
    :return result:运算结果
    """
    str_num = input("请输入您要计算的两个数字（以空格隔开）：")
    is_float = re.match(r'^(-?\d+)(\.\d+)? (-?\d+)(\.\d+)?$', str_num)

    if is_float:
        a = float(str_num.split(" ")[0])
        b = float(str_num.split(" ")[1])

        rule = input("请选择计算方式（加【1】减【2】乘【3】除【4】）：")
        if re.match(r'^[1-4]{1}$', rule):
            rule = int(rule)
            if rule == 1:
                result = add(a, b)
            elif rule == 2:
                result = sub(a, b)
            elif rule == 3:
                result = mul(a, b)
            elif rule == 4:
                result = div(a, b)
            print("计算结果为：{}".format(result))
            return result
        else:
            print("您输入的计算方式不合法，无法计算！")
            counter()
    else:
        print("您输入的数字不合法，无法计算！")
        counter()
