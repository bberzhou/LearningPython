#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能
"""

# 多重继承举例


class Animal(object):
	# 动物类
	pass


class Mammal(Animal):
	# 继承自动物类的哺乳类
	pass


class Bird(Animal):
	# 继承自动物类的鸟类
	pass


class Runnable(object):
	def run(self):
		print('Running ... ')


class Flyable(object):
	def fly(self):
		print('flying ...')

# 对于需要Runnable功能的动物，就多继承一个Runnable
class Dog(Mammal,Runnable):
	pass


class Cat(Mammal):
	pass

# 对于需要Flyable功能的动物，就多继承一个Flyable
class Parrot(Bird,Flyable):
	pass


class Ostrich(Bird):
	pass


# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。

# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，
# 再同时继承Runnable。这种设计通常称之为MixIn。

