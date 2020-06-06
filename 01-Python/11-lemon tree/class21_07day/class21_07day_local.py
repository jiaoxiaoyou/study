"""
@Author : jiaojie
@Time : 2020/4/19 20:55
@Desc : 
"""

"""
函数的作用域：
全局变量：直接定义在模块（py中的变量），在整个文件中任何地方都能够访问
局部变量：定义在函数中的，它的作用范围，仅限于当前的作用域（定义的函数中）

"""
a = 200

def func():
    b = 100
    print(b)
    print(a)

func()

print('-------------------------------------')

# 在函数中声明全局变量

def func1():
    global a
    a = 333300
func1()
print(a)

print('-------------------------------------')
b = 11
def func2():
    # b = b+100 # 不能对全局变量直接操作，需要赋值以后再操作
    # print(b)
    c = b
    c = c + 100
    print(c)

func2()
print(b)

print('-------------------------------------')
num = 1000

def func3():
    print("func3---num",num)

    def func4():
        global num
        num += 1
        print("func4---num",num)

    func4()

func3()
print(num)

print('-------------------------------------')
num1 = 10

def func5():
    num = 100
    def func6():
        nonlocal num
        num = 999
        print('func6----num:',num)
    func6()
    print('func5----num:',num)

func5()