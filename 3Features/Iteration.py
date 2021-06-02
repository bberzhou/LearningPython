#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections.abc import Iterable

# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，
# 这种遍历我们称为迭代（Iteration）
# 可以看出，Python的for循环抽象程度要高于C的for循环，
# 因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上

# 迭代一个dict
d = {'a': 2, 'b': 4}
for key in d:
    print(key)

for value in d.values():
    print(value)
# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，
# 如果要同时迭代key和value，可以用for k, v in d.items()

for ch in 'ABCD':
    print(ch)

# 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，
# 而我们不太关心该对象究竟是list还是其他数据类型

# 如何判断一个对象是可迭代对象呢?
# 方法是通过collections模块的Iterable类型判断
print(isinstance('abc', Iterable))  # true
print(isinstance(123, Iterable))  # False

# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# 0 A
# 1 B
# 2 C

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 1 1
# 2 4
# 3 9


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple

li = [1, 5, 7, 9, 8, 3]
lis = []


def findminandmax(L):
    if L == []:
        return (None, None)
    else:
        max1 = min1 = L[0]
        for i in L:
            if i < min1:
                min1 = i
            if i > max1:
                max1 = i
        return (min1, max1)


print(findminandmax(li))  # (1, 9)
print(findminandmax(lis))  # (None, None)
