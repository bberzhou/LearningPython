#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内建的filter()函数用于过滤序列
# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把 留还是丢弃该元素。

# 例如，在一个list中，删掉偶数，只保留奇数

def is_odd(n):
    # 返回值围true保留该值，是false舍弃该值
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10])))


# filter()函数返回的是一个Iterator，也就是一个惰性序列，
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回lis

# 把一个序列中的空字符串删除
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None])))


# ['A', 'B'],过滤出空的
# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

# 三、用filter求素数，
# 计算素数的一个方法就是埃氏筛法，

# 先定义一个从3开始的奇数序列，并且是一个无限序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        # 带有yield的函数在Python中称之为generator（生成器），print n，next一次，返回一次n的值
        yield n


# 定义一个筛选函数
def _not_divisible(n):
    # 返回
    return lambda x: x % n > 0


# 最后定义一个生成器，不断返回下一个素数
def primes():
    # 初始的时候返回2
    yield 2
    # 初始化序列
    it = _odd_iter()
    while True:
        # 返回序列的第一个数
        n = next(it)
        # 输出每一个n
        yield n
        # 构造新的序列，过滤掉能够整除的
        it = filter(_not_divisible(n), it)


# 这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。

# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件
for n in primes():
    if n < 100:
        print(n)
    else:
        break


# 练习：回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数


def is_palindrome(n):
    # 先转换为字符串
    n = str(n)
    # n[::-1]，对字符串反转，然后判断是否相等，相等则返回
    return n ==n[::-1]
# 利用上面的过滤函数，同时配合filter

print(list(filter(is_palindrome, range(1,100))))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]


# def is_palindrome(n):
#     # 转换为字符串
#     n = str(n)
#     # 判断一位的时候都是int(n)
#     if len(n) == 1:
#         return int(n)
#     else:
#         for i in range(len(n)):
#             i = i + 1
#             # 首位末尾或者倒数第二位正数第二位不同返回False，否则返回int(n)
#             if n[i - 1] != n[-i]:
#                 return False
#             else:
#                 return int(n)
