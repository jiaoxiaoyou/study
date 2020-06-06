"""
@Author : JJ
@Time : 2020/4/26 21:10
@Desc : 
"""

"""
1. 请输入考试分数，并判断考试成绩的等级
    score >= 85 A
    score >= 75 B
    score >= 60 C
    score >= 40 D
    score >= 0 E
    
2.  输入一个5位数，判断这个数字是否是回文数 
"""

print("---------------------第一题---------------------")
score = int(input("请输入考试分数："))

if score > 100:
    print("输入的考试成绩有误")
elif score >= 85:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
elif score >= 40:
    print("D")
elif score >= 0:
    print("E")
else:
    print("输入的考试成绩有误")

print("---------------------第二题---------------------")
# 回文数例如：12321

num = input("请输入一个5位数字：")
if len(num) != 5:
    print('不是5位数字')
elif num[0] == num[4] and num[1] == num[3]:
    print("此数字是回文数：",num)
else:
    print("此数字不是回文数")