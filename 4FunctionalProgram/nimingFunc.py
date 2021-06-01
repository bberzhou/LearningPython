#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
一、匿名函数
  在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便
'''
# 在Python中，对匿名函数提供了有限支持。还是以map()函数为例，
# 计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数
print(list(map(lambda x: x*x, [1, 2, 3, 4, 5, 6])))
# [1, 4, 9, 16, 25, 36],map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

# lambda x: x*x 实际上就是,关键字lambda表示匿名函数，冒号前面的x表示函数参数,等同于下面的这个函数
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
def f(x):
    return x*x
# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x*x
print(f(4))  # 16

# 同样，也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x*x + y*y

L = list(filter(lambda n: n%2 ==1,range(1, 20) ))