#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import pickle
from io import StringIO, BytesIO

"""
	序列化：
	1、在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict
		d = dict(name='Bob', age=20, score=88)
		可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。
		如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。
	2、把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization

	3、序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
		反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
	4、Python提供了pickle模块来实现序列化
		对象---》序列化:pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
				另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
	    序列化---->对象：	对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
	    				也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
		
		pickling" 是将 Python 对象及其所拥有的层次结构转化为一个字节流的过程
		而 "unpickling" 是相反的操作，会将（来自一个 binary file 或者 bytes-like object 的）字节流转化回一个对象层次结构
		
	    				
	5、JSON
		 在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
		 但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，
		 可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便
		 
		JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
		JSON类型		Python类型
		{}	    	dict
		[]	    	list
		"string"	str
		1234.56	int或float
		true/false	True/False
		null	None 
	   	Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
	   	1、dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
	   	2、要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
	   	
	   	pickle(python3.x)和cPickle(python2.x的模块)相当于java的序列化和反序列化操作。				
"""
# 一、把一个对象序列化并写入文件
# 1、首先，我们尝试把一个对象序列化并写入文件
d = dict(name='Bob', age=20, score=80)
# # 2、 pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# by = pickle.dumps(d)
# # 3、wb，写入二进制文件
# with open("C:\\Users\\Zhouz\\Desktop\\test.txt", 'wb') as f:
# 	f.write(by)


# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
# f = open("C:\\Users\\Zhouz\\Desktop\\test.txt", 'wb')
# pickle.dump(d, f)
# f.close()

# 二、把序列化对象从磁盘读到内存时
#    方法一
# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
# f = open("C:\\Users\\Zhouz\\Desktop\\test.txt", 'rb')
# r1 = pickle.load(f)
# print(r1)  # {'name': 'Bob', 'age': 20, 'scoree': 80}
# b = BytesIO()
# r1 = open("C:\\Users\\Zhouz\\Desktop\\test.txt", 'rb')
# r1.close()
# b.write(pickle.loads(r1))
# print(b.getvalue())


#     方法二
# with open("C:\\Users\\Zhouz\\Desktop\\test.txt", 'rb') as f:
# 	# pickle.load()方法从一个file-like Object中直接反序列化出对象
# 	dout = pickle.load(f)
# # 	# 输出对象，{'name': 'Bob', 'age': 20, 'scoree': 80}
# 	print(dout)


# JSON
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
js = json.dumps(d)
print(js)
# {"name": "Bob", "age": 20, "scoree": 80}
# dumps()方法返回一个str，内容就是标准的JSON。
# 类似的，dump()方法可以直接把JSON写入一个file-like Object、

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
json_str = '{"age": 20, "score": 80}'
st = json.loads(json_str)
print(st, type(st))
# {'age': 20, 'score': 80} <class 'dict'>

"""
	JSON进阶：
		Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，
		更喜欢用class表示对象，比如定义Student类，然后序列化
"""


class Student(object):

	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score


s = Student('Bob', 20, 88)


# 想把自己定义类序列化时报错，TypeError: Object of type Student is not JSON serializable
# print(json.dumps(s))
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，
# 我们只需要为Student专门写一个转换函数，再把函数传进去即可


def student2dict(std):
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score
	}


# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
print(json.dumps(s, default=student2dict))
# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict
# 为了方便每一个类都可以序列化,可以把default设置一个lambda表达式
print(json.dumps(s, default=lambda obj: obj.__dict__))
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
# 也有少数例外，比如定义了__slots__的class。

# 如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例


def dict2student(d):
	return Student(d['name'], d['age'], d['score'])

json_st = '{"age":20, "score": 88, "name": "Bob}'
print(json.loads(json_st, object_hook=dict2student))
