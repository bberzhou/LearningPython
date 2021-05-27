#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度

d = {'michael': 97, 'Bob': 90, 'Tracy': 86}
print(d['michael'])  # 97

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入

d['Adam'] = 78
print(d['Adam'])    # 78
# 一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Adam'] = 80
print(d['Adam'])    # 80
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值覆盖掉

# 如果key不存在，dict就会报错
# 要避免key不存在的错误，有两种办法:
# 一是通过in判断key是否存在,会返回一个布尔值,
flag = 'Adam' in d
print(flag)     # True
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Th', ))  # None

print(d.get('Th', -1))  # -1,返回指定的值

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除掉
d.pop('Bob')
print(d)  # 删除Bob,后{'michael': 97, 'Tracy': 86, 'Adam': 78}

# dict内部存放的顺序和key放入的顺序是没有关系的

# list和dict的比较和list比较，
# dict有以下几个特点：
#
#   1、查找和插入的速度极快，不会随着key的增加而变慢；
#   2、需要占用大量的内存，内存浪费多。

# 而list相反：
#
# 1、查找和插入的时间随着元素的增加而增加；
# 2、占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。要注意：dict里面的key必须是不可变的对象
# 在Python中，字符串、整数等都是不可变的
# 这是因为dict根据key来计算value的存储位置，
# 如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。
# 这个通过key计算位置的算法称为哈希算法（Hash）
# 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。
# 注意：list是可变的，就不能作为key，例如
key = [1, 2, 3]
# d[key] = 'a list ' TypeError: unhashable type: 'list'

# 二、set
# set和dict类似，也是一组key的集合，但不存储value。
# 由于key不能重复，所以，在set中，没有重复的key。要创建一个set，需要提供一个list作为输入集合

s2 = set([1, 2, 3])  # 老版本的定义方式
s = {1, 2, 3}
print(s)  # {1, 2, 3}
s1 = {'jjhh', 'gg', 'g'}
print(s1)  # {'jjhh', 'gg', 'g'}

# 传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，
# 显示的顺序也不表示set是有序的。并且重复元素在set中自动被过滤

s3 = {1, 2, 3, 4, 5, 1, 3, 4}
print(s3)  # 输出set，{1, 2, 3, 4, 5}相同的元素自动过滤掉

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s3.add(2)
# 通过remove(key)方法可以删除元素
s3.remove(4)
print(s3)  # 输出结果  {1, 2, 3, 5}

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作

s4 = {1, 2, 3}
s5 = {2, 3, 4}
print(s4 & s5)  # {2, 3} 求交集

s6 = {1, 2, 4}
s7 = {1, 4, 0}
print(s6 | s7)  # {0, 1, 2, 4}，求并集

# set和dict的唯一区别仅在于没有存储对应的value，
# 但是，set的原理和dict一样，所以，同样不可以放入可变对象，
# 因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
# 试试把list放入set，看看是否会报错
# s8 = {[1, 2, 4]}, 将一个List放入set就报错
# print(s8)
# s8 = {[1, 2, 4]}
# TypeError: unhashable type: 'list'

# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
# tuple元组虽然是不可变对象，但是放入的元素可以是List，所以还是可以变
s9 = {(1, 2, [2, 3])}
print(s9)
#     s9 = {(1, 2, [2, 3])}
# TypeError: unhashable type: 'list'
