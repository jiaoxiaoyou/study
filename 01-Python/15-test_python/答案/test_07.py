# @Author : 强小林
# @CreateDate : 2020/5/13 17:54
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

# 第1题：可优化项：按需输入--利用正则 re.match(r'^\d$', num_me)

# 方法1：猜一次
import random

print("----------第一题：方法1----------")

num = random.randint(1, 9)
num_me = int(input("请输入一个数字（猜一猜）："))

if num > num_me:
    print("对不起，您猜小了")
elif num < num_me:
    print("对不起，您猜大了")
else:
    print("恭喜您猜对了")

# 方法2：循环猜，直至猜中
print("----------第一题：方法2----------")

num = random.randint(1, 9)

while True:
    num_me = int(input("请输入一个数字（猜一猜）："))
    if num > num_me:
        print("对不起，您猜小了")
    elif num < num_me:
        print("对不起，您猜大了")
    else:
        print("恭喜您猜对了")
        break

# 第2题：可优化项：按需输入--利用正则 re.match(r'^[1-4]{1}$', num_me)
# 规则梳理：石头>剪刀、剪刀>布、布>石头
# 规则梳理：1>2、2>3、3>1

print("----------第二题----------")
print("------剪刀石头布游戏开始------\n请按下面提示出拳：\n石头【1】剪刀【2】布【3】退出【4】")

rule = {1: "石头", 2: "剪刀", 3: "布", 4: "退出"}

while True:
    robot = random.randint(1, 3)
    user = int(input("请输入你的选项："))
    if (robot == 1 and user == 3) or (robot == 3 and user == 2) or (robot == 2 and user == 1):
        print("您的出拳为：{}，电脑出拳为：{}，您胜利了".format(rule[user], rule[robot]))
    elif robot == user:
        print("您的出拳为：{}，电脑出拳为：{}，平局".format(rule[user], rule[robot]))
    elif user == 4:
        print("游戏结束")
        break
    else:
        print("您的出拳为：{}，电脑出拳为：{}，您输了".format(rule[user], rule[robot]))
