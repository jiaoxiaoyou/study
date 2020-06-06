# @Author : jiaojie
# @CreateDate : 2020/5/7 20:46
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

'''
***2020-05-07***

python打卡第二天
1、单引号、双引号、三引号的区别和用法
2、下面哪些不能作为标识符？
find  _num  7val  add.  def  pan  -print  open_file  FileName  print  INPUT  ls  user^name  list1  str_
3、总结变量的命名规范？明确标识符和变量的关系？（注意标识符是否区分大小写）
4、在控制台依次提示用户输入：姓名、年龄、性别 按照以下格式输出：
5、数值类型都有哪些？分别创建一个对应类型的变量

'''

print('---------------------第1题----------------------')
print('12'
      '21')
print("12"
      "21")
print("""12
21""")
print("It's me")
print('It\'s me')
print('"udp"')
print("'http'")

print('---------------------第2题----------------------')

#find  _num  7val  add.  def  pan  -print  open_file  FileName  print  INPUT  ls  user^name  list1  str_

# print 可以作为标识符，但是不建议使用

print('不能作为标识符的：7val add. def -print user^name')


print('---------------------第3题---------------------')
print("""
标识符的命名要求：
    1. 第一个字符必须是字母或者下划线_
    2. 标识符的其它部分由字母、数字和下划线组成
    3. 标识符对大小写敏感
    4. 中文也可以作为变量名
    5. 不用把保留字用作标识符
    
注：函数名，类名，项目名，包名，模块名其实都是标识符
""")
import keyword
print("所有保留字：",keyword.kwlist)

print('---------------------第4题---------------------')

name = input('请输入姓名：')
age = input('请输入年龄：')
gender = input('请输入性别：')
print('******************')
print('姓名：',name)
print('年龄：',age)
print('性别：',gender)
print('******************')

print('---------------------第5题---------------------')

print("""
六个标准的数据类型：
Number(数字)
String(字符串)
List(列表)
Tuple(元组)
Set(集合)
Dictionary(字典)
""")

num1, num2, num3, num4 = 11, 3.9, False, 2+4j
print(num1, num2, num3, num4)

str1 = "123dfho"
print(str1)

list1 = [11, 22, 33, 44]
print(list1)

tuple1 = ('11', 'aa', 'cc')
print(tuple1)

set1 = {'beijing', 'xian', 'shanghai'}
print(set1)

dict1 = {'name':'jj', 'age':30}
print(dict1)
