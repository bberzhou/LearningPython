#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	获取对象信息：
		当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
"""

# 方法一： 使用type()

# 首先，我们来判断对象类型，使用type()函数
import types

print(type(123))  # <class 'int'>
print(type('dsd'))  # <class 'str'>

# 如果一个变量指向函数或者类，也可以用type()判断：
print(type(abs))  # <class 'builtin_function_or_method'>


# 注意：判断基本数据类型可以直接写int，str等，
# 但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量

def fn():
	pass


print(type(fn) == types.FunctionType)  # True


# 方法二：使用instance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。


class Animal(object):

	def runs(self):
		print('animal is running...')


a = Animal()

print(isinstance(a, Animal))  # True
# 能用type()判断的基本类型也可以用isinstance()判断
# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：

print(isinstance([1, 2, 3], (list, tuple)))


# 方法三：使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，
# 它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))
# ['__add__', '__class__', '__contains__', '__delattr__', '_
# _dir__', '__doc__', '__eq__', '__format__', '__ge__', '__
# getattribute__', '__getitem__', '__getnewargs__', '__
# gt__', '__hash__', '__init__', '__init_subclass__', '__
# iter__', '__le__', '__len__', '__lt__', '__mod__', '__
# mul__', '__ne__', '__new__', '__reduce__', '__
# reduce_ex__', '__repr__', '__rmod__', '__rmul__', '_
# _setattr__', '__sizeof__', '__str__', '__subclasshook_
# _', 'capitalize', 'casefold', 'center', 'count',
# 'encode', 'endswith', 'expandtabs', 'find',
# 'format', 'format_map', 'index', 'isalnum',
# 'isalpha', 'isascii', 'isdecimal', 'isdigit',
# 'isidentifier', 'islower', 'isnumeric',
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust',
# 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind',
# 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
# 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print(len('ABC'))  # 3
print('ABC'.__len__())  # 3


# 对于自定义的类，如果也想用len(myObj)的话，就自己写一个__len__()方法


class MyDog(object):

	def __len__(self):
		return 100

	def __init__(self):
		self.x = 9

	def power(self):
		return self.x * self.x


dog = MyDog()
print(len(dog))	 # 100

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

# 创建一个MyDog的实例obj
obj = MyDog()
# 对象是否有属性 x
print(hasattr(obj, 'x'))  # True
# 对象是否有属性 y
print(hasattr(obj, 'y'))   # False

# 给对象设置属性：setattr() 方法，传入三个参数，要设置的对象, 属性名，属性值
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))	 # True

# 获取属性值：getattr() 方法，传入参数：obj:获取属性的对象，‘y’：属性名， 第三个是可选的默认属性值，防止报错

print(getattr(obj, 'y'))  # 19

# 如果没有该属性值，默认404
print(getattr(obj, 'm', 404))  # 404,获取属性'm'，如果不存在，返回默认值404

# 也可以获得对象的方法：

print(hasattr(obj, 'power'))  # True,  # 有属性'power'吗？

# 获取属性'power'
print(getattr(obj, 'power'))  # <bound method MyDog.power of <__main__.MyDog object at 0x000001A2216D2F10>>






