#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 字符编码
# 字符0用ASCII编码是十进制的48，二进制的00110000
# 又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。
# UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，
# 常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。


# python的字符串
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，
# chr()函数把编码转换为对应的字符
print(ord('A'))  # 65

print(chr(66))  # B

# 如果知道字符的整数编码，还可以用十六进制这么写str
print('\u4e2d\u6587')  # 中文
# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
# Python对bytes类型的数据用带b前缀的单引号或双引号表示
str = 'ABC'.encode('ascii')
print(str)  # b'ABC'
str2 = '中文'.encode('utf-8')
print(str2)     # b'\xe4\xb8\xad\xe6\x96\x87',utf-8三个字节表示一个中文字符
# 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

# str3 = '中文'.encode('ascii')
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
# 要把bytes变为str，就需要用decode()方法

str4 = b'ABC'.decode('ascii')
print(str4)     # ABC
str5 = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(str5)     # 中文
# 如果bytes中包含无法解码的字节，decode()方法会报错
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节

str6 = b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print(str6)

length = len('大家好，我是渣渣辉')
print(length)
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数

# 格式化输出字符串，在Python中，采用的格式化方式和C语言是一致的，用%实现
# %d 整数，  %f  浮点数, %s  字符串,%x   十六进制整数。
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
str7 = 'hello,%s' % 'world'
print(str7)    # hello,world
str8 = 'Hi,%s, you have $%d.' % ('Michael', 1000)
print(str8)  # Hi,Michael, you have $1000.

print('%03d-%02d' % (3, 1)) # 前面补0，003-01
print('%.2f' % 3.1415)      # 3.14
print('Age: %s. Gender: %s' % (25, True))   # Age: 25. Gender: True

# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print('growth rate: %d%%' % 7)     # growth rate: 7 % 有百分号的时候

# format()函数，另一种格式化字符串的方法是使用字符串的format()方法，
# 它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多;{1:.2f}指明保留的小数位数
print('hello, {0}, 成绩提升了{1:.2f}%'.format('小明', 23.221)) # hello, 小明, 成绩提升了23.22%


# 最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，
# 它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换.

r = 2.5
s = 3.14 * r ** 2
print(f'The area of circle with radius{r} is {s:.2f}')  # The area of circle with radius2.5 is 19.62
# {r} is replaced by r, and  {s:.2f} is replaced by s

'''
练习题目：小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，
并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
'''
score1 = 72
score2 = 85
rate = (score2 - score1) / score1
# 以% 形式格式化
print('%.1f%%' % rate)
# 以format()格式进行
print('{0:.1f}%'.format(rate))
# 使用f-string的方式，以f开头，对{}里面的内容进行替换
print(f'{rate:.1f}%')

# 0.2%
# 0.2%
# 0.2%
