# @Author : jiaojie
# @CreateDate : 2020/5/16 22:27
# @Description : 第14节 python异常处理&异常基类学习
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
1. 新建一个包pack，在包中新建两个模块module1.py, module2.py
在module1中定义一个函数，（函数实现上一次石头、剪刀布游戏的功能），
该函数可以通过传入的参数来控制游戏次数，然后在module2中导入module1中定义的函数，并调用

2.case.txt中存了很多数据，如下，一行位一条请求数据，怎么样才能把这些数据读取到并且保存到list中

url:http://127.0.0.1:/8080,mobilephone:18888888888,pwd:12345
url:http://127.0.0.1:/8081,mobilephone:18888888888,pwd:12345
url:http://127.0.0.1:/8082,mobilephone:18888888888,pwd:12345
url:http://127.0.0.1:/8083,mobilephone:18888888888,pwd:12345

请将文件中的数据读取出来，备注说明：读取出来的 数据保存格式为：
[{'url':'','mobilephone':'','pwd':''},{},{}]


3. 上次图书馆管理的作业，通过文件来实现，书记数据的永久存储。
思路：运行时从文件中读取数据，结束运行时将数据保存进文件
"""

print("---------------------第2题---------------------")
with open('case.txt', 'r') as f:
    cases = f.readlines()
print(cases)
for case in cases:
    # str.split(str="", num=string.count(str))
    datas = case.split(',')
    dic = {}
    for data in datas:
        i = data.split(':', 1)
        dic[i[0]] = i[1]

    print(dict)

