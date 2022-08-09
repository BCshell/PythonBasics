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
# del tup3_tuple
print(tup3_tuple)

# 元组拆包
'''
元组拆包是把元组的对象值分别赋值给不同的变量，也就是元组括号（）内的值给不同的变
量。注意变量的数量必须和元组中对象的数量一样，否则出错。
'''
# 元组拆包
tup9 = ('Python', 'Java', 'C++')
print('原来的元组是:', tup9)
language_1, language_2, language_3 = tup9
print('元组拆包后的值分别是:')
print('language_1 = ', language_1)
print('language_2 = ', language_2)
print('language_3 = ', language_3)
# 如果变量值和元素值不一致时, 报错！
# language_1, language_2, = tup9
# 嵌套元组也可以拆包
# 嵌套元组拆包
tup10 = 1, 2, ('Python', 'Java')
print(tup10)
a, b, (me, xiaoming) = tup10
print(f'我最喜欢的语言是：{me}, 小明最喜欢的语言是：{xiaoming}')

'''
如果我们只要元组的一个值，而不需要其他的元素值
我们使用下划线（_）来表示不想要的变量。但是，如果元组中元素很多，
则需要多个下划线，比如下面的例子中用到了 2 个下划线。在 Python 中，我们可以使用
*变量名来表示，比如*rest。但是我们经常使用的是*_表示多余的变量。
'''
# 使用下划线（_）表示不想要的对象
_, language_2, _ = tup9
print('\n小明最喜欢的编程语言是: ', language_2)

# 使用星号（*）接受任意多个对象值,比如*rest。
language_1, *rest = tup9
print('我最喜欢的编程语言是： ', language_1)
print('我不喜欢的编程语言有：', *rest)

# 但是我们经常使用的是*_表示多余的变量。
# *_也可以用在变量中间,比如生成 9 个数字，输出最后一个
number_1, number_2, *_, number_9 = range(10)
print('我最喜欢的数字是：', number_9)

'''
在 Python 编程中，我们可以使用（*变量名）给函数传递多个值，而不需要单独输入每一个值。
在 Python 中，divmod(a,b)为一个内建函数（直接可以使用的函数。函数为第六天内容）。
它返回 a//b 和 a%b 的结果组成的元组。

'''
# 使用*变量名传递多个值给函数
number_10 = (81, 9)
print(divmod(*number_10))
# 未使用
print(divmod(81, 9))

# 在各种笔试中，我们经常被问到如何交换两个变量的值。Python 可以轻易的使用拆包功能实现。

# 交换两个变量的值
language_4, language_5 = 'Python', 'Java'
print(f'我最喜欢的语言是：{language_4}, 小明最喜欢的语言是：{language_5}')

language_4, language_5 = language_5, language_4
print('交换两个变量值以后：')
print(f'我最喜欢的语言变成：{language_4}, 小明最喜欢的语言变成：{language_5}')

# 元组方法
tup1 = (1, 2, 3, 3, 6, 7, 5, 3)

# 元组名.count(a) 计算某一个数值 a 在元组中出现的次数
print('\n计算元组中 3 出现的次数',tup1.count(3))

# len(tuple) 计算元组个数
print('计算元组个数', len(tup1))

# max(tuple) 返回元组中元素最大值
print('查找元素的最大值', max(tup1))

# min(tuple) 返回元组中元素最小值
print('查找元素的最小值', min(tup1))

# 元组名.index(a) 查找元组中第一个出现 a 的索引值
print('查找 3 出现的索引值', tup1.index(3))

# 元组和列表的差别
'''
元组与列表都是序列类型的容器对象，可以存放任何类型的数据。并且都支持切片、迭代等操作。
元组与列表的定义方法不同，一个是括号（）；另一个是方括号[]。
最重要的差别点是元组是不可变的，而列表是可变的
只有列表才有 append()方法来添加更多的元素，而元组没有
同样大小的数据，元组比列表占用的内存空间更少；并且操作速度上元组更快。
如果需要一个常量集合，并且唯一需要做的是不断的遍历它的元素值，请选择元组而不是列表。
元组和列表之间可以互相转化。列表转化为元组的方法是内置的 tuple()函数接受一个 list，
并且返回一个有着相同元素的元组。元组转化为列表的方法是使用内置的 list()函数。
'''
print('元组的元素有 ', tup1)
print('将元组变成列表', list(tup1))
print(type(list(tup1)))
