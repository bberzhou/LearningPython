classmates = ['Michael', 'bob', 'Tracy']
print(classmates)
# 变量classmates就是一个list。用len()函数可以获得list元素的个数
length = len(classmates)
print(length)
# 用索引来访问list中每一个位置的元素，记得索引是从0开始的
# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
print(classmates)

# 也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1, 'jack')
print(classmates)

# 要删除list末尾的元素，用pop()方法：
classmates.pop()
print(classmates)
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)
print(classmates)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'sarah'
print(classmates)

# list里面的元素的数据类型也可以不同,list元素也可以是另一个list

L = ['Apple', 123, True]
L1 = ['python', 'java', ['asp', 'php'], 'scheme']
len(L1)  # 4


# 另一种有序列表叫元组，tuple,tuple和list非常类似，但是tuple一旦初始化就不能修改
classmate = ('Michael', 'Bob', 'Tracy')
# classmate这个tuple不能变了，它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2)
print(t)    # (1, 2)

# 定义一个空的tuple
tl = ()
# 定义一个只有一个元素的tuple，必须价格逗号
t2 = (1,)

# "可变"的tuple
t3 = ('a', 'b', ['A', 'B'])
# 修改里面的元素
t3[2][1] = 'X'
print(t3)   # ('a', 'b', ['A', 'B'])
# 事实上这里变的不是tuple的元素，而是list里面的元素，tuple的每一个元素，指向永远不变
