"""
Author : jiaojie
Time : 
Email : 15202938614@163.com
"""

"""
字符串拼接
"""

str3 = "python1"
str4 = "python2"

str5 = str3 + str4

print(str5)

print(str5*2)

# 字符串前边加r 关闭转义
str6 = r'hello \n world'
print(str6)

a = 'aaa'

#str7 = a.join(['111', '222', '333'])
str7 = a.join('123')

print(str7)

b = "pythonbbahskjaa"

print(b.find('a'))
print(b.count('a'))