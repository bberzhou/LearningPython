#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器：由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数


def now():
    print('2020-3')


f = now
f()  # 2020-3
# 函数对象有一个__name__属性，可以拿到函数的名字

print(f.__name__)  # now
print(now.__name__)  # now

# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”(Decorator)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 上面的log，因为是一个wrapper，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助Python的@语法，把decorator置于函数的定义处

# 把@log放到now1()函数的定义处，相当于执行了语句 now = log(now)
@log
def now1():
    print('2020')
# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：
now1()

# call now1():
# 2020
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
# 只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
# 写出来会更复杂。比如，要自定义log的文本
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 三层嵌套的装饰器


@log('execute')
def now2():
    print('2015')


now2()