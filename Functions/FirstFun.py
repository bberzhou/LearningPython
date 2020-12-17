import math

#  python 库自带的函数，可以直接调用，参考文档 https://docs.python.org/3/library/functions.html
print(max(1, 3))


# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(5))


# 定义一个空函数,pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
def nop():
    pass


def my_abs1(x):
    if not isinstance(int, float, ):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x


# print(my_abs1('A')) raise TypeError('bad operand type')


# 函数返回多个返回值,Python的函数返回多值其实就是返回一个tuple，但写起来更方便

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


m, n = move(100, 100, 60, math.pi / 6)
print(m, n)
# 151.96152422706632 70.0

r = move(100, 100, 60, math.pi / 6)
print(r)


# 其实返回的是一个(151.96152422706632, 70.0)  tuple

