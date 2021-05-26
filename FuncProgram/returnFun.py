# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

# 一、通常可变参数的求和

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 但是，如果不需要立刻求和，而是在后面的代码中，
# 根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数

def lazy_sum(*args):
    def su():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return su


# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f = lazy_sum(1, 2, 3, 5, 6)
print(f)
# 此时返回的是求和的函数 <function lazy_sum.<locals>.su at 0x107957730>

print(f())
# 17，调用时才真正计算求和的结果

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，
# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力。


f1 = lazy_sum(1, 2, 3, 5, 6)
f2 = lazy_sum(1, 2, 3, 5, 6)
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
print(f1== f2)
# False，f1 和f2的调用结果互不影响



# 二、闭包（Closure）

