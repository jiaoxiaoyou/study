# @Author : jiaojie
# @CreateDate : 2020/5/18 19:27
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
python打卡第十天
1、导入模块，导入模块中的类，导入模块中的方法，导入模块中的变量
2、创建一个test.txt文件，向文件中写入几行内容，读取文件内容并打印出来

"""

print("---------------------第1题---------------------")
# 1、导入模块，导入模块中的类，导入模块中的方法，导入模块中的变量

# 导入模块
import dog
print(dog)

# 导入模块中的类,导入多个类
from dog import Dog, Student
print(Dog)

# 导入模块中的方法
from dog import Dog
print(Dog.call)

# 导入模块中的变量
from dog import function, name
print(function)
print(name)




print("---------------------第2题---------------------")
# 2、创建一个test.txt文件，向文件中写入几行内容，读取文件内容并打印出来

#f_new = open('test.txt', 'a')

f_old = open("./old.txt", 'r', encoding='utf-8')
for line in f_old.readlines():
    print(line)
    with open('new.txt', 'a+') as new_txt:
        new_txt.write(line)

