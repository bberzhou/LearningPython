#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	字符串编码一直是令人非常头疼的问题，尤其是我们在处理一些不规范的第三方网页的时候。
	虽然Python提供了Unicode表示的str和bytes两种数据类型，并且可以通过encode()和decode()方法转换，
	但是，在不知道编码的情况下，对bytes做decode()不好做。
	chardet用来检测编码

"""

# 使用chardet
# 当我们拿到一个bytes时，就可以对其检测编码。用chardet检测编码，只需要一行代码
import chardet

cha = chardet.detect(b'Hello, world')
print(cha)  # {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}，检测出ascii的概率

data = '大加号'.encode('utf-8')
ch = chardet.detect(data)
print(ch)  # {'encoding': 'utf-8', 'confidence': 0.87625, 'language': ''}

data1 = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data1))  # {'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}

# 可见，用chardet检测编码，使用简单。获取到编码后，再转换为str，就可以方便后续处理。
