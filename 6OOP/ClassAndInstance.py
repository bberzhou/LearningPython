#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	类和实例：
		面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，
		比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
	在Python中，定义类是通过class关键字

"""


# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，
# 表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。


class Student(object):
	pass


# 创建实例（instance）：创建实例是通过类名+()实现的：
bart = Student()
print(bart)  # <__main__.Student object at 0x000001E0A6828250> bart指向一个Student实例，后面是内存地址
# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性
bart.name = 'Bart Sim'
print(bart.name)  # Bart Sim


# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：


class Teacher(object):
	# __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，
	# 就可以把各种属性绑定到self，因为self就指向创建的实例本身。
	# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
	# 但self不需要传，Python解释器自己会把实例变量传进去
	def __init__(self, name, age):
		self.name = name
		self.age = age


t1 = Teacher('Xu', 47)
print(t1.name)  # Xu
print(t1.age)  # 47
# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。

"""
	数据封装：
		面向对象编程的一个重要特点就是数据封装。在上面的Student类中，每个实例就拥有各自的name和score这些数据。我们可以通过函数来访问这些数据
		可以直接在Student类的内部定义访问数据的函数就把“数据”给封装起来了。
		这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：
		
	要定义一个方法，除了第一个参数是self外，其他和普通函数一样。
	要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入：
"""


class Animal(object):

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def print_info(self):
		print("name:%s, age:%s" % (self.name, self.age))

	def get_grade(self):
		if self.age >= 10:
			return 'A'
		else:
			return 'B'


dog = Animal('dog', 10)
dog.print_info()  # name:dog, age:10
print(dog.get_grade())  # A


"""
	小结：
		类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
		方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
		通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
		和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，
		对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
"""