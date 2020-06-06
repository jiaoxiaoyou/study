# @Author : 强小林
# @CreateDate : 2020/5/15 17:05
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription : 


import re

"""
python打卡第八天
1、输出99乘法表，结果如下：（提示嵌套for循环，格式化输出）
2、通过函数实现一个计算器，运行程序分别提示用户输入数字1、数字2，
然后再提示用户选择 ：加【1】 减【2】 乘【3】 除【4】，
每个方法使用一个函数来实现，选择后调用对应的函数，然后返回结果。
"""


# 第1题

def print_mul(positive=True):
    """
    输出九九乘法表，可以选择正序还是反序输出
    :param positive: 输出顺序，默认为正序
    :return: 无需返回值
    """
    if positive:
        for i in range(1, 10):
            for j in range(1, i + 1):
                print("{:^3d}*{:^3d}={:^4d}".format(j, i, i * j), end="")
            print()
    else:
        for i in range(9, 0, -1):
            for j in range(1, i + 1):
                print("{:^3d}*{:^3d}={:^4d}".format(j, i, i * j), end="")
            print()


# 第2题
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
