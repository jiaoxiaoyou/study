"""
@Author : JJ
@Time : 2020/4/27 21:34
@Desc : 
"""

"""
1、 用户登陆程序需求: 
    1. 输入用户名和密码; 
    2. 判断用户名和密码是否正确? (name='root', passwd='westos') 
    3. 为了防止暴力破解， 登陆仅有三次机会， 如果超过三次机会， 提示错误次数过多，账号已被冻结
2、使用了 while 来计算 1 到 100 的总和
"""

print("---------------------第一题---------------------")

times = 0

while times < 3:
    name = input("请输入用户名：")
    passwd = input("请输入密码：")
    if name == 'root' and passwd == 'westos':
        print('登录成功')
        break
    times += 1
    print('用户名或者密码失败,失败次数：', times)
else:
    print('错误次数过多，账号已被冻结')



print("---------------------第二题---------------------")

count = 0
a = 1
while a <= 100:
    #print(a)
    a += 1
    count += a
print(count)



