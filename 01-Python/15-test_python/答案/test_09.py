# @Author : 强小林
# @CreateDate : 2020/5/15 17:07
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription : 


import re
import random

"""
python打卡第九天
1、有1 2 3 4这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？
2、对第7天的石头剪刀布游戏升级，游戏一轮出拳后进入下一轮，
当选择结束游戏后，打印本次游戏的胜率：胜利的次数/(玩的总次数-平局数)
提示：（想办法记录一下计算胜率需要的数据，然后就可以算出结果）
"""


# 第1题

def three_digits(end=5, start=1):
    """
    获取指定区间内数字组成的互不相同且无重复的三位数
    :param end: 指定区间的结束范围，不包括此值（未处理异常情况，如0或大于10的数字）
    :param start: 指定区间的起始范围，（未处理异常情况，如0或大于9的数字）
    :return list_num: 返回所有组成的三位数列表
    """
    res = []
    for hundred in range(start, end):
        for decade in range(start, end):
            for unit in range(start, end):
                if hundred != decade and hundred != unit and decade != unit:
                    # num = int(str(hundred) + str(decade) + str(unit))
                    num = hundred * 100 + decade * 10 + unit
                    res.append(num)
    print("由[{0}, {1})内整数组成的互不相同且无重复的三位数的个数是：{2}个，它们分别是：\n{3}".format(start, end, len(res), res))
    return res


# 第2题
def game_jhj():
    """
    剪刀石头布游戏：计算游戏胜率；没有考虑容错机制，如被除数为0的情况
    :return win_rate:返回值为胜率
    """
    print("------剪刀石头布游戏开始------\n请按下面提示出拳：\n石头【1】剪刀【2】布【3】退出【4】")

    rule = {1: "石头", 2: "剪刀", 3: "布", 4: "退出"}

    num_win = 0  # 赢的次数
    num_draw = 0  # 平局的次数
    play_sum = 0  # 游戏次数

    while True:
        robot = random.randint(1, 3)
        user = input("请输入你的选项：")
        if re.match(r'^[1-4]{1}$', user):
            user = int(user)
            if user == 4:
                print("游戏结束")
                break
            else:
                play_sum += 1
                if (robot == 1 and user == 3) or (robot == 3 and user == 2) or (robot == 2 and user == 1):
                    num_win += 1
                    print("您的出拳为：{}，电脑出拳为：{}，您胜利了".format(rule[user], rule[robot]))
                elif robot == user:
                    num_draw += 1
                    print("您的出拳为：{}，电脑出拳为：{}，平局".format(rule[user], rule[robot]))
                else:
                    print("您的出拳为：{}，电脑出拳为：{}，您输了".format(rule[user], rule[robot]))
        else:
            print("您输入的选项不合法，请重新输入")

    win_rate = "{:.2%}".format(num_win / (play_sum - num_draw))
    print("游戏次数为：{}，平局次数：{}，胜利次数为：{}\n本次游戏您的胜率为：{}".format(play_sum, num_draw, num_win, win_rate))
    return win_rate
