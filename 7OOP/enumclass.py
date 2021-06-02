#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum, unique

"""
    使用枚举类
    
"""

# 枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# value属性则是自动赋给成员的int常量，默认从1开始计数


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Week(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 访问这些枚举类型可以有若干种方法
day1 = Week.Mon
print(day1)

print(Week.Tue)  # Week.Tue

print(Week.Tue.value)   # 2

print(day1 == Week.Mon)     # True

print(Week(1))      # Week.Mon

for name, member in Week.__members__.items():
    print(name, '=>', member)

# Sun => Week.Sun
# Mon => Week.Mon
# Tue => Week.Tue
# Wed => Week.Wed
# Thu => Week.Thu
# Fri => Week.Fri
# Sat => Week.Sat

# 可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。

