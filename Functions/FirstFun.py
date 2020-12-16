print(max(1, 3))


# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(5))
