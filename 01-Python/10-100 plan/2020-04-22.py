"""
@Author : JJ
@Time : 2020/4/22 21:11
@Desc : 
"""

"""
1. 0422-字符串截取子串
2. 0422-字典的遍历方式
"""

print("---------------------第一题---------------------")
# 字符串截取字串

str1 = 'aaabbbcccdddeeefff'
print('字符串截取子串：',str1[3:9])
print('字符串截取子串：',str1[::3])
print('字符串截取子串：',str1[-1:-7:-1])

print("---------------------第二题---------------------")
# 字典的遍历方式

dict1 = {'name': 'zhangsan', 'age': 18, 'gender': 'boy'}

print('***打印key***')
for i in dict1.keys():
    print(i)

print('***打印value***')
for i in dict1.values():
    print(i)

print('***打印(key,value)***')
for i in dict1.items():
    print(i)

print('***打印key:value***')
for k,v in dict1.items():
    print(k,':',v)

