"""
@Author : JJ
@Time : 2020/4/23 21:05
@Desc : 
"""

"""
1.0423-列表的增加、删除、更新
2.0423-字典的增加、删除、更新
"""

print("---------------------第一题---------------------")
# 列表的增加、删除、更新
list1 = ['aa', 'bb', 'cc', 'dd']

list1.append(11)
list1.append(22)
list1.append(33)
print('append新增后的列表：',list1)

list1.pop()
print('pop删除后的列表：',list1)

list1.remove(11)
print('remove删除后的列表：',list1)

list1[2] = 'ss'
print('更新后的列表：',list1)


print("---------------------第二题---------------------")
# 字典的增加、删除、更新
dict1 = {'name': 'zhangsan', 'age': 18, 'gender': 'boy'}

dict1['Class'] = 'First'
print('新增后的字典：',dict1)

dict1['age'] = 16
print('更新后的字典：',dict1)

del dict1['name']   # 删除键name
print('del删除后的字典：',dict1)

dict1.clear()    #清空字典
print('clear清空后的字典：',dict1)



