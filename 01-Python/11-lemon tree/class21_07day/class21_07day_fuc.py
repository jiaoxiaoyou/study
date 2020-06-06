"""
@Author : jiaojie
@Time : 2020/4/19 22:14
@Desc : 
"""

"""
python中的内置函数

int  float  bool  str  list  tuple   
dict  set  range len
type  id  print  input

eval：能够识别字符中的python表达式
exec：动态执行字符串中的python代码


"""

li = [11,22,33,44,55]

max_value = max(li)
print(max_value)
print(min(li))
print(sum(li))


print('--------------------------------------')
li = [11,22,33,44,55,'a','bb']

for i,j in enumerate(li):
    print('下标：{},值：{}'.format(i,j))

print('--------------------------------------')
# eval:
str1 = 'li'
print(str1)
print(eval(str1))

# num = eval(input('请输入：'))
#
# print(type(num),num)

str2 = 'print("hello world")'
eval(str2)

print('--------------------------------------')
# exec
str5 = """
print(111)
"""

exec(str5)


print('--------------------------------------')

# filter

li2 = [11,22,33,44,1,41,98]

def func(x):
    # 一定要有返回值
    return x > 30

res = filter(func,li2)

print(list(res))

print('--------------------------------------')

# map:
# res2 = map(func, li2)
# print(list(res2))

def add(a):
    return a[0]+a[1]
list_val = [(11,22),(33,44),(55,66)]
res2 = map(add, list_val)
print(list(res2))

print('--------------------------------------')
# zip 打包

title = ['name', 'age', 'gender']
value = ['musen', '18', 'man']
res5 = zip(title, value)
for i in res5:
    print(i)
#print(list(res5))
#print(dict(res5))

print('--------------------------------------')

# isinstance:判断数据类型
num = 1000
str12 = 'str'
print(isinstance(num, str))


