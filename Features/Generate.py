# -*- coding: utf-8 -*-
from collections.abc import Iterable

# 迭代器
# 可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 生成器
g = (x for x in range(1, 11))
print(g)


# <generator object <genexpr> at 0x0000019F76D06970>

# 带yiled的函数


def func():
    print('step1')
    yield 1
    print('step2')
    yield 3
    print('step5')
    yield 5


# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以使用isinstance()判断一个对象是否是Iterable对象
print(isinstance([], Iterable))
# list
print(isinstance({}, Iterable))
# dict
print(isinstance('abc', Iterable))
# str，字符串 True
print(isinstance(100, Iterable))
# False， 数字报错

# 而生成器不但可以作用于for循环，
# 还可以被next()函数不断调用并返回下一个值，
# 直到最后抛出StopIteration错误表示无法继续返回下一个值了
print(isinstance(g, Iterable))
# true ，生成器
