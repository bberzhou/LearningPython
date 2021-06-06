#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from datetime import datetime, timedelta, timezone

"""
	1、datetime是Python处理日期和时间的标准库
		strptime():str-parse-time：字符串解析为时间,将字符串转换为时间格式
		strftime()：str-format-time:字符串格式化时间，将时间格式转换为字符串
	
"""
# 一、获取当前日期和时间
now = datetime.now()  # 获取当前datetime
# datetime.now()返回当前日期和时间，其类型是datetime
print(now)  # 2021-06-05 20:20:46.817317

print(type(now))  # <class 'datetime.datetime'>
# datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。

"""
	二、获取指定日期和时间
"""
dt = datetime(2019, 4, 20, 20)
print(dt)  # 2019-04-20 20:00:00 手动自定义时间

"""
	三、datetime转换为timestamp
"""
# 时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# 这个时间对应的北京时间是 ：timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00

# 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法

dtime = datetime(2021, 5, 20, 18)
ds = dtime.timestamp()
print(ds)  # 1621504800.0
# 注意Python的timestamp是一个浮点数，整数位表示秒

# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法
ts = 122323434.0
print(datetime.fromtimestamp(ts))  # 1973-11-17 02:43:54
# timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换
# 实际上就是UTC+8:00时区的时间

# timestamp也可以直接被转换到UTC标准时区的时间

print(datetime.utcfromtimestamp(ts))  # 1973-11-16 18:43:54 + 8就是上面的时间

"""
	四、str转换为datetime：
		用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。
		转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串
"""
cday = datetime.strptime("2020-6-5 18:19:20", "%Y-%m-%d %H:%M:%S")
print(cday)  # 2020-06-05 18:19:20，就跟字符串的格式相同
# 字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式
# 注意转换后的datetime是没有时区信息的

"""
	五、datetime转换为str:
		如果已经有了datetime对象，要把它格式化为字符串显示给用户，
		就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：
"""
nowtime = datetime.now()
print(nowtime.strftime('%a, %b %d %H:%M'))
# Sat, Jun 05 20:58，

"""
	六、datetime加减：
		对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime
		加减可以直接用+和-运算符，不过需要导入timedelta这个类
"""
now1 = datetime.now()
print(now1)
# 在now1的时间基础上加10个小时
print(now1 + timedelta(hours=10))
# 在now1的基础上-1天
print(now1 - timedelta(days=1))
# 可见，使用timedelta你可以很容易地算出前几天和后几天的时刻。

"""
	七、本地时间转换为UTC时间
		本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
		一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
"""
tz_utc_8 = timezone(timedelta(hours=0))  # 创建时区UTC+8：00
now2 = datetime.now()
dtime1 = datetime(2015, 5, 18)
print(dtime1)
dtime1.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00
print(dtime1)

"""
	八、时区转换
		可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
		时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
		利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
		注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。
"""
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=tz_utc_8)
print(utc_dt)  # 2021-06-05 13:22:33.250680+08:00
# astimezone()将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)  # 2021-06-05 13:23:51.721734+08:00


def to_timestamp(dt_str, tz_str):
	# 正则表达式对第二个参数，时区进行过滤
	global tz1
	tz = re.match(r'^UTC(.)(\d{1,2}):(\d{2})$', tz_str)
	# re.match(r'^UTC([+-]{1}\d{1,2}):0{2}$',tz_str)

	# print(tz.groups())
	if tz.groups()[0] == '+':
		tz1 = 1 * int(tz.groups()[1])
	elif tz.groups()[0] == '-':
		tz1 = -1 * int(tz.groups()[1])

	# 将输入的日期，格式化为标准日期，并设置时区
	ctime = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
	tz_utc = timezone(timedelta(hours=tz1))
	cday = ctime.replace(tzinfo=tz_utc)
	cday_timestamp = cday.timestamp()
	return  cday_timestamp


print(to_timestamp('2015-6-1 08:10:30', 'UTC+7:00'))

