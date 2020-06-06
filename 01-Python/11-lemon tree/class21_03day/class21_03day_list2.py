"""
Author : jiaojie
Time : 
Email : 15202938614@163.com
"""


"""
列表的增删改查

添加元素：
append：往列表尾部添加元素
insert：通过下标指定位置插入元素
extend：添加多个元素（多个元素放在列表中）
remove：指定内容删除
pop：指定下标删除
clear：一次性清空列表

"""

list = [1,2,3]


# print(id(list))
print(list)
list.append(4)
print(list)
# print(id(list1))
# print(id(list))

list.insert(1,"333")
print(list)

list.extend(['22','44'])
print(list)

list.remove('22')
print(list)

aList = [123, 'xyz', 'zara', 'abc']
aList.append( 2009 )
print("Updated List : ", aList)