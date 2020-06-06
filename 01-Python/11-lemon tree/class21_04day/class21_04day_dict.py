"""
@Author : jiaojie
@Time : 2020/4/5 23:02
@Desc : 
"""

"""
字典：
字典的定义：{key1:value1, key2:value2}
key：是唯一的 不能重复，必须是不可变类型的数据
对于key的使用：建议使用字符串
value:可以任何类型的数据（python 中）

字典增删查改的方法
添加元素：通过键赋值，直接添加

修改元素：通过键直接修改

查找元素：
通过键直接找对应的value
get方法：也是通过键获取value值（好处：键不存在的时候不会报错）
items:获取所有的键值对，每个键值对为一个元组，放在dict_items类型的数据中，可以通过list转换为列表
keys:获取所有的值，放在dict_keys类型的数据中，可以通过list转换为列表
values:获取所有的值，放在dict_values类型的数据中，可以通过list转换为列表

删除元素：
pop:指定键删除元素值
popitem:删除最后一个元素
del：
"""

li = ['小明', 18, '1234567890']
dict1 = {'name':'xiaoming', 'age':18, 'phone':'1234567890', 'key':[11, 22, 33]}

dict2 = dict(name = '小明', age = 18, gender = '男')
# 添加
dict2['phone'] = '111111111'

# 添加多个键值对
dict2.update({'key1':999, 'age':8888})
print(dict2)

# 修改
dict2['name'] = 'musen'

# 查找元素
# print(dict2['age'])
# print(dict2.get('gender'))
#
# print(dict2.items())
# print(list(dict2.items()))
# print(dict2.keys())
# print(list(dict2.keys()))
# print(dict2.values())
# print(list(dict2.values()))


# 删除
print(dict2)
# pop
# res = dict2.pop('name')
# print(res)

#popitem：删除列表中最后一个元素
# res = dict2.popitem()
# print(res)

# del
#del dict2['age']

#print(dict2)