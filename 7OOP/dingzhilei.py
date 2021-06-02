#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
	Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类
"""

# 一、__str__


class Student(object):

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object (name: %s)' % self.name
	# 这里省略写法,因为这两个函数内容相同，所以直接赋值给__repr__
	__repr__ = __str__


print(Student('Michael'))
# 如果没有__str__，输出结果为：<__main__.Student object at 0x0000018A27E28250>
# 在Student类里面添加__str__ 方法，输出： Student object (name: Michael)，类似toString()方法

# 直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
# 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，


# 二、__iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。


# 以斐波那契数列为例，写一个Fib类，可以作用于for循环：


class Fib(object):

	def __init__(self):
		self.a, self.b = 0, 1  # 初始化两个计数器a,b

	def __iter__(self):
		return self  # 实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a, self.b = self.b, self.a+self.b  # 计算下一个值
		if self.a > 1000:  # 退出循环的条件
			raise StopIteration()
		return self.a  # 返回下一个值

	# 实现了这个方法之后，就可以按照下标访问数列得任意一项了
	# 进一步，list可以进行切片操作
	# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断
	def __getitem__(self, item):
		if isinstance(item, int):  # item是索引
			a, b = 1, 1
			for x in range(item):
				a, b = b, a+b
			return a
		if isinstance(item, slice):  # item 是切片
			start = item.start
			stop = item.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a+b
			return L



# 测试Fib类的实例
for n in Fib():
	print(n)



# 三、 __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行
# 比如，取第5个元素：
# Fib()[5]
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
f = Fib()
print(f[0])	 # 1
print(f[3])  # 3

# 进一步，list可以进行切片操作
# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断
# 对__getitem__()方法修改之后，再测试切片操作
f = Fib()
print(f[0:5])  # [1, 1, 2, 3, 5]

print(f[0, 100])
# 这个没有对step参数做处理， 也没有对负数作处理，

