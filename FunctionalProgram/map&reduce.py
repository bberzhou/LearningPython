#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

# Python内建了map()和reduce()函数。
# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
# map 和reduce

# 一、map接收两个参数，一个是函数，一个是Iterable(可迭代对象),
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# 例如函数f(x) = x^2


def fun(x):
    return x * x


result = map(fun, [1, 2, 3, 4, 5, 6, 7, 8])
# map()传入的第一个参数是f，即函数对象本身。结果r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让它把整个序列都计算出来并返回一个list。
print(list(result))
# [1, 4, 9, 16, 25, 36, 49, 64]
# 把f(x)作用在list的每一个元素并把结果生成一个新的list
# map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，
# 还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串

print(list(map(str, [1, 2, 3, 4, 5, 6, 7])))
# ['1', '2', '3', '4', '5', '6', '7']   # 转换成字符串

# 二、reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是:reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 比如对一个序列求和，就可以用reduce实现：


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7]))    # 16
# 输出16


# map和reduce函数结合起来使用,把字符串str转换成为int的函数

def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))  # 13579


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(list(map(char2num, '13579'))) # [1, 3, 5, 7, 9]
print(reduce(fn, map(char2num, '13579')))   # 13579，这里的13579 是数字类型





# 整理成一个str2int的转换函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]
    # 利用map和reduce将传入的字符串s转换成一个int类型的数字
    return reduce(fn, map(char2num, s))


print(str2int('2123'))  # 2123

# 还可以利用lambda表达式进一步简化成如下：
def ch2nu(s):
    return DIGITS[s]

def str2in(s):
    return reduce(lambda x, y: x*10 + y, map(ch2nu, s))

# 练习一：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：


name = ['adam', 'LISA', 'barT']


def normalize(name):
    # 利用切片操作，取第一个字符大写，后面的都是小写
    return name[:1].upper()+name[1:].lower()


print(list(map(normalize, name)))


# 练习二、Python提供的sum()函数可以接受一个list并求和，
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积
multi = [3, 5, 7, 9]


def prod(l):
    def mul(x, y):
        return x * y
    return reduce(mul, l)


print(prod(multi))


# 练习三、利用map和reduce编写一个str2float函数，
# 把字符串'123.456'转换成浮点数123.456
