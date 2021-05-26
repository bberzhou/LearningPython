from functools import reduce


# map 和reduce

# 一、map接收两个参数，一个是函数，一个是Iterable,map讲传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回
# 例如函数f(x) = x^2


def fun(x):
    return x * x


result = map(fun, [1, 2, 3, 4, 5, 6, 7, 8])
print(list(result))
# [1, 4, 9, 16, 25, 36, 49, 64]
# map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，
# 还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串

print(list(map(str, [1, 2, 3, 4, 5, 6, 7])))


# ['1', '2', '3', '4', '5', '6', '7']

# 二、reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是:reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 比如对一个序列求和，就可以用reduce实现：
def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7]))


# 输出16


# map和reduce函数结合起来使用,把字符串str转换成为int的函数

def fn(x, y):
    return x * 10 + y


def charTonum(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(charTonum, '13576')))

# 整理成一个转换函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def strToint(s):
    def fn(x, y):
        return x * 10 + y

    def charTonum(s):
        return DIGITS[s]

    return reduce(fn, map(charTonum, s))
