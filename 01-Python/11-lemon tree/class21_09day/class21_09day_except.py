# @Author : jiaojie
# @CreateDate : 2020/5/16 23:33
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
异常处理

异常就是程序运行出错了
异常分析：找到错误点
异常处理

常见异常
1. 变量没定义: nameError
2. 语法错误:
3. 键不存在：keyError
4. 没找到模块: ModuleNotFoundError
5. 类型错误：TypeError
6. IndexError

BaseException
systemExit
keyboardInterrupt

try:
    有可能会出现错误的代码
except:
    try里面的代码出现了错误之后，对错误处理的代码
else:
    try 中的代码没有发生错误，执行else中的代码
finally:
    不管代码有没有错误都会执行
"""

print(111)
# try:
#     print(a)
# except:
#     #print('代码出错了')
#     pass

# try:
#     with open('text.txt', 'r', encoding='utf8') as f:
#         print(f.read())
# except:
#     with open('text.txt', 'w', encoding='utf8') as f:
#         print(f.write('初始化内容'))
# else:
#     print('代码没有出现错误，执行else的代码')
# finally:
#     print('不管代码有没有错误都会执行')
#
# print(22)

def copy_file(path):
    # 切换工作路径
    # 获取所有的文件和目录列表
    #判断是否是文件
    pass

copy_file('C:/Personal/Study/Python/lemon tree/class21_09day')