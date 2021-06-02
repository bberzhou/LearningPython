# -*- coding:utf-8 -*-
# python字符串和编码问题
# Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了
# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
# 单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
a = ord('A')
print(a)  # 65

b = ord('中')
print(b)  # 20013

print(chr(66))  # B

# 由于Python的字符串类型是str，
# 在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes

# Python对bytes类型的数据用带b前缀的单引号或双引号表示
x = b'ABC'
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节
print('ABC'.encode('ascii'))  # b'ABC'
print('中文'.encode('utf-8'))  # b'\xe4\xb8\xad\xe6\x96\x87'
# print('中文'.encode('ascii')) # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)65
# 这里报错是因为，纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
# 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错


# 要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))  # ABC
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中文
# 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节

# 如果bytes中包含无法解码的字节，decode()方法会报错
# b'\xe4\xb8\xad\xff'.decode('utf-8')
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')

# 要计算str包含多少个字符，可以用len()函数
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数

# %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，
# %d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。
# 如果只有一个%?，括号可以省略
print('%2d-%02d' % (3, 1))  # 3-01

print('%.2f' % 3.14)  # 3.14

print('Age: %s.Gender:%s' % (25, True))  # Age: 25.Gender:True

# 字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%

# format()
# 另外一种格式化字符串的方式是使用字符串的format()方法，他会用传入的参数依次替换字符串内的占位符{0}、{1}……，

st = 'hello, {0},成绩提升了{1:.1f}%'.format('小明', 17.25)
print(st)  # hello, 小明,成绩提升了17.2%

# f-string
# 最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius{r} is {s:.2f}')  # The area of a circle with radius2.5 is 19.62
# 上述代码中，{r}被变量r的值替换，{s:.2f}被变量s的值替换，并且:后面的.2f指定了格式化参数（即保留两位小数），因此，{s:.2f}的替换结果是19.62
