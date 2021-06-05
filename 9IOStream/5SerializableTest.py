#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle

"""
	1、pickle.dumps(obj)-把对象序列化后以bytes对象返回,不写入文件
	import pickle
	dump()函数接受一个文件句柄和一个数据对象作为参数，数据对象以特定的格式保存到给定的文件中
	pickle.dump(obj,f)
	
	pickle.dumps(obj,f)
	load()函数从文件中取出已保存的对象时，pickle知道如何恢复这些对象到它们本来的格式
	pickle.load(f)
	pickle.loads(f)
"""
t1 = (1, 2, 3, 4, 5)
l1 = [1, 2, 3, 4, 5]

res_t1 = pickle.dumps(t1)
res_l1 = pickle.dumps(l1)

# 对数据进行序列化之后，
print(res_l1)
print(res_t1)
# b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'

"""
	2、pickle.loads(bytes_object) — 从 bytes 对象中读取一个反序列化对象，并返回其重组后的对象
"""
# 将序列化的res_t1，反序列化为一个对象
t = pickle.loads(res_t1),
print(t, type(t))

l = pickle.loads(res_l1),
print(l, type(l))


"""
	3、pickle.dump(obj , file) — 序列化对象，并将结果数据流写入到文件对象中
		pickle.dump()直接把对象序列化后写入一个file-like Object：
"""

with open("C:\\Users\\Zhouz\\Desktop\\test.txt", 'wb') as f:
	pickle.dump(t1, f)

with open("C:\\Users\\Zhouz\\Desktop\\test.txt", 'wb') as f:
	pickle.dump(l1, f)


"""
	4、pickle.load(file) — 反序列化对象，将文件中的数据解析为一个Python对象
"""
with open("C:\\Users\\Zhouz\\Desktop\\test.txt", 'rb') as f:
	res = pickle.load(f)
	print(res)  # [1, 2, 3, 4, 5]


