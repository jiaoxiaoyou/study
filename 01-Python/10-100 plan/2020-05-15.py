# @Author : jiaojie
# @CreateDate : 2020/5/15 23:44
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
5、写一个Bicycle(自行车)类,有run(骑行)方法, 调用时显示骑行里程km:
再写一个电动自行车类EBicycle继承自Bicycle,添加电池电量valume属性, 同时有两个方法：
1）. fill_charge(vol) 用来充电, vol 为电量(度)
2.） run(km) 方法用于骑行,每骑行10km消耗电量1度,当电量消耗尽时调用Bicycle的run方法骑行
并显示骑行结果
"""
print("---------------------第5题---------------------")
class Bicycle(object):
    def run(self, mileage):
        print("骑行里程：{} km".format(mileage))

class EBicycle(Bicycle):
    def __init__(self):
        self.valume = 0

    def fill_charge(self,valume):
        self.valume = valume

    def run(self, mileage):
        if self.valume <= 0:
            super().run(mileage)
        else:
            # 可骑行里程
            cycling_mileage = self.valume / 10
            print('可骑行里程：{} km'.format(cycling_mileage))

print("---------------------第6题---------------------")

"""
6、模拟英雄联盟写一个游戏人物的类:
(1)创建一个 Game_role的类.
(2) 构造方法中给对象封装name,ad(攻击力),hp(血量).三个属性.
(3) 创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
例: 实例化一个对象 盖伦,ad为10, hp为100
实例化另个一个对象 剑豪 ad为20, hp为80
盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血, 还剩多少血'的提示功能
"""

class Game_role(object):
    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

def attack():
    role1 = Game_role('盖伦', 10, 100)
    role2 = Game_role('剑豪', 20, 80)
    print("{0}攻击{1},{1}掉了{2}血, 还剩{3}血".format(role1.name, role2.name, role1.ad, role2.hp-role1.ad))
    print("{0}攻击{1},{1}掉了{2}血, 还剩{3}血".format(role2.name, role1.name, role2.ad, role1.hp-role2.ad))

if __name__ == '__main__':
    attack()
    e_bicycle = EBicycle()
    e_bicycle.fill_charge(1)
    e_bicycle.run(1)