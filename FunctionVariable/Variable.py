# -*- coding: utf-8 -*-

# 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。
# 对于函数的调用者来说，只需要知道如何传递正确的参数，
# 以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。
# Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，
# 还可以使用默认参数、可变参数和关键字参数，
# 使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码

print(4 * 4)


# 计算一个数的n次方


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(3, 3))


# 默认参数


def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power2(2, 2))  # 4
print(power2(2))  # 4,这里相当于默认参数就是n=2,如果次数大于2就需要显示的传入一个参数


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age', age)
    print('city', city)


# 此时带有默认的参数age 和city
print(enroll('kath', 'man'))
# name: kath
# gender: man
# age 6
# city Beijing

# 此时会覆盖掉默认值
print(enroll('Jian', 'woman', 10, 'Shanghai'))


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


print(add_end([1, 2, 3]))  # [1, 2, 3, 'END']
print(add_end(['a', 'b', 'c']))  # ['a', 'b', 'c', 'END']

print(add_end())  # ['END']用默认参数调用时，一开始结果也是对的
print(add_end())  # ['END', 'END'] 再次调用add_end()时，结果就不对


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


print(add_end1())  # ['END']
print(add_end1())  # ['END']


#  可变参数，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

# 求输入数字 a2+b2+c2+d2...的和


def sumNum(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i * i
    return sum


# 这种情况要先把传入的参数封装起来，一个list或者一个tuple
print(sumNum([1, 2, 3, 4, 5, 6]))  # 91 传入一个list，可变的
print(sumNum((3, 4, 5, 6)))  # 86   传入一个tuple 元组一旦初始化就不可变


# 但是利用可变参数，就可以不用


def sumNum1(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i * i
    return sum


print(sumNum1(1, 2, 3, 4, 5))  # 55
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，
# 因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
print(sumNum1())  # 0

# 如果当前已经有一个list或者时tuple，要调用一个可变参数
numTuple = [1, 2, 3]  # list
numList = (1, 2, 3)  # tuple
print(sumNum1(numTuple[0], numTuple[1], numTuple[2]))  # 14
# 还可以在前面加一个*号
print(sumNum1(*numList))  # 14
print(sumNum1(*numTuple))
print('_________________________________________')


# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict，字典


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other', kw)


person('Michael', 30)  # name: Michael age: 30 other {}
person('Jack', 60, city='Beijing')  # name: Jack age: 60 other {'city': 'Beijing'}
person('Ada', 79, gender='M', job='Engineer')  # name: Ada age: 79 other {'gender': 'M', 'job': 'Engineer'}

# 关键字参数有什么用？它可以扩展函数的功能。
# 比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。
# 试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，
# 其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict字典转换为关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Ming', 45, city=extra['city'], job=extra['job'])
# name: Ming age: 45 other {'city': 'Beijing', 'job': 'Engineer'}
# 这种写法也可以简化
person('Jackson', 24, **extra)  # name: Jackson age: 24 other {'city': 'Beijing', 'job': 'Engineer'}


# **extra 这种写法表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

# 命名关键字参数，对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数，
# 至于传入了哪些，就需要在函数内部通过kw来进行检查，但是调用者仍可以传入不受限制的关键字参数：


def per(name, age, **kw):
    if 'city' in kw:
        # here，如果有某某参数的话，就可以在这里做一些操作
        print('here')
        pass
    if 'job' in kw:
        pass
    print('name：', name, 'age：', age, 'other：', kw)


per('jack', 25, city='Shanghai', addr='Beijing', zipcode=145454)


# name： jack age： 25 other： {'city': 'Shanghai', 'addr': 'Beijing', 'zipcode': 145454}

# 命名关键字参数，如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数

def person1(name, age, *, city, job):
    print(name, age, city, job)


person1('Jean', 26, city='Nanjing', job='engineer')  # Jean 26 Nanjing engineer


# person1('Kang', 89)
# 这里如果不传入关键字参数的值，就会报错
# TypeError: person1() missing 2 required keyword-only arguments: 'city' and 'job'
# 如果在函数中已经定义了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊的分割符*了


def person2(name, age, *city, job, address):
    print(name, age, city, job, address)


# person2('Lili', 23, 'Chongqing', 'Beijing','HongKong', )
# 报错 TypeError: person2() missing 1 required keyword-only argument: 'job'
person2('Lili', 80, 'Chongqing', job='engineer', address='Hongkong')  # Lili 80 ('Chongqing',) engineer


# 命名关键字参数可以有缺省值，从而可以简化调用
def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person3('Kobe', 34, job='Software')  # Kobe 34 Beijing Software 有默认值city


# 由于命名关键字参数city具有默认值，调用时，可不传入city参数
# 在命名关键字参数的时候，要特别注意，如果没有可变参数，就必须加一个* 作为特殊分隔符，
# 如果缺少* Python解释器将无法识别位置参数和命名关键字参数


def sum3(*number):
    sum = 0
    for i in number:
        sum = sum + i * i
    return sum


print(sum3(1, 2, 3, 4))  # 30
sumTuple1 = (1, 2, 3, 4)
print(sum3(*sumTuple1))  # 30
print(sum3(sumTuple1[0], sumTuple1[1], sumTuple1[2], sumTuple1[3]))  # 30


# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


# 关键字参数
def keyword(name, **kw):
    print(name, 'other', kw)


keyword('Trump', phone=14334, car='BMW')


# Trump other {'phone': 14334, 'car': 'BMW'}

# 命名关键字

def keyword1(name, *, city, add):
    print(name, city, add)


keyword1('Wang', city='Chongqing',add='Jiangbei')
# Wang Chongqing Jiangbei


print('----------------------------------------------------------------')
# 参数组合,一个函数里面有多个参数


def func1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b,  'c=',c, 'args=', args, 'kw=', kw)


func1(1, 2)
# a= 1 b= 2 c= 0 args= () kw= {}
func1(2, 4, 5)
# a= 2 b= 4 c= 5 args= () kw= {}
func1(3, 6, 8, 'mm', 'ooo')
# a= 3 b= 6 c= 8 args= ('mm', 'ooo') kw= {}
func1(3, 6, 8, 'mm', 'ppp', key='Music')
# a= 3 b= 6 c= 8 args= ('mm', 'ppp') kw= {'key': 'Music'}
# 通过一个tuple和dict，你也可以调用上述函数：
argument = (1, 2, 3, 4, 5)  # tuple
key = {'d':99, 'X':'dd'}    # list
func1(3,8,9,*argument,**key)
# a= 3 b= 8 c= 9 args= (1, 2, 3, 4, 5) kw= {'d': 99, 'X': 'dd'}
# 并且在调用的时候还有一个问题
func1(*argument,**key)
# 输出结果：a= 1 b= 2 c= 3 args= (4, 5) kw= {'d': 99, 'X': 'dd'}


def product(x, *y):
    su = 1
    if y is None:
        return x*1
    else:
        for i in y:
            su = su * i

        return su * x


num = (5, 6)
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

# 总结：默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#   要注意定义可变参数和关键字参数的语法：
#       *args是可变参数，args接收的是一个tuple；
#       **kw是关键字参数，kw接收的是一个dict。
#
#   调用函数时如何传入可变参数和关键字参数的语法：
#       可变参数既可以直接传入：func(1, 2, 3)，
#       又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#       关键字参数既可以直接传入：func(a=1, b=2)，
#       又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。



