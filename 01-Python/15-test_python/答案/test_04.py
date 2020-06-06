# @Author : 强小林
# @CreateDate : 2020/5/9 14:19
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

# 1、将给定字符串的PHP替换为Python

print("--------------第1题--------------")
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP", "Python"))

# 2、现在有一个列表 li2=[1，2，3，4，5]，
#     第一步：请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]，
#     第二步：对li2进行排序处理
#     第三步：删除li2中的倒数第二个元素

print("--------------第2题--------------")

li2 = [1, 2, 3, 4, 5]

li2.insert(0, 0)
li2.insert(4, 66)
li2.extend([11, 22, 33])
print("插入元素后的li2为:{}".format(li2))

li2.sort()  # 正序li2.sort(reverse=False)
# li2.sort(reverse=True)  # 反序
# li2.reverse()  # 反倒序
print("li2进行从小到大排序后为:{}".format(li2))

li2.pop(-2)
print("删除li2中的倒数第二个元素后:{}".format(li2))

# 3、切片
#     1、li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
#     2、s = 'python java php',通过切片获取:'java'
#     3、tu = ['a','b','c','d','e','f','g','h'],通过切片获取['g', 'b']

print("--------------第3题--------------")

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("li切片后:{}".format(li[2::3]))

s = 'python java php'
print("s切片后（方法1）结果为:{}".format(s[7:11]))  # 方法1
print("s切片后（方法2）结果为:{}".format(s.split(" ")[1]))  # 方法2

tu = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("tu切片后（方法1）结果为:{}".format(tu[-2::-5]))  # 方法1

# 方法2
tu_new = tu[1::5]
tu_new.reverse()
print("tu切片后（方法2）结果为:{}".format(tu_new))
