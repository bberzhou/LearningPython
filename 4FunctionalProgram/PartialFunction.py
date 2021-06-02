#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
# 偏函数（Partial function）要注意，这里的偏函数和数学意义上的偏函数不一样。
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
num = int('12345')
print(num)  # 12345 是字符串，默认为10进制
print(isinstance(num, int))  # True
# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
num1 = int('25', base=8)		# 这里默认25是8进制，可以通过int函数自动转换成10进制
print(num1)		# 21
num2 = int('25', base=16)
print(num2)		# 37
print('------------------')
# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，
# 于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去


def int2(x, base=2):
	return int(x, base)


print(int2('101'))		# 5
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：

int2 = functools.partial(int, base=2)
print(int2('1001'))		# 9
print(int2('1101'))		# 13
'''
	简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
	返回一个新的函数，调用这个新函数会更简单。
	注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：
'''
print(int2('23', base=10))		# 23,也可以设置为10进制

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
