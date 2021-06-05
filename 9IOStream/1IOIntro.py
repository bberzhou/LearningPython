#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	IO流操作：
		IO在计算机中指Input/Output，也就是输入和输出。
		IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动。
		Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。
		由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配的问题

		第一种是CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行，这种模式称为同步IO
		另一种方法是CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，于是，后续代码可以立刻接着执行，这种模式称为异步IO。

		同步和异步的区别就在于是否等待IO执行的结果。

		异步IO的复杂度远远高于同步IO。

	pythonIO操作：
		读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。
		读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
		所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），
		或者把数据写入这个文件对象（写文件）。

	读文件：
		方法：要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符
			f = open('/Users/michael/test.txt', 'r')，标示符'r'表示读，这样，我们就成功地打开了一个文件。
		结果１：如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：
		结果２：如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，
				Python把内容读到内存，用一个str对象表示：


	二进制文件：
		要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

	字符编码：
		1、要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件,
		2、遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
			遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：


	写文件：
		1、写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
		2、可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。
			当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
			只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
			忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险
"""
# f = open("C:\\Users\\Zhouz\\Desktop\\test.txt", 'r')  # 标示符'r'表示读
# # 文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
#
# st = f.read()
# print(st)  # HelloWorld。在内存中使用的一个Str对象表示
# # 读完比之后调用close关闭文件,文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
# f.close()

# 文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
# try:
# 	f = open("C:\\Users\\Zhouz\\Desktop\\test.txt", 'r')
# 	print(f.read())  # 将读取到的内容打印出来
# finally:
# 	if f:
# 		f.close()

# Python引入了with语句来自动帮我们调用close()方法

# with open('/path/to/file', 'r') as f:
# 	print(f.read())
# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法

"""
	读取文件注意事项：
		调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
		所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
		另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
		因此，要根据需要决定怎么调用。
		
		像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
		除了file外，还可以是内存的字节流，网络流，自定义流等等。
		file-like Object不要求从特定类继承，只要写个read()方法就行。
"""
# with open("C:\\Users\\Zhouz\\Desktop\\test.txt", 'r', encoding='UTF-8', errors='ignore') as f:
# 	# 使用readlines()一次读取test.txt中所有内容并按行返回list。
# 	for lines in f.readlines():
# 		# strip()
# 		print(lines.strip())


# 写入文件到test.txt文件里面, 'a'参数就是append，追加到文件后面
f = open("C:\\Users\\Zhouz\\Desktop\\test.txt", 'a', encoding='utf-8')
f.write('hello writefile')
f.close()
# 保险起见还是使用with方式比较好
with open("C:\\Users\\Zhouz\\Desktop\\test.txt", 'r') as f:
	for lines in f.readlines():
		print(lines.strip())  # hello writefile
# 'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。
# 如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入


