# @Author : jiaojie
# @CreateDate : 2020/5/11 23:10
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

print("---------------------第1题---------------------")
# dict = {key1 : value1, key2 : value2 }
dict = {}
dict['name'] = input('请输入姓名：')
dict['gender'] = input('请输入性别：')
dict['age'] = int(input('请输入年龄：'))

print("我的名字{name}，今年{age}岁，性别：{gender}，喜欢敲代码".format(name=dict['name'],age=dict['age'],gender=dict['gender']))

dict['height'] = '180cm'
dict['telephone'] = '18888888888'

print(dict)

del dict['telephone']
print("删除联系方式之前：",dict)

dict['hobby'] = ['hobby1', 'hobby2', 'hobby3']
print("增加爱好之后：",dict)



print("---------------------第2题---------------------")

li = [11,22,33,22,22,44,55,77,88,99,11]

len_all = len(li)

print("方法一：")
# 集合中没有重复的元素
de_duplication_list = list(set(li))
print(de_duplication_list)

print("去重之后的列表长度：",len(de_duplication_list))

print("方法二：")
new_list1 = []
for i in li:
    if i not in new_list1:
        new_list1.append(i)
print(new_list1)
print("去重之后的列表长度：",len(new_list1))

print("方法三：")
import itertools
li.sort()
li2 = itertools.groupby(li)
new_list2 = []
for k,v in li2:
    new_list2.append(k)

print(new_list2)
print("去重之后的列表长度：",len(new_list2))
