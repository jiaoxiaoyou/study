# @Author : jiaojie
# @CreateDate : 2020/5/16 14:17
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :


"""  类和实例  """
# 类名通常是大写开头
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
#
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 80:
#             return 'B'
#         else:
#             return 'C'

# bart = Student()
# print(bart)
# print(Student)
#
# bart.name = 'Bart Simpson'
# print(bart.name)

# bart = Student('Bart Simpson', 59)
# print(bart.name)
# print(bart.score)
# bart.print_score()
# lisa = Student('Lisa', 99)
# print(bart.name, bart.get_grade())
# print(lisa.name, lisa.get_grade())

""" 访问限制 """
class Student(object):
    def __init__(self, name, score):
        self.__name = name  # 变量名如果以__开头，就变成一个私有变量
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')



bart = Student('Bart Simpson', 59)
# print(bart.name)  #会报错，应该私有变量外部不能访问
print(bart._Student__name)
print(bart.get_name())
bart.set_score(99)
print(bart.get_score())



""" 继承和多态 """

# class Animal(object):
#     def run(self):
#         print('Animal is running……')
#
#
# class Dog(Animal):
#     def run(self):
#         print('Dog is running……')
#
#     def eat(self):
#         print('Eating meat……')
#
# class Cat(Animal):
#     def run(self):
#         print('Cat is running...')
#
#     def eat(self):
#         print('Eating fish……')
#
# dog = Dog()
# dog.run()
#
# cat = Cat()
# cat.run()
#
# a = list()
# b = Animal()
# c = Dog()
#
# print(isinstance(a, list))
# print(isinstance(b, Animal))
# print(isinstance(c, Dog))
# print(isinstance(c, Animal))
# print(isinstance(b, Dog))
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
# run_twice(Animal())
# run_twice(Dog())
# run_twice(Cat())
#
# class Tortoise(Animal):
#     def run(self):
#         print('Tortoise is running slowly...')
#
# run_twice(Tortoise())
#
""" 获取对象信息 """
#
# print(type(11123))
# print(type('11123'))
# print(type(None))
# print(type(abs))
# print(type(a))
# print(type(123)== type(456))
# print(type(123)==int)
# print(type('123')== type('abc'))
# print(type('123')==str)
# print(type('123')==type(123))
#
# import types
# def fn():
#     pass
#
# print(type(fn)==types.FrameType)
# print(type(abs)==types.BuiltinFunctionType)
# print(type(lambda x: x)==types.LambdaType)
# print(type((x for x in range(10)))==types.GeneratorType)
#
# # isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
# print(isinstance([1,2,3],(list,tuple)))
#
# # 如果获取一个对象的所有属性和方法，使用dir()
# print(dir(123))
# print(dir('123'))
#
# print(len('123'))
# print('123'.__len__())
#
# class MyDog(object):
#     def __len__(self):
#         return 100
#
# dog = MyDog()
# print(len(dog))
#
# print('ABC'.lower())
#
# # getattr()
# # setattr()
# # hasattr()
#
# class MyObject(object):
#     def __init__(self):
#         self.x = 9
#     def power(self):
#         return self.x * self.x
#
# obj = MyObject()
#
# print("obj 有属性'x'吗：",hasattr(obj, 'x'))
# print("obj 有属性'y'吗：",hasattr(obj, 'y'))
# setattr(obj, 'y', 19)
# print("obj 有属性'y'吗：",hasattr(obj, 'y'))
# print("获取属性'y'：",getattr(obj, 'y'))
# print("获取属性'y'：",obj.y)
# print("获取属性'z'：",getattr(obj, 'z', 404))
# print("obj 有属性'power'吗：",hasattr(obj, 'power'))
# print(getattr(obj, 'power'))
# fn = getattr(obj, 'power')
# print(fn)
# print(fn())
#
# def readImage(fp):
#     if hasattr(fp, 'read'):
#         pass
#         #return readData(fp)
#     return None

""" 实例属性和类属性 """

# class Student(object):
#     name = 'Student'
#     # def __init__(self, name):
#     #     self.name = name
#
# # s = Student('Bob')
# # s.score = 90
# s = Student()
# print(s.name)
#
# print(Student.name)
# s.name = 'Michael'
# print(s.name)
# print(Student.name)
# del s.name
# print(s.name)