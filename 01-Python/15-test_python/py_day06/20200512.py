# @Author : jiaojie
# @CreateDate : 2020/5/12 20:36
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
例如：12321是回文数，个位与万位相同，十位与千位相同。 根据判断打印出相关信息。

"""
"""
格式化输出:
format:
1、{}占位
指定顺序：{n}、{变量名}

2、指定格式
{:.nf}：保留小数点位数，f只能用于浮点数或整数，保留方式采用四舍五入
    {:.2f}表示保留小数点后2位, {:.0f}表示不保留小数点

{:.n%}：保留百分比，f只能用于浮点数或整数，保留方式采用四舍五入
    {:.2%}表示保留到小数点后2位

{:x>ns}：表示向左侧补充x，直至整个数据的长度为n
{:>nd}：表示向左侧补充n个空格
{:x<nd}：表示向数据右侧补充x，直至整个数据的长度为n
{:ns}：等同于{:<ns}，表示向右侧补充n个空格
{:^ns}：表示居中对齐，整个数据长度为n；若n为奇数时，数据偏左显示1个字符
以上：
    s：用于字符串，不能用于浮点数或整数，一个汉字长度按1计算
    d：用于整型数据，1个数字长度按1计算
    f：不太适用，用的时候不会报错；永远只会将浮点数保留6位
"""

print("---------------------第1题---------------------")

price = int(input("请输入购买金额："))
if price < 0:
    print("输入金额有误")
elif 50 <= price <= 100:
    print("购买金额{0},打10%，折扣后{1}".format(price, price*0.9))
elif price > 100:
    print("购买金额{},打20%，折扣后{:.2f}".format(price, price*0.8))

print("---------------------第2题---------------------")

print("方法一：")
num = input("请输入一个5位数：")

if len(num) == 5:
    if num[0] == num[4] and num[1] == num[3]:
        print("此数据是回文数：",int(num))
    else:
        print("此数据不是回文数：", int(num))
else:
    print("输入不是5位数")

print("方法二：")

while True:
    num = input("请输入一个5位数：")
    li = list(num)
    old_li = li.copy()
    #print("old_li:",old_li)
    li.reverse()
    #print("new_li:",li)
    if old_li == li:
        print("此数据是回文数：", int(num))
        break
    else:
        print("此数据不是回文数：", int(num))


print("方法三：")
num = input("请输入一个5位数：")
start = 0
end = len(num)-1

while start < end:
    if num[start] == num[end]:
        start += 1
        end -= 1
    else:
        print("此数据不是回文数：", int(num))
        break
else:
    print("此数据是回文数：", int(num))




