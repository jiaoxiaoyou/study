# @Author : jiaojie
# @CreateDate : 2020/5/9 11:01
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
python打卡第四天
1、将给定字符串的PHP替换为Python
  best_language = "PHP is the best programming language in the world! "
2、现在有一个列表 li2=[1，2，3，4，5]，
    第一步：请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]
    第二步：对li2进行排序处理
    第三步：删除li2中的倒数第二个元素
3、切片运算
    （1）li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
    （2）s = 'python java php',通过切片获取: 'java'
    （3）tu = ['a','b','c','d','e','f','g','h'],通过切片获取 ['g', 'b']

"""

print("---------------------第1题---------------------")

# str.replace(old, new[, max])
best_language = "PHP is the best programming language in the world! "
print(best_language.replace('PHP', 'Python'))


print("---------------------第2题---------------------")

li2=[1, 2, 3, 4, 5]

# list.insert(index, obj)
li2.insert(0, 0)
li2.insert(4, 66)

# list.extend(seq)
li3 = [11, 22, 33]
# 方法一
li2.extend(li3)
print(li2)
# 方法二
#print("li2+li3:",li2+li3)

# list.sort(key=None, reverse=False)
li2.sort()
print(li2)

# list.pop([index=-1])
li2.pop(-2)
print(li2)


print("---------------------第3题---------------------")

# li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
li = [1,2,3,4,5,6,7,8,9]
print(li[2::3])

# s = 'python java php',通过切片获取: 'java'
s = 'python java php'
# [7:11] 截取的是7到10的字符串，不包含11
print(s[7:11])

# tu = ['a','b','c','d','e','f','g','h'],通过切片获取 ['g', 'b']
tu = ['a','b','c','d','e','f','g','h']

# 方法一
print(tu[-2:-8:-5])
# 方法二
tu1 = tu[1:7:5]
tu1.reverse()
print(tu1)

# !!! 错误的
print(tu1.reverse())


