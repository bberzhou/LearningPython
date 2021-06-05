#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

"""
	操作文件和目录：
		1、要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
		2、Python内置的os模块也可以直接调用操作系统提供的接口函数
			os.name, 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
					要获取详细的系统信息，可以调用uname()函数
			注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
		3、环境变量：
			在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
			
		4、操作文件和目录
			操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
		5、把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
		   这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
		   同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
		
		6、OS包中没有提供文件的复制等操作，shutil模块提供了copyfile()的函数，
			可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
"""

print(os.name)  # nt ,如果是nt，就是Windows系统
# print(os.uname())   # 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的
print(os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('PATH'))  # 获取PATH中的变量

# 查看、创建和删除目录的用法
# 1、查看当前目录的绝对路径:
print(os.path.abspath('.'))  # D:\CodeFiles\PyCharmProject\LearningPython\9IOStream

# 2.1在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# print(os.path.abspath('.'))
# 2.2然后创建一个目录:
# os.mkdir("D:\\CodeFiles\\PyCharmProject\\LearningPython\\9IOStream\\testdir")
# 注意，如果由同名的文件夹存在时，再次创建就会报错，FileExistsError
# 3、删除一个目录
# os.rmdir("D:\\CodeFiles\\PyCharmProject\\LearningPython\\9IOStream\\testdir")
# 同样的道理，删除之后，再删除会报：FileNotFoundError:错误
# 拆分文件名,后一部分总是最后级别的目录或文件名
# print(os.path.split("C:\\Users\\Zhouz\\Desktop\\test.txt"))
# ('C:\\Users\\Zhouz\\Desktop', 'test.txt')
tu = os.path.split("C:\\Users\\Zhouz\\Desktop\\test.txt")  # split()函数拆分得到一个元组
print(tu[0])  # C:\Users\Zhouz\Desktop
print(tu[1])  # test.txt

tu1 = os.path.splitext("C:\\Users\\Zhouz\\Desktop\\test.txt")
print(tu1[0])  # C:\Users\Zhouz\Desktop\test
print(tu1[1])  # .txt

# 文件操作使用下面的函数。假定当前目录下有一个test.txt文件

# 对文件重命名:
# os.rename('test.txt', 'test.py')
# # 删掉文件:
# os.remove('test.py')

# 利用列表生成式来过滤文件
# 要列出当前目录下的所有目录os.path.isdir(x),判断x是否是目录
print([x for x in os.listdir('.') if os.path.isdir(x)])  # 有一个test 目录，['test']

# 要列出素有的.py文件,首先判断x是file,然后后缀名为.py结尾,os.path.splitext(x),获取x 的后缀名
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
# 输出结果：['1IOIntro.py', '2StringIOByteIO.py', '3filedir.py', '__init__.py']

# 练习：1、利用os模块编写一个能实现dir -l输出的程序。
# 练习：2、编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
