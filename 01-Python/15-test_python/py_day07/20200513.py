# @Author : jiaojie
# @CreateDate : 2020/5/13 20:38
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
python打卡第七天
1、利用random函数生成随机整数，从1-9取出来。然后输入一个数字，来猜：
如果大于，则打印大于随机数；小了，则打印小于随机数；如果相等，则打印等于随机数。
2、使用循环和条件语句完成剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
电脑随机出拳比较胜负，显示用户胜、负还是平局。运行如下图所示：

"""

print("---------------------第1题---------------------")
import random

user_input = int(input("请输入一个数字："))
computer_input = random.randint(1,9)

if user_input > computer_input:
    print("{0}大于随机数{1}".format(user_input, computer_input))
elif user_input < computer_input:
    print("{0}小于随机数{1}".format(user_input, computer_input))
else:
    print("{0}等于随机数{1}".format(user_input, computer_input))


print("---------------------第2题---------------------")

"""
石头（1）／剪刀（2）／布（3）/退出（4）
电脑胜利
user    computer
1           3       2
2           1       -1
3           2       -1

用户胜利
user    computer
1           2       1
2           3       1
3           1       -2

"""
print("石头剪刀布开始")
print("根据提示出拳：")
li = ["石头", "剪刀", "布"]

while True:
    print("石头（1）／剪刀（2）／布（3）/退出（4）")
    user = int(input("请输入你的选择："))
    computer = random.randint(1,3)

    if user == 4:
        print("退出游戏 ")
        break
    elif 1 <= user <= 3:
        if user == computer:
            print('你：{0}，电脑：{1}，平局'.format(li[user-1], li[computer-1]))
        elif computer-user == 1 or computer-user == -2:
            print('你：{0}，电脑：{1}，你赢了'.format(li[user-1], li[computer-1]))
        else:
            print('你：{0}，电脑：{1}，你输了'.format(li[user-1], li[computer-1]))
    else:
        print("你输入的有误")


import re
def game_jhj():
    """
    剪刀石头布游戏：计算游戏胜率；没有考虑容错机制，如被除数为0的情况
    :return win_rate:返回值为胜率
    """
    print("------剪刀石头布游戏开始------\n请按下面提示出拳：\n石头【1】剪刀【2】布【3】退出【4】")

    rule = {1: "石头", 2: "剪刀", 3: "布", 4: "退"}

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