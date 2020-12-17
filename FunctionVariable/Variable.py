# -*- coding: utf-8 -*-

# 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。
# 对于函数的调用者来说，只需要知道如何传递正确的参数，
# 以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。
# Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，
# 还可以使用默认参数、可变参数和关键字参数，
# 使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码

print(4*4)

# 计算一个数的n次方


def power(x, n):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s


print(power(3, 3))

# 默认参数


def power2(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s


print(power2(2, 2))   # 4
print(power2(2))      # 4,这里相当于默认参数就是n=2,如果次数大于2就需要显示的传入


def enroll(name, gender , age=6, city='Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age', age)
    print('city', city)


# 此时带有默认的参数age 和city
print(enroll('kath','man'))
# name: kath
# gender: man
# age 6
# city Beijing

# 此时会覆盖掉默认值
print(enroll('Jian','woman',10,'Shanghai'))
# name: Jian
# gender: woman
# age 10
# city Shanghai
# 默认参数降低了函数调用的难度，
# 而一旦需要更复杂的调用时，又可以传递更多的参数来实现。
# 无论是简单调用还是复杂调用，函数只需要定义一个。

# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。
# 比如调用enroll('Adam', 'M', city='Tianjin')，
# 意思是，city参数用传进去的值，其他默认参数继续使用默认值。


def add_end(l=[]):
    l.append('END')
    return l


print(add_end([1,2,3])) # [1, 2, 3, 'END']
print(add_end(['a','b','c'])) # ['a', 'b', 'c', 'END']

print(add_end())    # ['END']用默认参数调用时，一开始结果也是对的
print(add_end())    # ['END', 'END'] 再次调用add_end()时，结果就不对
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，
# 默认参数的内容就变了，不再是函数定义时的[]了

# None是个不变对象


def add_end1(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end1())   # ['END']
print(add_end1())   # ['END']

#  可变参数，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

# 求输入数字 a2+b2+c2+d2...的和


def sumNum(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i*i
    return sum

# 这种情况要先把传入的参数封装起来，一个list或者一个tuple
print(sumNum([1,2,3,4,5,6]))    # 91
print(sumNum((3,4,5,6)))        # 86

# 但是利用可变参数，就可以不用


def sumNum1(*numbers):
    sum =0
    for i in numbers:
        sum = sum + i*i
    return sum
print(sumNum1(1,2,3,4,5))   # 55
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，
# 因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
print(sumNum1()) # 0

# 如果当前已经有一个list或者时tuple，要调用一个可变参数
numTuple = [1,2,3]
numList = (1,2,3)
print(sumNum1(numTuple[0],numTuple[1],numTuple[2])) # 14
# 还可以在前面加一个*号
print(sumNum1(*numList))    # 14

# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict


def person(name, age, **kw):
    print('name:',name,'age:',age, 'other',kw)

person('Michael', 30)   # name: Michael age: 30 other {}
# 关键字参数有什么用？它可以扩展函数的功能。
# 比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。
# 试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，
# 其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求


