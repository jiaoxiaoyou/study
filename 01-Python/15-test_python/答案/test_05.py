# @Author : 强小林
# @CreateDate : 2020/5/9 14:19
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription : 

"""
python打卡第五天
1、有5道题（通过字典来操作）：
    （1）某比赛需要获取你的个人信息，设计一个程序，运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据存储起来
    （2）数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
    （3）有一个人对你很感兴趣，平台需要您补足您的身高和联系方式
    （4）平台为了保护你的隐私，需要你删除你的联系方式
    （5）你为了取得更好的成绩，你添加了自己的擅长技能，至少需要 3 项
2、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，请统计列表中不重复的元素个数

"""

# 第一题

print("----------第一题----------")

print("1、请输入您的个人信息：")

name = input("请输入姓名：")
sex = input("请输入性别：")
age = input("请输入年龄：")

dict_user = {"姓名": name, "性别": sex, "年龄": age}
# dict_user = dict(姓名=name, 性别=sex, 年龄=age)  # 也可用此方式

print("2、请进行自我介绍：")

print("我的名字是{0}，今年{1}岁，性别{2}，喜欢敲代码".format(dict_user["姓名"], dict_user["年龄"], dict_user["性别"]))

print("3、请补充您的个人信息：")

height = input("请输入身高：")
iphone = input("请输入联系方式：")
dict_user.update({"身高": height, "联系方式": iphone})

print("补充后您的信息为：{}".format(dict_user))

print("4、为保护隐私，系统将删除您的联系方式：")

dict_user.pop("联系方式")
print("删除联系方式后我的信息为：{}".format(dict_user))

print("5、请补充您的擅长技能：")

skills = input("请输入不少于三项技能，用空格隔开：")
list_skills = skills.split(" ")
dict_user["擅长技能"] = list_skills

print("增加擅长技能后您的信息为：{}".format(dict_user))


# 第二题
print("----------第二题----------")

li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]

# 对题意的理解1：[11, 22, 33, 44, 55, 77, 88, 99]

li = set(li)  # 此处还可以继续转换为list(set(li)) ，但没有必要，len()是内置函数，可用于集合
print("li列表中不重复的元素个数为：{}".format(len(li)))

# 对题意的理解2：[33, 44, 55, 77, 88, 99]
print("----------第二题：另一种理解----------")

li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]

num = 0

for i in li:
    if li.count(i) > 1:
        num += 1

print("不重复的元素个数为：{0}\n".format(len(li) - num))


