"""
3.匹配出合法的身份证号码（15 或 18位，最后一个可能是字符X）

s= "1234578457845 d124568745421212 123456789123456 78978978978978978d 123457896547854X 784568785X123456 1234567891234567891"

4. 写一个正则表达式判断一个字符串是否是ip地址

规则：一个ip地址由4个数字组成，每个数字之间用.连接。每个数字的大小是0-255 例如：255.189.10.37 正确 256.189.89.9 错误

5.验证输入的内容只能是汉字

6.计算一个字符串中所有的数字的和

例如：字符串是：‘hello90abc 78sjh12.5’ 结果是90+78+12.5 = 180.5

s = "hello77s 88hi dfs7.5s 6sdfs89 dsa3dfs5ss1 "
"""

import re


id_str = "1234578457845 d124568745421212 123456789123456 78978978978978978d " \
    "12345789654789954X 784568785X123456 1234567891234567891 123457896547899549"

id_pattern = re.compile(r"\d{14}X\b|\d{17}X\b|\d{15}\b|\d{18}\b")
id_result = id_pattern.findall(id_str)
print(id_result)


ip_str = "255.189.10.37"
ip_pattern = re.compile(r"(([1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}([1-9]$|[1-9]\d$|1\d{2}$|2[0-4]\d$|25[0-5]$)")
ip_result = ip_pattern.search(ip_str)
print(ip_result)

my_input = input("请输入汉字：")
matchObj = re.match(r"^[\u4E00-\u9FA5]+$", my_input)
if matchObj:
    print(matchObj.group())
else:
    print("No match")


str6 = "hello77s 88hi dfs7.5s 6sdfs89 dsa3dfs5ss1 "

pattern6 = re.compile(r"\d+\.\d+|\d+")
result6 = pattern6.findall(str6)
num_sum = 0
for i in result6:
    num_sum += float(i)
print("所有的数字的和：", num_sum)

