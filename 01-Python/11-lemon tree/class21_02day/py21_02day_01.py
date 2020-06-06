"""
小整数值：-5到256

"""

a = 10
b = 10

print("a is b:", a is b)

c = 1000
d = 1000
print("c is d:", c is d)

"""
random模块：生成随机数
"""

import random
# 生成随机浮点数（0-1）
a = random.random()

print(a)

# 生成随机的整数
b = random.randint(1,100)
print(b)