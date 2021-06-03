#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

"""
	错误处理：
		在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，
		以及出错的原因。在操作系统提供的调用中，返回错误码非常常见。
		比如打开文件的函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1
"""

# 一、try...except...finally
"""
	try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
"""


# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，
# 而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕

# Python的错误其实也是class，所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽


# 二、调用栈
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看err.py


# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     bar('0')
#
#
# main()


# 记录错误
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
# 既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。


# def foo(s):
# 	return 10 / int(s)
#
#
# def bar(s):
# 	return foo(s) * 2
#
#
# def main():
# 	try:
# 		bar('0')
# 	except Exception as e:
# 		logging.exception(e)
#
#
# main()
# print('END')  # END
# 通过日志文件打印出：ERROR:root:division by zero
# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。

# 三、抛出错误
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。
# Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误


class FooError(ValueError):
	pass


# def foo(s):
# 	n = int(s)
# 	if n == 0:
# 		raise FooError('invalid value: %s' % s)
# 	return 10 / n
#
#
# foo('0')
# __main__.FooError: invalid value: 0

# 只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），
# 尽量使用Python内置的错误类型。


def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise  # raise语句如果不带参数，就会把当前错误原样抛出。

bar()