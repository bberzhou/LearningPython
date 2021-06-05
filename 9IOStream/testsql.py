#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mysql.connector

# 设置连接参数等
conn = mysql.connector.connect(
	host='127.0.0.1',
	user='root',
	password='123456',
	database='plp',
	auth_plugin='mysql_native_password')

# 获取一个连接对象
cursor = conn.cursor()

# 创建user表：
# cursor.execute('create table user(id varchar(20) primary key, name varchar (20))')
cursor.execute('insert into user(id,name) values (%s, %s)', ['2', 'Michael'])
# print(cursor.rowcount)
# 提交
conn.commit()
# 关闭连接
cursor.close()
conn.close()
