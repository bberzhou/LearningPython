#!/usr/bin/env python3
# -*- coding: utf-8 -*-# 生成器

# 一、生成器的定义：
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，


# 二、如何创建一个生成器：1）第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(1, 11)]
print(L)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 生成器,跟列表生成式不同的就是
g = (x * x for x in range(1, 11))
print(g)
# <generator object <genexpr> at 0x000002C2C1EE59E0>
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

# 怎么打印出generator的每一个元素呢？,可以使用next(g)，来依次输出，每次调用next(g)，就计算出g的下一个元素的值，
# 直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

# 遍历g 中的所有元素
# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值
print(next(g))
print('-------------')
for i in g:
    print(i)


# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100

# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到

# 1，1，2，3，5，8，13，21.。。
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易
# 斐波拉契数列

def fib(max):
    n, a, b, c = 0, 0, 0, 1
    while n < max:
        print(c)
        # a, b = b, a+b
        # 注意这里这个写法，t = (b, a+b) ，t相当于是一个元组， a = t[0]  b =t[1]
        # 也可以使用一个中间变量temp来实现
        a = b
        b = c
        c = a + c
        n = n + 1
    return 'done'


# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21


fib(8)


# 仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，
# 可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator

# 定义方式二
def fib2(max):
    n = 0
    a = 0
    b = 1
    while n < max:
        yield b
        temp = a
        a = b
        b = temp + b
        n = n + 1
    return 'done'


# 这就是定义generator的另一种方法。
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

print('______________')
print(fib2(6))  # <generator object fib2 at 0x000002A256B51890>
for n in fib2(6):
    print(n)


# <generator object fib2 at 0x000001DCE0BE6A50>
# 最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
# 再次执行时从上次返回的yield语句处继续执行


def odd():
    print('step1')
    yield 1
    print('step2')
    yield 3
    print('step3')
    yield 5


o = odd()
next(o)
# step1
next(o)
# step2
next(o)
# step3
# 调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值
# next(o)
#     next(o)
#  StopIteration
# 当没有yield可以执行的时候，如果还继续调用就会报错
# 在循环过程中不断调用yield，就会不断中断。
# 当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来

# 使用for循环来迭代输出
for n in fib2(6):
    print(n)
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib2(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generater return value:', e.value)
        break


# g: 1
# g: 1
# g: 2
# g: 3
# g: 5
# g: 8
# Generater return value: done
# generator函数的“调用”实际返回一个generator对象：


# 练习题目：通过生成器输出杨辉三角
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：
# 定义一个生成器
def triangles():
    n = 1
    L = []
    while True:
        # 下面这行代码是核心，
        L = [1 if x == 0 or x == n - 1 else L[x - 1] + L[x] for x in range(n)]
        # 增加下一行元素的个数
        n = n + 1
        # 返回一个list
        yield (L)


n = 0
res = []
for t in triangles():
    res.append(t)
    n = n + 1
    if n == 10:
        break
for t in res:
    print(t)


def trai():
    n = 1
    l = []
    while True:
        # 列表生成式
        l = [1 if x == 0 or x == n - 1 else l[x - 1] + l[x] for x in range(n)]
        n = n + 1
        yield l


print('----')
index = 0
lis = []
for i in trai():
    print(i)
    index += 1
    if index == 10:
        break

