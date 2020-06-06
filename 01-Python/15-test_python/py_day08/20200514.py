# @Author : jiaojie
# @CreateDate : 2020/5/14 16:22
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""

python打卡第八天
1、输出99乘法表，结果如下：（提示嵌套for循环，格式化输出）
1 * 1 = 1

2 * 1 = 2  2 * 2 = 4

3 * 1 = 3  3 * 2 = 6  3 * 3 = 9

4 * 1 = 4  4 * 2 = 8  4 * 3 = 12 4 * 4 = 16

5 * 1 = 5  5 * 2 = 10 5 * 3 = 15 5 * 4 = 20 5 * 5 = 25

6 * 1 = 6  6 * 2 = 12 6 * 3 = 18 6 * 4 = 24 6 * 5 = 30 6 * 6 = 36

7 * 1 = 7  7 * 2 = 14 7 * 3 = 21 7 * 4 = 28 7 * 5 = 35 7 * 6 = 42 7 * 7 = 49

8 * 1 = 8  8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64

9 * 1 = 9  9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81

2、通过函数实现一个计算器，运行程序分别提示用户输入数字1、数字2，
然后再提示用户选择 ：加【1】 减【2】 乘【3】 除【4】，
每个方法使用一个函数来实现，选择后调用对应的函数，然后返回结果。

"""

print("---------------------第1题---------------------")

for i in range(1,10):
    for j in range(1,i+1):
        print("{0} * {1} = {2}  ".format(i, j, i*j),end="")
    print("\n")


print("---------------------第2题---------------------")

def add(x, y):
    print("{0} + {1} = {2}".format(x, y, x+y))
    return x + y

def sub(x, y):
    print("{0} - {1} = {2}".format(x, y, x - y))
    return x - y

def divide(x, y):
    if y == 0:
        print("0不能作为除数")
    else:
        print("{0} / {1} = {2}".format(x, y, x / y))
        return x / y

def multi(x, y):
    print("{0} * {1} = {2}".format(x, y, x * y))
    return x * y

num1 = int(input("请输入数字1："))
num2 = int(input("请输入数字2："))
print("加【1】 减【2】 乘【3】 除【4】")
operation = int(input("请选择运算方法："))

if operation == 1:

    add(num1, num2)
elif operation == 2:
    sub(num1, num2)
elif operation ==3:
    multi(num1, num2)
elif operation ==4:
    divide(num1, num2)

