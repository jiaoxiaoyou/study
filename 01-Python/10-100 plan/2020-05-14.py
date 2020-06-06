# @Author : jiaojie
# @CreateDate : 2020/5/14 23:04
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
3、写一个Student类,此类的对象有属性name, age, score, 用来保存学生的姓名,年龄,成绩:
1) 写一个函数input_student读入n个学生的信息,用对象来存储这些信息(不用字典),并返回对象的列表
2) 写一个函数output_student 打印这些学生信息(格式不限)

"""
print("---------------------第3题---------------------")
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


# students_info=[('zhangsan', 16, 88), ('lisi', 17, 89)]
def input_students(students_info=[]):
    list1 = []
    for student_info in students_info:
        list1.append(Student(student_info[0], student_info[1], student_info[2]))
    return list1


# students_info=[Student_Obj]
def output_student(students_obj=[]):
    for student_obj in students_obj:
        print('姓名：',student_obj.name,"，年龄：",student_obj.age,"，成绩：",student_obj.score)



print("---------------------第4题---------------------")
"""
4、定义一个类Huamn(人类),定义函数input_human录入信息,main调用显示信息:
有三个属性:姓名name,年龄age,家庭住址address (可以省略没有)
"""
class Human(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


# name = str,age = int,address = str
def input_human(name, age, address):
    return Human(name, age, address)

if __name__ == '__main__':
    students_obj = input_students([('zhangsan', 16, 88), ('lisi', 17, 89)])
    output_student(students_obj)

    human_obj = input_human('wangwu', 18, 'Shanxi')
    print("姓名：{0}，年龄：{1}，家庭住址：{2}".format(human_obj.name, human_obj.age, human_obj.address))