#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

# 一、通常可变参数的求和

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 但是，如果不需要立刻求和，而是在后面的代码中，
# 根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数

def lazy_sum(*args):
    def su():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return su


# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f = lazy_sum(1, 2, 3, 5, 6)
print(f)
# 此时返回的是求和的函数 <function lazy_sum.<locals>.su at 0x107957730>

print(f())
# 17，调用时才真正计算求和的结果

# 在这个例子中，我们在函数lazy_sum中又定义了内部函数su，并且，
# 内部函数su可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数su时，相关参数和变量都保存在返回的函数中，
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力。


f1 = lazy_sum(1, 2, 3, 5, 6)
f2 = lazy_sum(1, 2, 3, 5, 6)
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
print(f1 == f2)
# False ，说明f1 和f2的调用结果互不影响
# 二、闭包（Closure）
# 注意到返回的函数在其定义内部引用了局部变量args，所以，
# 当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行
'''
    闭包的条件：
        1、在一个外函数中定义了一个内函数
        2、内函数里运用了外函数的临时变量
        3、外函数的返回值是内函数的引用
    因为：一般情况下，如果一个函数结束，函数的内部所有东西都会释放掉，还给内存，局部变量都会消失。
        但是闭包是一种特殊情况，如果外函数在结束的时候发现有自己的临时变量将来会在内部函数中用到，
        就把这个临时变量绑定给了内部函数，然后自己再结束。
'''


def counting():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        # 这里用到了外部函数counting()的局部变量fs
        fs.append(f)
    return fs
# 在这个例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了

f1, f2, f3 = counting()

print(f1())
print(f2())
print(f3())
# 9
# 9
# 9
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，
# 用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


k1, k2, k3 = count()
print(k1())
print(k2())
print(k3())
# 1
# 4
# 9

# 练习题：利用闭包返回一个计数器函数，每次调用它返回递增整数


def createCounter():
    def counter():
        return 1
    return counter


