#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
# 为了编写单元测试，我们需要引入Python自带的unittest模块
from mydict import Dict


class TestDict(unittest.TestCase):

	def setUp(self):
		print('setUP...')

	def test_init(self):
		d = Dict(a=1, b='test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key, 'value')
		self.assertEqual(d['key'], 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

	def tearDown(self):
		print('tearDown...')


if __name__ == '__main__':
	unittest.main()

# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
# 对每一类测试都需要编写一个test_xxx()方法。unittest.TestCase提供了很多内置的条件判断，
# 我们只需要调用这些方法就可以断言输出是否是我们所期望的
# 最常用的断言就是assertEqual()：
# self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等
# 另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：


"""
	运行单元测试：
	方式一：一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码
		if __name__ == '__main__':
    		unittest.main()
    方式二：在命令行通过参数-m unittest直接运行单元测试
    	   python -m unittest mydict_test
    	这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试

	setUp与tearDown：可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
	
	加上之后，每个测试方法调用前后都会打印出，那两个方法里面的print()
	
	
	小结：
		单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
		单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
		单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
		单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。
"""
