#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
"""
	TCP简介：
		Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，
		而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可
		大多数连接都是可靠的TCP连接。创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器
		
"""

# 创建一个socket,创建Socket时，AF_INET指定使用IPv4协议,如果要用更先进的IPv6，就指定为AF_INET6
# SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
# IP地址可以用域名www.sina.com.cn自动转换到IP地址,注意参数是一个tuple，包含地址和端口号。
s.connect(('www.baidu.com', 80))
# 建立TCP连接后，就可以向新浪服务器发送请求，要求返回首页的内容：
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# TCP连接创建的是双向通道，双方都可以同时给对方发数据

# 接收请求到的数据
buffer = []
# 接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，
# 在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环
data = ''
while True:
	# 每次最多接收1k字节
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
	# 	拼接数据
	data = b''.join(buffer)

# 当我们接收完数据后，调用close()方法关闭Socket，这样，一次完整的网络通信就结束了：
s.close()

# 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数写入文件
with open('sina.html', 'wb') as f:
	f.write(html)

# 一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket