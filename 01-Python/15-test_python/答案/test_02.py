# 作者 : 55414
# 文件名 : test_02
# 创建日期 : 2020/5/6 14:07
# 创建时间 : 2020/5/6 14:07

# print("="*10, "python打卡第一天", "="*10)
# print("hello python")

print("=" * 10, "python打卡第二天", "=" * 10)

print("""
1、单引号、双引号、三引号的区别和用法
- 单引号和双引号没有区别，常用于字符串中完成单双嵌套
- 三引号又称为文档字符串或文档注释，可以用来注释，也可以保留格式输出
""")

"""我是一条注释信息"""

print("我"
      "是"
      "强"
      "小"
      "林")  # 回车换行自动添加引号

print("我是'强小林'")

print("""
2、下面哪些不能作为标识符？
find  _num  7val  add.  def  pan  -print  open_file  FileName  print  INPUT  ls  user^name  list1  str_

答：7val add. def -print user^name """)

print("""
3、总结变量的命名规范？明确标识符和变量的关系？（注意标识符是否区分大小写）

变量命名规范：
- 只能包含数字、字母、下划线，且不能以数字为首
- 不能是python关键字
- 可以是python内置函数名、内置模块名，但不建议使用

标识符和变量的关系：
项目名、包名、模块名、函数名、类名等都是标识符，变量是标识符的一种，变量区分大小写
""")

print("4、在控制台依次提示用户输入：姓名、年龄、性别 按照以下格式输出：\n")
print("{0}\n姓名：{1}\n年龄：{2}\n性别：{3}\n{0}".format("*" * 18, input("请输入用户名："), input("请输入年龄："), input("请输入性别：")))

print("""
5、数值类型都有哪些？分别创建一个对应类型的变量

数值类型（Number）包含：
整型：int
浮点型：float
布尔型：bool（只有True False）
复数：complex（基本不会用到）
""")

a = int()
b = float()
c = bool()
d = complex()

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

a, b, c, d = 100, 99.99, True, 4 + 3j

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
