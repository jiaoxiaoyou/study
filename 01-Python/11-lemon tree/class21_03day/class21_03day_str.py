"""
Author : jiaojie
Time : 
Email : 15202938614@163.com
"""

"""
字符串的方法

count：查找元素的个数
find：查找字符串的下标
replace：替换指定字符
split：字符串分割
format：格式化输出
upper：转大写
lower：转小写
join：拼接
"""

str1 = "abc112233Abc"

# print(str1.split('11'))
print(str1.upper())
print(str1.lower())

str2 = 'aa bb c 7 jj aa   ll  '
print(str2.replace(' ',''))
print(''.join(str2.split(' ')))

# 替换
# res = str1.replace("a", 'hhh')
# print(res)


# 格式化输出

str4 = "今收到{:^8s}，交来的学费{:.2f}，日期{}"
print(str4.format('小明',8000,'2020-3-22'))

# {:x>4d} 左边填充
# {:x<4d} 右边填充

print("{0}xxx{1}yyyy{0}".format(100,200))
print("{c}111{b}222{a}".format(a='aaa',b='bbbb',c='ccc'))

# %s %d %f

print("这位同学叫：{name}，今天：{age}岁，银行卡余额：{money}".format(name='小明',age=18,money=99.99))

