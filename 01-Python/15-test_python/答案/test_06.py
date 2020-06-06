# @Author : 强小林
# @CreateDate : 2020/5/13 17:54
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription : 

"""
python打卡第六天

1、一家商场在降价促销：
如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣；
如果购买金额大于100元会给20%折扣。
编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格。

2、一个5位数，判断它是不是回文数。
例如：12321是回文数，个位与万位相同，十位与千位相同。 根据判断打印出相关信息

"""

# 第1题：可优化项：输入合法性--利用正则 re.match(r'^\d+(\.\d{1,2})?$', price)
print("----------第一题----------")

price = float(input("请输入原始购买价格："))
discount_price = 0
final_price = price

if price > 100:
    discount_price = price * 0.2
elif price >= 50:
    discount_price = price * 0.1

final_price = price - discount_price

print("您购买的商品原价为{:.2f}元，优惠了{:.2f}元，最终需支付{:.2f}元".format(price, discount_price, final_price))

# 第2题：可优化项：按需输入--利用正则 re.match(r'^[1-9]{1}\d{4}$', num)

# 方法1：利用列表可以反序，不限制死只能5位数
print("----------第二题：方法1----------")

num = input("请输入一个5位数：")
num = list(num)
num_new = num.copy()  # 复制列表
num_new.reverse()  # 列表反序

if num == num_new:
    print("您输入的数字是个回文数")
else:
    print("您输入的数字不是回文数")

# 方法2：利用字符串索引，用while-else循环语句，不限制死只能5位数
print("----------第二题：方法2----------")

num = input("请输入一个5位数：")
start = 0
end = len(num) - 1

while start < end:
    if num[start] == num[end]:
        start += 1
        end -= 1
    else:
        print("您输入的数字不是回文数")
        break
else:
    print("您输入的数字是个回文数")

# 方法3：利用数值的算术运算，优势是如果直接给个整型数据，就不能用前两种方法了，缺点是限制为5位数了
print("----------第二题：方法3----------")

num = int(input("请输入一个5位数："))

num1 = num // 10000
num2 = (num // 1000) % 10
num4 = (num % 100) // 10
num5 = num % 10

if num1 == num5 and num2 == num4:
    print("您输入的数字是个回文数")
else:
    print("您输入的数字不是回文数")