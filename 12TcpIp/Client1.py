#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 注意获取连接时，传入一个tuple ,(ip,port)
s.connect(('127.0.0.1', 9999))
# 接收来自服务器端的信息, 并设置格式
data = s.recv(1024).decode('utf-8')
print(data)

# 向服务器端发送数据
for i in [b'num', b'nuu', b'sdd']:
	s.send(i)
	print(s.recv(1024).decode('utf-8'))

# 发送退出信息
s.send(b'exit')

# 关闭连接
s.close()
