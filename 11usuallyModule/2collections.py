#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple, deque, defaultdict, OrderedDict,Counter
"""
	1、collections是Python内建的一个集合模块，提供了许多有用的集合类
		# namedtuple是一个函数，它用来创建一个自定义的tuple对象，
		并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素，
		这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用
"""
# 一、namedtuple


# tuple可以表示不变集合,例如，一个点的二维坐标就可以表示成
p = (1, 2)
# 但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的
Point = namedtuple('Point', ['x', 'y'])
point = Point(1, 2)
print(point.x, point.y)  # 1 2
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用
print(isinstance(point, Point))  # True
# Returns a new subclass of tuple with named fields.
print(isinstance(point, tuple))  # True
# 可以看出Point是tuple的一种子类,因为Point的实例也是tuple类型的实例
# 类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义
Circle = namedtuple('Circle', ['x', 'y', 'r'])
circle = Circle(3, 4, 1.0)
print(circle.x, circle.y, circle.r)  # 跟普通tuple不同的是，可以使用属性的方式来访问某个元素，不需要使用下标


# 二、deque

# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
# 因为list是线性存储，数据量大的时候，插入和删除效率很低。

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
# 定义一个双向列表，传入的是一个list
q = deque(['a', 'b', 'c'])
# 插入两个元素
q.append('x')
q.appendleft('y')
# deque(['y', 'a', 'b', 'c', 'x'])，输出
print(q)

print(isinstance([1, 2, 3], list))
print(isinstance((1, 2, 3), tuple))
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素


# 三、defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])  # abc
print(dd['key2'])  # N/A
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的


# 四、OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序
# 如果要保持Key的顺序，可以用OrderedDict


d = dict([('a', 1), ('b', 2), ('c', 4), ('d', 7)])
d1 = {'a': 1, 'b': 2, 'c': 4, 'd': 7}
for key, value in d1.items():
	print(key, value)
# a 1
# b 2
# c 4
# d 7
print(d)
od = OrderedDict()
od['x'] = 1
od['y'] = 3
od['m'] = 2
print(list(od.keys()))  # ['x', 'y', 'm']

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key


class LastUpdatedOrderedDict(OrderedDict):
	def __init__(self, capacity):
		super(LastUpdatedOrderedDict, self).__init__()
		self._capacity = capacity

	def __setitem__(self, key, value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False)
			print('remove:', last)
		if containsKey:
			del self[key]
			print('set:', (key, value))
		else:
			print('add:', (key, value))
		OrderedDict.__setitem__(self, key, value)


# 五、ChainMap
# ChainMap可以把一组dict串起来并组成一个逻辑上的dict。
# ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。


# 六、Counter是一个简单的计数器，例如，统计字符出现的个数

c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1

print(c)
# Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
# Counter实际上也是dict的一个子类，上面的结果可以看出每个字符出现的次数

