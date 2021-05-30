#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections.abc import Iterator, Iterable

# 迭代器
# 可以直接作用于for循环的数据类型有以下几种：
# 一是：集合数据类型，如list、tuple、dict、set、str等；
# 二是：generator，包括生成器和带yield的generator function。
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


def triangle():
    n = 1
    lis = []
    while True:
        lis = (1 if x == 1 or x == n-1 else lis[x-1] + lis[x]for x in range(n))
        n = n+1
        yield lis
# 可迭代对象：可以直接作用于for循环的对象统称为可迭代对象：Iterable
#           可以使用isinstance()判断一个对象是否是Iterable对象
print(isinstance([], Iterable))
# list
print(isinstance({}, Iterable))
# dict
print(isinstance('abc', Iterable))
# str，字符串 True
print(isinstance(100, Iterable))
# False， 数字报错

# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
# 直到最后抛出StopIteration错误表示无法继续返回下一个值了
print(isinstance(g, Iterable))
# true ，生成器
print('------------------------')
# 迭代器：可以被next()函数调用并不断返回下一个值的对象称为迭代器
#        可以使用isinstance()判断一个对象是否是Iterator对象
print(isinstance([], Iterator))     # False
print(isinstance((x for x in range(10)), Iterator)) # True
print(isinstance(('ABC'), Iterator))    # False
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数

lis = [1, 2, 3]
print(isinstance(iter(lis), Iterator))  # True

'''
    小结：
     凡是可作用于for循环的对象都是Iterable类型；   
     凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
     集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
'''
# Python的for循环本质上就是通过不断调用next()函数实现的
for x in [1, 2, 3, 4]:
    pass

# 等价于
it = iter([1, 2, 3, 4])
while True:
    try:
        # 获取下一个值
        x = next(it)
    except StopIteration:
        # 如果遇到StopIteration，就推出循环
        break
