#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改

	s = Student()
	s.score = 9999这显然不合逻辑。
	为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，
	这样，在set_score()方法里，就可以检查参数：
"""


# class Student(object):
#
# 	# def __init__(self,score):
# 	# 	self.score = score
#
# 	def get_score(self):
# 		return self.score
#
# 	def set_score(self, value):
# 		if not isinstance(value, int):
# 			raise ValueError('score must be an integer!')
# 		if value < 0 or value > 100:
# 			raise ValueError('score must be between 0~100')
# 		self.score = value
#
#
# # 对任意的Student实例进行操作，就不能随心所欲地设置score了
# s = Student()
# s.set_score(60)
# print(s.get_score())  # 60

# s.set_score(1000)  # ValueError: score must be between 0~100

# 上面的方法略为复杂，有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
# Python内置的@property装饰器就是负责把一个方法变成属性调用的


class Student1(object):
	# 用装饰器来进行修改,把一个getter方法变成属性，只需要加上@property就可以了
	@property
	def score(self):
		return self.score

	# @property本身又创建了另一个装饰器 @ score.setter负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must be between 0~100')
		self.score = value


s3 = Student1()
s3.score = 60   # OK，实际转化为s.set_score(60)






