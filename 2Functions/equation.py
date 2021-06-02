# -*- coding: utf-8 -*-
import math


# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解


def quadratic(a, b, c):
    #  先判断delta的值
    sqr = math.sqrt(b**2 - 4*a*c)
    if sqr >= 0:
        x1 = (-b + sqr) / (2*a)
        x2 = (-b - sqr) / (2*a)
        return x1, x2
    else:
        print('没有实根')


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
