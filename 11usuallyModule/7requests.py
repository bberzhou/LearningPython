#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
"""
	requests。它是一个Python第三方库，处理URL资源特别方便
"""

# 一、get请求
# 使用requests访问一个页面

r = requests.get("https://www.baidu.com/")  # 百度首页
code = r.status_code
print(code)  # 200
text = r.text
print(text)  # HTML file

r1 = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r1.url)  # 实际请求的URL地址：https://www.douban.com/search?q=python&cat=1001

# requests自动检测编码，可以使用encoding属性查看
print(r.encoding)  # ISO-8859-1
print(r1.encoding)  # None
# 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：

print(r.content)

# requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：
r2 = requests.get('https://69530c99-9322-4e19-a44d-41f94bacdaa5.mock.pstmn.io/addressTest')
print(r2.json())

# 需要传入HTTP Header时，我们传入一个dict作为headers参数
# r3 = requests.get('https://www.baidu.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r3.text)

# 二、POST请求
# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
r4 = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})


# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数
# params = {'key': 'value'}
# r5 = requests.post(url=, json=params)

# 类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数
# 并且注意：在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度
# upload_file = {'file': open('', 'rb')}
# r6 = requests.post(url=, files=upload_file)

# 把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源


# requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头
print(r.headers)
print(r.headers['Content-Type'])  # text/html,这里返回的是dict，可以按照key值获取value值
print(r.headers['Date'])

# requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：

print(r.cookies)

# 如果要在请求中传入Cookie，只需准备一个dict传入cookies参数：
# cooki = {'token':'12345', 'status': 'working'}
# r8 = requests.get(url=,cooki=cooki)

# 要指定超时，传入以秒为单位的timeout参数：
# r9 = requests.get(url=,timeout=2.7)

# 请求豆瓣网页时，提供一个headers，现在大部分网站都增加了安全验证
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://www.douban.com/'
r10 = requests.get(url, headers=headers)
