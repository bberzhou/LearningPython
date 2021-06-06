#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import threading
import time

# 首先，创建一个基于IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听地址和端口
s.bind(('127.0.0.1', 9999))

# 紧接着调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')
# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接


def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome')
	while True:
		# 接受客户端发送的数据
		data = sock.recv(1024)
		time.sleep(5)
		# 如果没有数据或者数据为exit就退出
		if not data or data.decode('utf-8') == 'exit':
			break
		# 	向客户端发送数据
		sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
	# 	关闭socket连接
	sock.close()
	print('Connection from %s:%s closed.' % addr)


# 接下来，服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接/


while True:
	# 接受一个新连接：
	sock, addr = s.accept()
	# 创建一个新的线程来处理TCP连接：
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()
