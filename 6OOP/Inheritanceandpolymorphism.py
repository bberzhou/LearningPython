#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	继承和多态：
		在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
		新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）

"""


class Animal(object):
	def runs(self):
		print("Animal is running...")

	def run_tw(animal):
		animal.runs()
		animal.runs()


class Dog(Animal):
	# pass
	def runs(self):
		print('Dog is running...')


class Cat(Animal):
	# pass
	def runs(self):
		print('Cat is running...')


# 对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似


dog = Dog()
dog.runs()  # Animal is running...
cat = Cat()
cat.runs()  # Animal is running...
# Dog is running...
# Cat is running...  在子类中重写父类的同名方法

# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，
# 在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。


"""
	当我们定义一个class的时候，我们实际上就定义了一种数据类型。
	我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样
	
	a = list() # a是list类型
	b = Animal() # b是Animal类型
	c = Dog() # c是Dog类型
	
	
"""
# 判断一个变量是否是某个类型可以用isinstance()判断：

print(isinstance(dog, Animal))  # True
print(isinstance(dog, Dog))  # True
print(isinstance(cat, Animal))  # True

# 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行
b = Animal()
print(isinstance(b, Dog))  # False


# 要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量


def run_tw(animal):
	# 调用runs()方法
	animal.runs()
	animal.runs()


# 当我们传入Animal的实例时，run_twice()就打印出
run_tw(Animal())
# Animal is running...
# Animal is running...

#  当我们传入Dog的实例时，run_twice()就打印出
run_tw(Dog())
# Dog is running...
# Dog is running...

# 当我们传入Cat的实例时，run_twice()就打印出：
run_tw(Cat())
# Cat is running...
# Cat is running...


class tortoise(Animal):
	def runs(self):
		print('totorise is running slowly...')


run_tw(tortoise())
# totorise is running slowly...
# totorise is running slowly...
# 新增一个Animal的子类，不必对run_twice()做任何修改，
# 实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。


"""
	调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，
	不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
		对扩展开放：允许新增Animal子类；
		对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
	Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
	
	继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，
	子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。	
"""


class Timer(object):

	def runs(self):
		print('start')


# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，

