#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""  # 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

__author__ = 'BBer zhou'  # __author__变量把作者写进去

import sys

'''
	为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，
	这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。
	在Python中，一个.py文件就称之为一个模块（5Module）

	使用模块的好处：
		1、提高了代码的可维护性
		2、提高代码的复用性
		3、使用模块还可以避免函数名和变量名冲突。

	为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）
	每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的
	__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块


	注意：
	模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。
	创建自己的模块时，要注意：
	模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
	模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。
'''


# 以内建的sys模块为例，编写一个hello的模块


def test():
	# 	sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，
	args = sys.argv
	if len(args) == 1:
		print('Hello world')
	elif len(args) == 2:
		print('hello, %s!' % args[1])
	else:
		print('Too many arguments!')


if __name__ == '__main__':
	test()
# 当我们在命令行运行intro模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该intro模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。


'''
	作用域：
		在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有
		的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
		正常的函数和变量名是公开的（public）
	
		类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量
		类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
		，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，
		是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
	
'''


def _private_1(name):
	return 'hello, %s' %name


def _private_2(name):
	return 'hi, %s' % name


def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)

# 在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，
# 这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。


print(greeting('hidd'))


'''
	关于安装第三方模块：
		使用pip安装或者Anaconda
	
	
	模块搜索路径：
	Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错
	默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量
	print(sys.path)
	
	如果我们要添加自己的搜索目录，有两种方法：
		一是:直接修改sys.path，添加要搜索的目录：
			sys.path.append('/Users/michael/my_py_scripts')
		二是：设置环境变量PYTHONPATH
			该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。
			注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。
	
'''

