# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# from hello import Hello
# """
# 	元类：
# 		动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
#
# """
#
# # 当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象
#
# h = Hello()
# h.hello()  # Hello, world.
#
# print(type(Hello))  # <class 'type'>
# # type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type,h是一个实例，它的类型就是class Hello
# # class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
# print(type(h))  # <class 'hello.Hello'>
#
# # class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
# # type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# # 比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义
#
#
# def fn(self, name='world'):  # 先定义函数
# 	print('hello, %s.' % name)
#
#
# # (object,) tuple 单元素的写法
# Hell = type('Hell', (object,), dict(hell=fn))  # 创建Hell class
#
# h = Hell()
#
# h.hell()  # 这里的hello()，实际就是fn函数
#
# print(type(Hell))  # <class 'type'>
#
# print(type(h))  # <class '__main__.Hell'>
#
#
# """
# 	要创建一个class对象，type()函数依次传入3个参数
# 		1、class的名称；
# 		2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 		3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# """
# Test = type('Test', (object, ), dict(test=fn))
# te = Test()
# te.test()  # hello, world.
# # 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
# # 仅仅是扫描一下class定义的语法，然后调用type()函数创建出class
# # 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来
#
#
# """
# 	metaclass:
# 	除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
# 	metaclass，直译为元类，简单的解释就是：
# 	当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 	但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 	连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
# 	所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
# 	metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。
# """
#
# # 例子，这个metaclass可以给我们自定义的MyList增加一个add方法
# # metaclass是类的模板，所以必须从'type'类派生
#
#
# class ListMetaclass(type):
#
# 	"""
# 		__new__()方法接收到的参数依次是：
# 		当前准备创建的类的对象；
# 		类的名字；
# 		类继承的父类集合；
# 		类的方法集合。
# 	"""
#
# 	def __new__(cls, name, base, attrs):
# 		attrs['add'] = lambda self, value: self.append(value)
# 		return type.__new__(cls, name, base, attrs)
#
# # 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass
#
#
# class MyList(list, metaclass=ListMetaclass):
# 	pass
#
#
# # 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，
# # 要通过ListMetaclass.__new__()来创建,在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
#
# # 测试一下MyList是否可以调用add()方法
# L = MyList()
# L.add(1)
# print(L)  # [1]
#
# # L2 = list()
# # L2.add(1)
# # print(L2)   # 'list' object has no attribute 'add'，普通的list没有add()方法
#
#
# # 使用metaclass虽然比较复杂，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子
# # ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，
# # 也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句
# # 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
#
# # 编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User
#
# # 首先来定义Field类，它负责保存数据库表的字段名和字段类型：
# class Field(object):
#
# 	def __init__(self, name, column_type):
# 		self.name = name
# 		self.column_type = column_type
#
# 	def __str__(self):
# 		return '<%s:%s>' % (self.__class__.__name__, self.name)
#
# # 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等
#
#
# class StringField(Field):
#
# 	def __init__(self, name):
# 		super(StringField, self).__init__(name, 'varchar(100)')
#
#
# class IntegerField(Field):
#
# 	def __init__(self, name):
# 		super(IntegerField, self).__init__(name, 'bigint')
#
#
# # 编写最复杂的ModelMetaclass
#
# class ModelMetaclass(type):
#
# 	def __new__(cls, name, bases, attrs):
# 		if name=='Model':
# 			return type.__new__(cls, name, bases, attrs)
# 		print('Found model: %s' % name)
# 		mappings = dict()
# 		for k, v in attrs.items():
# 			if isinstance(v, Field):
# 				print('Found mapping: %s==>%s' % (k, v))
# 				mappings[k] = v
#
# 		for k in mappings.keys():
# 			attrs.pop(k)
# 		attrs['__mapping__'] = mappings  # 保存属性和列的映射关系
# 		attrs['__table__'] = name  # 假设表名和类名一致
# 		return type.__new__(cls, name, bases, attrs)
#
#
# # 以及基类（Model）
# class Model(dict, metaclass=ModelMetaclass):
#
# 	def __init__(self, **kw):
# 		super(Model, self).__init__()
#
# 	def __getattr__(self, key):
# 		try:
# 			return self[key]
# 		except KeyError:
# 			raise AttributeError(r"'Model' object has no attribute '%s'" % key)
#
# 	def __setattr__(self, key, value):
# 		self[key] = value
#
# 	def save(self):
# 		fields = []
# 		params = []
# 		args = []
# 		for k, v in self.__mappings__.items():
# 			fields.append(v.name)
# 			params.append('?')
# 			args.append(getattr(self, k, None))
# 		sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
# 		print('SQL: %s' % sql)
# 		print('ARGS: %s' % str(args))
#
#
# class User(Model):
# 	# 定义类的属性到列的映射
# 	id = IntegerField('id')
# 	name = StringField('username')
# 	email = StringField('email')
# 	password = StringField('password')
#
#
# # 创建一个user实例
# u = User(id=123, name = 'Michael', email='test@123.com', password='test')
#
# # 保存到数据库
# u.save()
#
# # 其中父类Model和属性类型StringField、IntegerField是由ORM框架提供的，
# # 剩下的魔术方法比如save()全部由父类Model自动完成。虽然metaclass的编写会比较复杂，
# # 但ORM的使用者用起来却异常简单。
#
