# 高阶函数

# 一、变量可以指向函数
print(abs(-10))
# <built-in function abs> 内置函数
print(abs)

# 把函数本身赋值给变量
fun = abs
print(fun(-4))


# 输出4，函数本身也可以赋值给变量，即：变量可以指向函数。

# 函数名其实就是指向函数的变量，

# 二、传入函数，变量可以指向函数，函数的参数能接收变量，
# 那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数

# 传入函数名fun
def add(x, y, f):
    return f(x) + f(y)


print(add(-2, -4, fun))
# 6 传入fun函数名，
