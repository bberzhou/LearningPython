#   输入输出系统就是I/O
print("hello,world")

#  print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出
print("hello", "world")

print('100+200=', 100 + 200)

# name = input()
# print('your name is ', name)
#   Python的语法比较简单，采用缩进方式，


# print absolute value of an integer:
# Python程序是大小写敏感的，如果写错了大小写，程序会报错。
# 以#开头的语句是注释，注释是给人看的，可以是任意内容，解释器会忽略掉注释。
# 其他每一行都是一个语句，当语句以冒号:结尾时，缩进的语句视为代码块。
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

"""
python输入
Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里
"""
name = input()
print("hello", name)

name2 = input("please input your name:")
print("hello:", name2)
# 当语句以冒号:结尾时，缩进的语句视为代码块，默认使用的是4个空格
# Python程序是大小写敏感的
