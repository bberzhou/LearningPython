#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request, parse
import json

"""
	urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应
"""


# 一、Get请求
# with request.urlopen("https://tieba.baidu.com/index.html") as f:
# 	data = f.read()
# 	print('Status:', f.status, f.reason)
# 	for k, v in f.getheaders():
# 		print('%s:%s' % (k, v))
# 	print('Data:', data.decode('GBK'))

# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
# 	print('Status:', f.status, f.reason)
# 	for k, v in f.getheaders():
# 		print('%s: %s' % (k, v))
# 	print('Data:', f.read().decode('utf-8'))

# 二、POST请求

# print('Login to weibo.cn...')
# email = input('Email: ')
# passwd = input('Password: ')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
#
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))



# 练习题题目：利用urllib读取JSON，然后将JSON解析为Python对象
# https://69530c99-9322-4e19-a44d-41f94bacdaa5.mock.pstmn.io/addressTest

# with request.urlopen("https://69530c99-9322-4e19-a44d-41f94bacdaa5.mock.pstmn.io/addressTest") as f:
# 	data = f.read()
# 	print('Status:', f.status, f.reason)
# 	for k, v in f.getheaders():
# 		print('%s:%s' % (k, v))
# 	print('Data:', data)
# 	json2obj = json.loads(data)
# 	print(json2obj)



# def fetch_data(url):
# 	with request.urlopen(url) as f:
# 		data = f.read().decode('utf-8')
# 		json2obj = json.loads(data)
# 		return json2obj
#
# print(fetch_data("https://69530c99-9322-4e19-a44d-41f94bacdaa5.mock.pstmn.io/addressTest"))

