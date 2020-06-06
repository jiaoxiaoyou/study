# @Author : jiaojie
# @CreateDate : 2020/5/16 23:04
# @Description : 第15节 Python调试方法以及技巧（1）
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

import os

"""
os模块 和操作系统交互的（windows linux mac）

相对路径：
.   代表当前目录下
..  代表上一级目录
绝对路径：电脑硬盘中的文件路径

"""
# 返回当前的工作路径 os.getcwd()
print("当前文件绝对路径：",os.getcwd())

# 切换工作路径 os.chdir()
# os.chdir('..')
#
# print("当前文件绝对路径：",os.getcwd())

# 创建目录
os.mkdir('pakafe02')
# 删除目录
os.rmdir('pakafe02')

print(os.listdir(r'C:\Personal\Study\Python\lemon tree\class21_09day'))

# 判断是否是目录
res = os.path.isdir('package')
print(res)

# 判断是否是文件
res2 = os.path.isfile('case.txt')
print(res2)

# 获取当前文件的绝对路径
print(__file__)

res1 = os.path.abspath(__file__)
print(res1)

# 当前文件的父级绝对路径
res3 = os.path.dirname(__file__)
res4 = os.path.dirname(res3)
print(res3)
print(res4)

# os.path.join()