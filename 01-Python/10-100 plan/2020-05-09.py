# @Author : jiaojie
# @CreateDate : 2020/5/9 22:02
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
继承和多态

"""

class Animal(object):
    def run(self):
        print('Animal is running……')

    def eat(self):
        print("Eating meat……")

class Dog(Animal):
    def run(self):
        print('Dog is running……')

class Cat(Animal):
    def run(self):
        print('Cat is running……')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

a = list()
b = Animal()
c = Dog()

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))

print(isinstance(c, Animal))
print(isinstance(b, Dog))

def run_twice(animal):
    animal.run()
    animal.run()

print(run_twice(Animal()))

print(run_twice(Dog()))

print(run_twice(Cat()))

class Tortoise(Animal):
    def run(self):
        print("Tortoise is running slowly……")

print(run_twice(Tortoise()))

