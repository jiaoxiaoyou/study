# @Author : jiaojie
# @CreateDate : 2020/5/14 0:04
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

print("---------------------第1题---------------------")
"""
要求：
* 类名、属性名、属性类型、方法名、方法参数、方法返回值自拟
* 自己写main函数测试设计是否合理

1.设计一个"狗"类
1>属性
* 颜色
* 奔跑的速度（单位是m/s）
* 性别
* 体重（单位是kg）

2>行为
* 吃： 每吃一次，体重增加0.5kg,输出吃完后的体重
* 吠（叫）：输出所有的属性
* 跑：每跑一次，体重减少0.5kg，输出速度和跑完后的体重

"""

class Dog(object):
    def __init__(self, color, speed, sex, weight):
        self.color = color
        self.speed = speed
        self.sex = sex
        self.weight = weight

    def eat(self):
        return self.weight + 0.5

    def call(self):
        print("color: {0}, speed: {1}, sex: {2}, weight: {3}".format(self.color, self.speed, self.sex, self.weight))

    def run(self):
        return self.weight - 0.5

if __name__ == '__main__':
    dog = Dog('black', 20, 'male', 10)
    dog.call()
    weight = dog.eat()
    print("吃胖了：",weight)



print("---------------------第2题---------------------")

"""
2.设计一个"学生"类
1>属性
* 姓名
* 生日
* 年龄
* 身高（单位是m）
* 体重（单位是kg）
* 性别
* C语言成绩
* OC成绩
* iOS成绩

2>行为
* 跑步：每跑步一次，身高增加1cm,体重减少0.5kg,输出跑完后的体重
* 吃饭：每次一次，身高增加1cm,体重增加0.5kg,输出吃完后的体重
* 学习：每学习一次，3可成绩各加1分，输出学习完后的3科成绩
* 睡觉：输出所有的属性

* 计算总分：算出3科成绩的总分并显示
* 计算平均分：算出3科成绩的平均分并显示
"""

class Student():
    def __init__(self, name, brith, age, height, weight, sex, C_language, OC_language, iOS_language):
        self.name = name
        self.birth = brith
        self.age = age
        self.height = height
        self.weight = weight
        self.sex = sex
        self.C_language = C_language
        self.OC_language = OC_language
        self.iOS_language = iOS_language

    def run(self):
        self.height += 1
        self.weight -= 0.5
        print(self.weight)

    def eat(self):
        self.height += 1
        self.weight += 0.5
        print(self.weight)

    def study(self):
        self.C_language += 1
        self.OC_language += 1
        self.iOS_language += 1

    def sleep(self):
        print(self.name, self.birth, self.age, self.height, self.weight, self.sex, self.C_language, self.OC_language, self.iOS_language)


    def sum(self):
        print("三科总成绩：",self.C_language+self.OC_language+self.iOS_language)

    def avg(self):
        print("三科平均成绩：",(self.C_language+self.OC_language+self.iOS_language)/3)


