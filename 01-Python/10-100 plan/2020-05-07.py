# @Author : jiaojie
# @CreateDate : 2020/5/7 21:31
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
1. 学习—类和实例，访问限制
2. 把Student对象的gender子段对外隐藏，用get_gender（）和set_geeder（）代替，并检查参数的有效性，返回测试结果。(有name和gender两个字段)

"""

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score  = score

# bart = Student()
# print(bart)
# print(Student)
# bart.name = 'Bart Simpson'
# print(bart.name)

# bart = Student('Bart Simpson', 59)
# print(bart.name)
# print(bart.score)

# def print_score(std):
#     print('{name}:{score}'.format(name=std.name, score=std.score))
#
# print_score(bart)

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('{name}:{score}'.format(name=self.name, score=self.score))
#
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
#
# bart = Student('Bart', 59)
# lisa = Student('Lisa', 99)
# bart.print_score()
# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())
#
# print(bart.score)
# bart.score = 88
# print(bart.score)

# 私有变量 变量名以__开头
class Student(object):

    def __init__(self, name, score, gender):
        self.__name = name
        self.__score = score
        self.__gender = gender

    def print_score(self):
        print('{name}:{score}'.format(name=self.__name, score=self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_gender(self):
        return self.__gender

    def set_score(self, score):
        self.__score = score

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('wrong parameter')

bart = Student('Bart', 88, 'male')
print(bart.get_gender())
bart.set_gender('female')
print(bart.get_gender())
bart.set_gender('woman')
print(bart.get_gender())