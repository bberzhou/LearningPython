#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 一、函数的参数
# 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。
# Python的函数定义非常简单，但灵活度却非常大。
# 除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，
# 使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

# 二、位置参数
def power(x):
    return x * x


# 对于power(x)函数，参数x就是一个位置参数
# 当我们调用power函数时，必须传入有且仅有的一个参数x

# 计算x的n次方


def powerN(x, n):
    result = 1
    while n > 0:
        n = n - 1
        result = result * x
    return result


print(powerN(5, 4))  # 625


# power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n
# 一个函数在内部调用自身本身，这个函数就是递归函数。
# 典型的计算阶乘的函数


# 三、默认参数
def powerN1(x, n=2):
    result = 1
    while n > 0:
        result = result * x
        n = n - 1
    return result


print(powerN1(4, 3))  # 64
# 设置一个默认值n
print(powerN1(3))
# 9，这里即使传入的只有一个参数，但是有一个默认参数n，但是对于n大于2的情况，必须明确地传入n
'''
    默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
    一是必选参数在前，默认参数在后，否则Python的解释器会报错.
    二是如何设置默认参数。当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数
    
'''


def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)


def enroll1(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


# 比较这两个函数，第二个就设置了两个默认参数值,只有与默认参数不符合的学术才需要提供额外的信息
# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，也可以不按顺序提供部分默认参数。
# 当不按顺序提供部分默认参数时，需要把参数名写上。


enroll1('Bob', 'M', 7)
enroll1('Adam', 'M', city='Shanghai')  # age就是默认的参数，而city是新的


# 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：

def add_end(L=[]):
    L.append('END')
    return L


# 正常调用
print(add_end([1, 2, 3]))  # [1, 2, 3, 'END']

# 当使用默认参数调用的时候，开始也是正常的

print(add_end())  # ['END']

# 再次调用就会出现问题
print(add_end())  # ['END', 'END']


# 默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，
# 它指向对象[]，每次调用该函数，如果改变了L的内容，
# 则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
# 所以要注意一点：定义默认参数要牢记一点：默认参数必须指向不变对象！

# 对于上面这个例子，可以使用None这个不变对象来实现


def add_end1(L=None):
    # 先判断L是否为None
    if L is None:
        # 如果未传入参数，就将L置为[]，然后再添加一个'END'
        L = []

    # 如果L不为[]，直接添加
    L.append('END')
    return L


print(add_end1())  # ['END']  默认参数为None
print(add_end1())  # ['END']
print(add_end1([1, 2, 3]))  # [1, 2, 3, 'END']


# 四、可变参数
# 在Python函数中，还可以定义可变参数。
# 以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……


def calc(numbers):
    sum1 = 0
    for n in numbers:
        sum1 = sum1 + n * n
    return sum1


# 调用的时候，需要先组装成一个list或tuple


print(calc([1, 2, 3]))  # 14
print(calc((1, 3, 7)))  # 59


# 改为可变参数的形式，在括号内加入一个 *numbers


def calc1(*numbers):
    sum1 = 0
    for n in numbers:
        sum1 = sum1 + n * n
    return sum1


# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple
# 调用该函数时，可以传入任意个参数，包括0个参数


print(calc1(1, 2, 3))  # 14

# 如果现在有一个list或者tuple，要调用一个可变参数怎么办？可以这样做
nums = [1, 2, 3]
print(calc1(nums[0], nums[1], nums[2]))
# 这种写法比较繁琐，需要一个一个读取，
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums1 = (1, 2, 3)
print(calc1(*nums1))  # *nums1就把tuple转换成为可变参数传进去


# 五、关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，
# 这些关键字参数在函数内部自动组装为一个dict


def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'other: ', kw)


# 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数


print(person('michael', 30))  # name:  michael age:  30 other:  {}
# 也可以传入任意个数的关键字参数：
print(person('Bob', 35, gender='M', job='Engineer'))
# 输出结果：name:  Bob age:  35 other:  {'gender': 'M', 'job': 'Engineer'}
# 关键字参数的作用：它可以扩展函数的功能
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去

di = {'city': 'LA', 'job': 'player'}
print(person('test', 25, city=di['city'], job=di['job']))
print(person('kang', 18, **di))


# **di,表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


# 六、命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
# 至于到底传入了哪些，就需要在函数内部通过kw检查

# 仍以上面的person()函数为例，我们希望检查是否有city和job参数


def person1(name, age, **kw):
    if 'city' in kw:
        # 有City参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age: ', age, 'other: ', kw)


# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
def person3(name, age, *, city, job):
    print(name, age, city, job)


# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数


# 调用方式
print(person3('jack', 39, city='chongqing', job='pp'))


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# *args就是可变参数

def person4(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
print(person4('Li', 30, 233, 42, 33, city='Nanjing', job='player'))


# Li 30 (233, 42, 33) Nanjing player

# 命名关键字参数可以有缺省值，从而简化调用：


def person5(name, age, *, city='Beijing', job):
    print(name, age, city, job)


#     由于命名关键字参数city具有默认值，调用时，可不传入city参数
print(person5('person5', 30, job='son'))


def f1(a, b, c=0, *args, k, **kw):
    print('a:', a, 'b:', b, 'c:', c, 'args:', args, 'k:', k, 'kw:', kw)


# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
# 如果缺少*，Python解释器将无法识别位置参数和命名关键字参数


# 七、参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：
# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def f2(a, b, c=0, *, k, **kw):
    print('a:', a, 'b:', b, 'c:', c, 'k:', k, 'kw:', kw)


print(f1(1, 2, 3, 1, 2, 3, k='40', kk='kw'))

# 测试
# a: 1 b: 2 c: 3 args: (1, 2, 3) k: 40 kw: {'kk': 'kw'}
args = (1, 2, 3, 4)

# 通过一个tuple和dict，你也可以调用上述函数：
kw = {'k': 'ding', 'city': 'Beijing', 'job': 'player'}
print(f1(*args, **kw))


# a: 1 b: 2 c: 3 args: (4,) k: ding kw: {'city': 'Beijing', 'job': 'player'}
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：

def mul(x, *y):
    result = x
    if len(y) == 0:
        return result
    elif len(y) > 0:
        for i in y:
            result = result * i

    return result


print(mul(5))
print(mul(5, 6, 7, 9))


# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(4))
# 递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰
# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，
# 所以，递归调用的次数过多，会导致栈溢出。
# print(fact(1000))
# maximum recursion depth exceeded in comparison
print(fact(100))


# 解决递归调用时栈溢出的方法就是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的
# 尾递归是指，在函数返回的时候，调用自身，并且return语句不能包含表达式，
# 编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。


# 尾递归的方式实现，主要是要把每一步的乘积传入到递归函数中


def func1(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# 可以看到 return fact_iter(num-1, num * product)仅返回递归函数本身，
# num - 1和num * product在函数调用前就会被计算，不影响函数调用。
# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出


print(func1(5))


# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
# 大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

# 汉诺塔游戏练习，请编写move(n, a, b, c)函数，它接收参数n，
# 表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法

def fci(n):
    if n == 1:
        return 1
    return n*fci(n-1)


print(fci(4))


# 尾递归优化
def fc1(n):
    return fc1_iter(n, 1)


def fc1_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num*product)


print(fci(4))
