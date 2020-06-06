# @Author : jiaojie
# @CreateDate : 2020/5/8 10:06
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :


"""
python打卡第三天
1、卖橘子的计算器：提示用户输入橘子的价格，然后随机生成购买的斤数（5到10斤之间），最后计算出应该支付的金额！
2、现在有字符串：str1 = 'python hello aaa 123123aabb'
（1）请计算字符串中有多少个'a'
（2）请找出字符串中'123'的下标起始位置
（3）请分别判断 'o a' 'he' 'ab' 'nh' 是否是该字符串中的成员？

"""

print('---------------------第1题----------------------')

import random
unit_price = int(input("请输入橘子的价格："))
total_price = unit_price * random.randint(5,10)
print("总共消费{0}元".format(total_price))


print('---------------------第2题----------------------')

str1 = 'python hello aaa 123123aabb'

# （1）请计算字符串中有多少个'a'
print("（1）请计算字符串中有多少个'a'")

# str.count(sub, start= 0,end=len(string))
sub1 = 'a'
print("str1中有{count}个'a'".format(count=str1.count(sub1)))


# （2）请找出字符串中'123'的下标起始位置
print("（2）请找出字符串中'123'的下标起始位置")

# str.find(str, beg=0, end=len(string))
sub2 = '123'
print("字符串'123'的下标起始位置-find：",str1.find(sub2))
print("字符串'123'的下标起始位置-index：",str1.index(sub2))

# str.index(str, beg=0, end=len(string))
# find和index的区别：find 找不到返回-1，index找不到抛个异常

sub3 = 'xyz'
print("字符串'xyz'的下标起始位置：",str1.find(sub3))
#print("字符串'xyz'的下标起始位置：",str1.index(sub3))


#（3）请分别判断 'o a' 'he' 'ab' 'nh' 是否是该字符串中的成员？
print("（3）请分别判断 'o a' 'he' 'ab' 'nh' 是否是该字符串中的成员？")

print("'o a'是否是该字符串中的成员：",'o a' in str1)
print("'he'是否是该字符串中的成员：",'he' in str1)
print("'ab'是否是该字符串中的成员：",'ab' in str1)
print("'nh'是否是该字符串中的成员：",'nh' in str1)




