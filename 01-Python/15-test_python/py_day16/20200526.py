# @Author : jiaojie
# @CreateDate : 2020/5/26 11:35
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
python打卡第十六天
1、实现文字版游戏：坦克大战
步骤一：定义TANK类（必做）
（1）实现一个BaseTank类（所有Tank的父类）
    BaseTank拥有live属性（这个属性代表Tank是否存活 :  1代表活的，0代表死）
    BaseTank拥有position属性（这个属性代表Tank的位置，位置随机生成，一共有（1,10）10个位置）
    BeseTank拥有HP属性（代表血量，默认为10）
    BeseTank拥有attck_position属性（代表攻击位置，位置随机生成，一共有（1,10）10个位置）
（2）实现一个玩家坦克类（MyTank类），继承于BaseTank，该类拥有两个方法。
    move方法：(移动tank位置)调用该方法时，提示玩家输入移动的目标位置，输入完之后，将坦克移动到输入的位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）
    Bullet_launch方法：发射子弹，提示玩家输入攻击的目标位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）
（3）实现一个电脑坦克类（PCTank类），继承于BaseTank，该类拥有两个方法。
    move方法：(移动tank位置) 调用该方法时，随机移动位置（1,10）
    Bullet_launch方法：发射子弹，攻击目标位置随机生成（1,10）

步骤二：游戏规则逻辑完善（扩展题做，不要求提交）
（1）启动游戏后，创建一个玩家坦克，一个电脑tank
（2）游戏环节（循环，直到有tank死亡才退出循环）
    玩家发生子弹，然后电脑坦克发射子弹，
    玩家判断有没有被电脑击中，电脑判断有没有被玩家击中。
    判断双方坦克是否存活，如果有tank死亡，则宣布存活的一方胜利。都存活则继续游戏。
    玩家移动、电脑移动
"""
import random


class BaseTank(object):
    def __init__(self):
        self.live = 1
        self.position = random.randint(1, 10)
        self.HP = 10
        self.attack_position = random.randint(1, 10)


class MyTank(BaseTank):
    def move(self):
        while True:
            try:
                tank_position = int(input("请输入移动的目标位置："))
            except ValueError:
                print("您输入的是无效数据，请重新输入")
            else:
                if 1 < tank_position < 10:
                    self.position = tank_position
                    break
                else:
                    print("您输入的是无效数据，请重新输入")

    def bullet_launch(self):
        while True:
            try:
                launch_position = int(input("请输入攻击的目标位置："))
            except ValueError:
                print("您输入的是无效数据，请重新输入")
            else:
                if 1 <= launch_position <= 10:
                    self.attack_position = launch_position
                    break
                else:
                    print("您输入的是无效数据，请重新输入")


class PCTank(BaseTank):
    def move(self):
        self.position = random.randint(1, 10)

    def bullet_launch(self):
        self.attack_position = random.randint(1, 10)


def play_game():
    # 创建玩家坦克
    my_tank = MyTank()
    # 创建电脑坦克
    pc_tank = PCTank()
    while True:
        # 玩家发射子弹
        my_tank.bullet_launch()
        # 电脑发射子弹
        pc_tank.bullet_launch()
        if my_tank.attack_position == pc_tank.position:
            pc_tank.HP -= 1
            print("电脑还剩{}点血".format(pc_tank.HP))
        if pc_tank.attack_position == my_tank.position:
            my_tank.HP -= 1
            print("玩家还剩{}点血".format(my_tank.HP))
        if my_tank.HP == 0 and pc_tank.HP == 0:
            print("平局")
            break
        elif my_tank.HP == 0:
            print("电脑胜利")
            break
        elif pc_tank.HP == 0:
            print("玩家胜利")
            break
        my_tank.move()
        pc_tank.move()



if __name__ == "__main__":
    play_game()