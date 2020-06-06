# @Author : 强小林
# @CreateDate : 2020/5/26 10:28
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
    BaseTank拥有postion属性（这个属性代表Tank的位置，位置随机生成，一共有（1,10）10个位置）
    BeseTank拥有HP属性（代表血量，默认为10）
    BeseTank拥有attck_postion属性（代表攻击位置，位置随机生成，一共有（1,10）10个位置）
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


# 坦克基类
class Tank(object):
    def __init__(self, name):
        self.name = name
        self.live = 1  # 表示tank是否存活：1表示存活，0表示死亡
        self.HP = 10  # HP表示血量，攻击成功一次，血量-1为；血量为0，则live
        self.postion = random.randint(1, 10)  # 坦克的位置
        self.attck_postion = random.randint(1, 10)  # 攻击的位置

    # 确定坦克对象是否还存活
    def online(self):
        if self.HP == 0:
            setattr(self, "live", 0)
            return False
        else:
            return True

    # 移动tank位置
    def move(self, play):
        while self.online():  # 只有存活时才可以移动
            try:
                pos = int(eval(play))  # 这样写，是为了让人和电脑都可以复用此方法
                if pos in range(1, 11):
                    setattr(self, "postion", pos)  # 修改坦克位置
                    break
                else:
                    print("else：您输入的数据无效，请重新输入")
            except:
                print("except：您输入的数据无效，请重新输入")
        return pos

    # 确定攻击坦克位置
    def bullet_launch(self, tank, play):
        while self.online() and tank.online():  # 只有自己和对方都存活，才可进行攻击
            try:
                att_pos = int(eval(play))  # 这样写，是为了让人和电脑都可以复用此方法
                if att_pos in range(1, 11):
                    setattr(self, "attck_postion", att_pos)  # 修改攻击位置
                    if tank.postion == self.attck_postion:  # 攻击位置与对手的位置一致时，才认为攻击成功
                        tank.HP -= 1  # 攻击成功血量-1
                        str_p = "【{0}】攻击了【{1}】，此时【{1}】在位置【{3}】，攻击位置是【{4}】，攻击成功，攻击后【{1}】的血量为{2}"
                        print(str_p.format(self.name, tank.name, tank.HP, tank.postion, self.attck_postion))
                    else:
                        str_p = "【{0}】攻击了【{1}】，此时【{1}】在位置【{3}】，攻击位置是【{4}】，攻击失败，攻击后【{1}】的血量为{2}"
                        print(str_p.format(self.name, tank.name, tank.HP, tank.postion, self.attck_postion))
                    break
                else:
                    print("else：您输入的数据无效，请重新输入")
            except:
                print("except：您输入的数据无效，请重新输入")


# 玩家坦克
class MyTank(Tank):

    # 移动tank位置
    def move(self):
        super().move('input("请输入移动的目标位置（1-10）：")')

    # 确定攻击坦克位置
    def bullet_launch(self, tank):
        super().bullet_launch(tank, 'input("请输入攻击的目标位置（1-10）：")')


# 电脑坦克
class PCTank(Tank):
    # 移动tank位置
    def move(self):
        super().move('1')  # 调试的时候用这个写死
        # super().move('random.randint(1, 10)')

    def bullet_launch(self, tank):
        super().bullet_launch(tank, '1')  # 调试的时候用这个写死
        # super().bullet_launch(tank, 'random.randint(1, 10)')


# 玩家和电脑PK类
class TankPK(object):  # 无需继承玩家和电脑坦克类
    def __init__(self, name_p, name_c):
        self.name_p = name_p
        self.name_c = name_c

    def tank_PK(self):
        print("---------游戏启动，玩家正在进入房间---------")
        person = MyTank(self.name_p)  # 创建玩家
        computer = PCTank(self.name_c)  # 创建玩家
        print("--------玩家已准备就绪，即将开始游戏--------")
        count = 0  # 记录对打次数
        while person.online() and computer.online():  # 两人同时存活才可进行对打
            count += 1
            print("----------------第{}回合----------------".format(count))
            person.bullet_launch(computer)
            if computer.HP == 0:  # 攻击后对方血量如果为0，直接结束游戏
                setattr(computer, "live", 0)
                print("-" * 50)
                print("经历{}个回合后，【{}】的血量为0，【{}】获取胜利，游戏结束".format(count, computer.name, person.name))
                break
            person.move()

            computer.bullet_launch(person)
            if person.HP == 0:  # 攻击后对方血量如果为0，直接结束游戏
                setattr(person, "live", 0)
                print("-" * 50)
                print("经历{}个回合后，【{}】的血量为0，【{}】获取胜利，游戏结束".format(count, person.name, computer.name))
                break
            computer.move()


pk = TankPK("强小林", "电脑")
pk.tank_PK()
