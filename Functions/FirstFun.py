#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
# from XXXA import XXXB ，就是从XXXA引入XXXB函数

# 一、调用函数
#  python 库自带的函数，可以直接调用，参考文档 https://docs.python.org/3/library/functions.html
print(max(1, 3))
# 调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，并且Python会明确地告诉你：abs()有且仅有1个参数，但给出了两个

# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(5))


# 定义一个空函数,pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
def nop():
    pass


def my_abs1(x):
    if not isinstance(int, float, ):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x


# print(my_abs1('A')) raise TypeError('bad operand type')


# 函数返回多个返回值,Python的函数返回多值其实就是返回一个tuple，但写起来更方便

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


m, n = move(100, 100, 60, math.pi / 6)
print(m, n)
# 151.96152422706632 70.0

r = move(100, 100, 60, math.pi / 6)
print(r)


# 其实返回的是一个(151.96152422706632, 70.0)  tuple
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，
# 而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便
# 二、数据类型转换
# Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数
print(int('123'))
print(float('12.34'))
print(str(1.23))    # 这里输出是字符串：1.23

# 利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串
n1 = 255
print(hex(n1))  # 0xff


# 三、空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句
def nops():
    pass

# 四、参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError

# my_abs1(1, 2)，传入两个参数就会报错
# 数据类型检查可以用内置函数isinstance()实现


def my_abs2(x):
    # 先判断传入的类型
    if not isinstance(x, (int, float)):
        # 如果不是int或者float类型，就会报错
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


'''
    小结：
    定义函数时，需要确定函数名和参数个数；

    如果有必要，可以先对参数的数据类型做检查；

    函数体内部可以用return随时返回函数结果；

    函数执行完毕也没有return语句时，自动return None。

    函数可以同时返回多个值，但其实就是一个tuple。    
'''

'''
  请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解。
  利用求根公式
    
'''


def quadratic(a, b, c):
    delt = b**2 - 4*a*c
    if delt < 0:
        print('equation is no answer!%d'%delt)
        return ('测试失败，该方程无解')
    else:
        x1 = (-b + math.sqrt(delt))/(2*a)
        x2 = (-b - math.sqrt(delt))/(2*a)
    return x1, x2


print(quadratic(1, 3, -4))

