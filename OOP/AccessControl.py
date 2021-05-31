#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	访问限制：
		要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
		在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，

	注意：
		在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
		是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
"""


class Student(object):

	def __init__(self, name, score):
		# __name，就相当于把name属性变为private了
		self.__name = name
		self.__score = score

	def print(self):
		# 	将self.name 改为 self.__name
		print('name: %s, score: %s' % (self.__name, self.__score))

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_name(self, name):
		self.__name = name

	def set_score(self, score):
		self.__score = score


bart = Student('Bart Sim', 90)
# bart.__name	这样就不能直接从外部访问实例的变量了

# 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
# 通过get方法获取属性
print(bart.get_name())  # Bart Sim
# 如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法
# 并且在方法中，可以对参数做检查，避免传入无效的参数：
bart.__name = 'da'

print(bart.get_name())
print(bart.__name)


class Student(object):
	def __init__(self, name, gender):
		self.name = name
		self.__gender = gender

	def set_gender(self, gender):
		self.__gender = gender

	def get_gender(self):
		return self.__gender


