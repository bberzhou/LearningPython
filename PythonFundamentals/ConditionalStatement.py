#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 一、条件判断
age = 20
if age >= 18:
    print('your age is :', age)
else:
    print('child')
    # 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
if age >= 18:
    print('your age is: ', age)
    print('adult')

    # if判断条件还可以简写，比如写：

    # if x:
    #     print('')
# 二、多重嵌套
num = 10
if num >= 18:
    print('adult')
elif num >= 6:
    print('teenager')
else:
    print('child')

# input函数，可以从键盘读取字符串，可以使用int()函数转换成int类型数据
birthStr = input('birth:')
birthInt = int(birthStr)
if birthInt < 200:
    print('00前')
else:
    print('00后')

# 多重判断
height = 1.75
weight = 80.5
bmi = weight / height ** 2
if bmi > 32:
    print('very heavy')
elif bmi > 28:
    print('heavy')
elif bmi > 25:
    print('little')
elif bmi > 18.5:
    print('normal')
else:
    print('guoqing')

# 循环。python里面有两种循环，一种是for...in 循环，另外一种是while循环
# 依次把list或者tuple中的每个元素迭代出来，所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句

names = ['Michael', 'Bob', 'Alice']
for name in names:
    print(name)

# 计算1加到100，range()函数可以生成一个整数序列，再通过list()函数可以转换为list
# range(101)就可以生成0-100的整数序列
su = 0
for x in list(range(101)):
    su += x

print(su)

# 使用while循环计算0到100
sum1 = 0
n = 100
while n >= 0:
    sum1 += n
    n = n - 1
print(sum1)

# break关键字,在循环中，break语句可以提前退出循环

n1 = 1
while n1 <= 100:
    if n1 > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n1)
    n1 = n1 + 1
print('END')
# 执行上面的代码可以看到，打印出1~10后，紧接着打印END，程序结束。可见break的作用是提前结束循环

# 只打印奇数，可以用continue语句跳过某些循环
n2 = 0
while n2 < 10:
    n2 = n2 + 1
    if n2 % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n2)

# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。

# 要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

# 有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。
