'''
List表是可以修改的数据结构，而Tuple元组是固定长度，不能被修改元素值的数据结构。
元组是使用圆括号()表示，而列表是使用方括号[]。请注意两者的区别。

创建元组最简单的方法是用逗号分隔一些值，元组自动创建完成；元组大部分
时候是通过圆括号括起来的；空元组可以用没有包含内容的圆括号来表示；
只含一个值的元组，必须加个逗号（,）； (1,)
'''

tup1 = 1, 2, 3
tup2 = 'python', 'java'
# 创建元组
tup3 = (1, 2, 3, 4)
# 创建空元组
tup4 = ()
# 只有一个元素的元组
tup5 = (1,)
# 不是元组，是一个整型数字
tup6 = (1)
print(tup1)
print(tup2)
print(tup3)
print(tup4)
print(tup5)
print(type(tup6))

'''
Python中的tuple（）函数也可以创建元组，将任意序列或者迭代器放在该函数内即可。
注意该函数只接受 任意序列或迭代器 ， 比如不能是数字的组合，例子tuple(1,2,3)
Python 编程中，我们经常使用 tuple() 把列表变成字典。
另外，我们还可以通过双层圆括号创建元组的元组。
'''
# 使用tuple（）函数创建元组
tup2_tuple = tuple('python')
print(tup2_tuple)

tup3_tuple = tuple(['Python', 'Java', 'C'])
print(tup3_tuple)
# 构造元组的元组
tup7 = (1, 2, 3, 4), ('Python', 'Java')
print('创建的元组:', tup7)

# 使用tuple()函数创建元组的元组
tup_tuple = ((1, 2, 3, 4), ('Python', 'Java'))
print('使用tuple函数创建元组:', tup_tuple)

'''
我们还可以通过加号（+）把多个元组拼接在一起，形成更长的元组；也可以使用乘号（*）
复制多份同样的元组
'''
# 通过 + 生成更长的元组
tup8 = (1, 2, 3, 4) + ('Python', 'Java', 5) + ('C++',)
print('通过 + 生成更长的元组',tup8)
# 通过 * 生成多份同样的元组
tup9 = ('Python','Java') * 3
print('通过 * 生成多份同样的元组', tup9)

# 试图修改元组
'''
元组创建完成以后，其各个位置上的值是不可以修改，否则得到一个错误：'tuple' object
does not support item assignment。但是，如果我们创建的元组中包括可变的对象，比如列
表，那么我们可以修改它的值。
'''
tup4_tuple = tuple(['Python', [1, 2, 3], 'Java'])
print('创建还有列表的元组:', tup4_tuple)
# 试图修改元组的值
# tup4_tuple[2] = 'C++'

# 可以修改元组中列表的值
tup4_tuple[1].append(4)
print('修改元组中的可变对象。修改后的元素是：', tup4_tuple)

'''
元组的值虽然不能被修改，但是可以给存储元组的变量赋不同的值。并且元组中的任一项都
可以通过索引被单独访问。也就是说，元组中的每一项都有一个索引号，并且从 0 开始计数。与
列表切片一样，元组也可以使用切片的方法访问列表中的元素
'''
rag = (30, 40, 50)
print('old range is:\n')
print(rag)
rag = (60, 70, 80)
print('new range is:\n')
print(rag)
print('使用索引访问元组中的第二个元素', rag[1])
print('使用切片访问元组中前两个元素', rag[0:2])

'''
元组中的值是不允许删除的，但是我们可以使用 del 语句删除整个元组。但是删除以后在输
出就会报错，证明已被删除。
'''
up3_tuple = tuple(['Python', 'Java', 'C++'])
print(tup3_tuple)
# 删除元组
del tup3_tuple
print(tup3_tuple)