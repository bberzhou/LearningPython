#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import StringIO, BytesIO
"""
	字符流和字节流：
		1、数据读写不一定是文件，也可以在内存中读写
		2、StringIO顾名思义就是在内存中读写str，要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可
		3、要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取 ，f = StringIO("Hi\nHello world")
		
	ByteIO：
		1、StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
		2、BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
	
	StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口	
		
"""
f = StringIO()
f.write('hello')
print(f.getvalue())  # 写入到内存中，getvalue()方法读取出来，hello


f = StringIO("Hi\nHello world")
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())

# Hi
# Hello world


# 字节流
b = BytesIO()
# 这里写入的不是str，而是经过UTF-8编码的bytes
b.write('中文'.encode('utf-8'))
print(b.getvalue())  # b'\xe4\xb8\xad\xe6\x96\x87'，这里用三个字节表示一个汉字
# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取
b1 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(b1.read())  # b'\xe4\xb8\xad\xe6\x96\x87'