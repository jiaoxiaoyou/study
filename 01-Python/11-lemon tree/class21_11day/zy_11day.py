# @Author : jiaojie
# @CreateDate : 2020/5/26 19:33
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

# 定义测试用例类
class TestCases(object):
    def __init__(self, url, data, excepted, actual):
        """

        :param url:
        :param data:
        :param excepted:
        :param actual:
        """
        self.url = url
        self.data = data
        self.excepted = excepted
        self.actual = actual


case1 = TestCases(url='http://baidu.com', data={"user":999}, excepted={"user":1}, actual={"user":99})
setattr(case1, 'method', 'post')
res1 = getattr(case1, 'method')
res2 = case1.method
print(res1)
print(res2)
# 删除属性
delattr(case1, 'url')

"""
所有对象都有的属性而且属性值是一样的，设置为类属性
不同的对象之间，属性值是不一样的，设置为实例属性
self里的是实例属性
"""

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

