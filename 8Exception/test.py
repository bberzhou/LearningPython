#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
# 加上这一行之后，在37行报错时，会有一个INFO：输出
logging.basicConfig(level=logging.INFO)
"""
	调试程序：
		方法一：第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看：

		方法二：断言，凡是用print()来辅助查看的地方，都可以用断言（assert）来替代

		方法三：logging，把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件
			   它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，
			   logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了
			   logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
			   
		方法四：pdb:启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：
		


"""


def foo(s):
	n = int(s)
	# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
	# 如果断言失败，assert语句本身就会抛出AssertionError
	assert n != 0, 'n is zero!'
	return 10 / n


def main():
	foo('0')

# 启动Python解释器时可以用-O参数来关闭assert,关闭后，你可以把所有的assert语句当成pass来看


#
s = '0'
n = int(s)
logging.info('n = %d'% n)
print(10 / n)
