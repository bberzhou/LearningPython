# -*- coding: utf-8 -*-
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度

d = {'michael': 97, 'Bob': 90, 'Tracy': 86}
print(d['michael'])  # 97

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入

d['Adam'] = 78
print(d['Adam'])

# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值覆盖掉
# 如果key不存在，dict就会报错
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在,会返回一个布尔值，
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Th', ))  # None

print(d.get('Th', -1))  # -1,返回的指定值

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除掉
d.pop('Bob')
print(d)  # 删除Bob,后{'michael': 97, 'Tracy': 86, 'Adam': 78}

# dict内部存放的顺序和key放入的顺序是没有关系的

# list和dict的比较和list比较，
# dict有以下几个特点：
#
# 1、查找和插入的速度极快，不会随着key的增加而变慢；
# 2、需要占用大量的内存，内存浪费多。

# 而list相反：
#
# 1、查找和插入的时间随着元素的增加而增加；
# 2、占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
# 这是因为dict根据key来计算value的存储位置，
# 如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。
# 这个通过key计算位置的算法称为哈希算法（Hash）
# 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。
# 而list是可变的，就不能作为key，例如
key = [1, 2, 3]
# d[key] = 'a list ' TypeError: unhashable type: 'list'

# set和dict类似，也是一组key的集合，但不存储value。
# 由于key不能重复，所以，在set中，没有重复的key。要创建一个set，需要提供一个list作为输入集合

s2 = set([1, 2, 3])  # 老版本的定义方式
s = {1, 2, 3}
print(s)  # {1, 2, 3}
s1 = {'jjhh', 'gg', 'g'}
print(s1)  # {'jjhh', 'gg', 'g'}

# 传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。
# 并且重复元素在set中自动被过滤
s3 = {1, 2, 3, 4, 5, 1, 3, 4}
print(s3)  # {1, 2, 3, 4, 5}相同的元素自动过滤掉

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s3.add(2)
# 通过remove(key)方法可以删除元素
s3.remove(4)
print(s3)  # 输出结果  {1, 2, 3, 5}

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作

s4 = {1, 2, 3}
s5 = {2, 3, 4}
print(s4 & s5)  # {2, 3}

# set和dict的唯一区别仅在于没有存储对应的value，
# 但是，set的原理和dict一样，所以，同样不可以放入可变对象，
# 因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
# 试试把list放入set，看看是否会报错
