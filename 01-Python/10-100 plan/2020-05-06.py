"""
@Author : jiaojie
@filename : 2020-05-06.py
@DATE : 2020/5/6 
@Time : 23:45
@Desc : 
"""

"""
1. 1.冒泡法对b=[9, 7, 8, 6, 5, 3, 4, 2, 1]进行排序，返回计算次数
2. 2.求十万内所有素数，返回个数，计算次数，执行时间
"""

print("---------------------第一题---------------------")

b = [9, 7, 8, 6, 5, 3, 4, 2, 1]

length = len(b)
times = 0
for i in range (0, length):
    #print(b[i])
    for j in range(0, length-i-1):
        if b[j] > b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]
            times = times + 1
print(b)
print("交换次数：",times)


print("---------------------第二题---------------------")

# 素数又称质数（prime number），有无限个。质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数的数称为素数
# for……else…… else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行
import time
count = 0   # 素数个数
times = 0   # 计算次数
num = []
start = time.perf_counter()
for i in range(3, 100000):
    for j in range(3, i):
        times += 1
        if i%j == 0:
            break
    else:
        count += 1
        num.append(i)
end = time.perf_counter()

print(num)
print("素数个数：",count)
print("计算了{0}次".format(times))
print("执行时间：{0}s".format(end - start))
