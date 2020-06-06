"""
1.匹配所有的开头字母内容
s1="i love you not because of who you are, but because of who i am when i am with you"
2.匹配所有开头的数字内容
s2="i love you not because 12df 56ere 666 r777 yy88"
"""
import re

str1 = "i love you not because of who you are, but because of who i am when i am with you"

pattern1 = re.compile(r"\b[a-zA-Z]")
result1 = pattern1.findall(str1)
print(result1)

str2 = "i love you not because 12df 56ere 666 r777 yy88 9"

pattern2 = re.compile(r"\b\d[0-9a-zA-Z]*")
result2 = pattern2.findall(str2)
print(result2)