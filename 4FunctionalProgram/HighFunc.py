#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 高阶函数

# 一、变量可以指向函数
# 以python内置的函数abs()为例
print(abs(-10))  # 这里是函数调用
# <built-in function abs> 内置函数
print(abs)  # abs是函数本身


# 函数本身也可以赋值给变量，即：变量可以指向函数
fun = abs
print(fun(-4))


# 输出4，函数本身也可以赋值给变量，即：变量可以指向函数。

# 函数名其实就是指向函数的变量，
# 二、函数名也是变量
# abs = 10
# abs(-10)
# 把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！

# 三、传入函数，变量可以指向函数，函数的参数能接收变量，
# 那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
# 传入函数名fun


def add(x, y, f):
    return f(x) + f(y)


print(add(-2, -4, abs))
# 6 传入fun函数名，