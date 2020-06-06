# @Author : jiaojie
# @CreateDate : 2020/5/16 14:09
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
python打卡第九天
1、有1 2 3 4这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？
2、对第7天的石头剪刀布游戏升级，游戏一轮出拳后进入下一轮，
当选择结束游戏后，打印本次游戏的胜率：胜利的次数/(玩的总次数-平局数)
提示：（想办法记录一下计算胜率需要的数据，然后就可以算出结果）
"""

print("---------------------第1题---------------------")

new_list = []
redup_list = []

for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            new_list = [x, y, z]
            redup_set = set(new_list)
            if len(redup_set) == 3:
                print(new_list)
                redup_list.append(new_list)

print("1 2 3 4这四个数字中能组成 {} 个互不相同且无重复数字的3位数".format(len(redup_list)))


print("---------------------第2题---------------------")
import random

def game():
    # 玩的总数
    total_count = 0
    # 胜利的总数
    win_count = 0
    # 平局
    draw_count = 0

    print("石头剪刀布开始")
    print("根据提示出拳：")
    li = ["石头", "剪刀", "布"]

    while True:
        print("石头（1）／剪刀（2）／布（3）/退出（4）")
        user = int(input("请输入你的选择："))
        computer = random.randint(1, 3)

        if user == 4:
            print("退出游戏 ")
            break
        elif 1 <= user <= 3:
            total_count += 1
            if user == computer:
                print('你：{0}，电脑：{1}，平局'.format(li[user - 1], li[computer - 1]))
                draw_count += 1
            elif computer - user == 1 or computer - user == -2:
                print('你：{0}，电脑：{1}，你赢了'.format(li[user - 1], li[computer - 1]))
                win_count += 1
            else:
                print('你：{0}，电脑：{1}，你输了'.format(li[user - 1], li[computer - 1]))
        else:
            print("你输入的有误")

    # 胜利的次数/(玩的总次数-平局数)
    win_rate = "{:.2f}%".format(win_count / (total_count - draw_count) * 100)
    # win_rate = win_count /(total_count - draw_count) * 100
    print("游戏次数为：{}，平局次数：{}，胜利次数为：{}\n本次游戏您的胜率为：{}".format(total_count, draw_count, win_count, win_rate))

game()