#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# 列表生成式，即是List即List Comprehensions，
# 是Python内置的非常简单却强大的可以用来创建list的生成式
# 快速生成一个list
print(list(range(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？

L = []
for i in range(1, 11):
    L.append(i * i)

print(L)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list


print([x*x for x in range(1, 11)])
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 列表生成式一行语句代替循环
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，
# 就可以把list创建出来，并且还可以在for循环后面加上判断

print([x * x for x in range(1, 11) if x % 2 != 0])
# [1, 9, 25, 49, 81]，筛选出仅奇数的平方

# 还可以使用两层循环，可以生成全排列
print([m + n for m in 'ABCD' for n in 'HDJD'])
# 生成一个全排列['AH', 'AD', 'AJ', 'AD', 'BH', 'BD', 'BJ', 'BD', 'CH', 'CD', 'CJ', 'CD', 'DH', 'DD', 'DJ', 'DD']

# 运用列表生成式，可以写出非常简洁的代码。
# 例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
print([name for name in os.listdir('.')])
# ['aList.py', 'Iteration.py', 'ListComprehensions.py', '__init__.py']，当前文件夹下面的所有文件，是一个list

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for key, value in d.items():
    print(key, '=', value)
for kes in d.keys():
    print(kes)
# 其实相当于把dict里面的键值对都进行了遍历

# x = A
# y = B
# z = C

# 列表生成式也可以使用两个变量来生成lis
d1 = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d1.items()])
# ['x=A', 'y=B', 'z=C']
# 这里相当于把dict 的键值两个变量组合生成一个新的list

# 最后把一个list中所有的字符串变成小写：
L2 = ['A', 'C', 'F', 'R']
print([s.lower() for s in L2])
# ['a', 'c', 'f', 'r'],调用 lower函数


ch = 'a'
ch1 = ch.upper()
print(ch1)  # A

# 使用列表生成式的时候，if...else的用法
print([x for x in range(1, 11) if x % 2 == 0])
# [2, 4, 6, 8, 10]，筛选出偶数,但是，我们不能在最后的if加上else
# 这是因为跟在for后面的if是一个筛选条件，不能带else


# 但是如果if写在for前面必须加else，否则报错
# 这是因为for前面的部分是一个表达式，它必须根据x计算出一个结果。
# 因此，考察表达式：x if x % 2 == 0，它无法根据x计算出结果，因为缺少else，必须加上else
print([x if x % 2 == 0 else -x for x in range(1, 11)])
# [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],奇数变为-x,偶数不变
# for前面的表达式x if x % 2 == 0 else -x才能根据x计算出确定的结果。
# 可见，在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else


# 练习题目：
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行

L = ['Hello', 'World', 19, 'Apple']
# print([s.lower() for s in L ])
# AttributeError: 'int' object has no attribute 'lower'
# 使用内建的isinstance函数可以判断一个变量是不是字符串
print([x.lower() for x in L if isinstance(x, str)])
# ['hello', 'world', 'apple']
L2 = ['Hello', 'World', 19, 'Apple']
print([x.lower() if isinstance(x, str) else x for x in L2])
# ['hello', 'world', 19, 'apple']

L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() if isinstance(s, str) else s for s in L])

# 使用内建的isinstance函数可以判断一个变量是不是字符串
x = 'abd'
y = 132
print(isinstance(x, str))   # True
print(isinstance(y, str))   # False
