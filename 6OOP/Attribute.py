#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	由于Python是动态语言，根据类创建的实例可以任意绑定属性

	如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：

"""


# 给实例绑定属性的方法是通过实例变量，或者通过self变量：


class Student(object):
	name = 'Student'

# def __init__(self, name):
# 	self.name = name


s = Student()
s.score = 90

# 定义一个类属性：name = 'Student'，类的所有实例都可以访问到

s1 = Student()
# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(s.name)  # Student
print(s1.name)
# 打印类的name属性
print(Student.name)  # Student

# 给实例绑定name属性
s.name = 'Michael'
print(s.name)  # Michael 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name)  # Student 但是类属性并未消失，用Student.name仍然可以访问


# 练习：为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加


class Student1(object):
	count = 0

	def __init__(self, name):
		self.name = name
		# 把count属性放到构造函数里面，每次创建对象时，count自增1
		Student1.count += 1


"""
	小结：
		实例属性属于各个实例所有，互不干扰；
		类属性属于类所有，所有实例共享一个属性；
		不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
"""