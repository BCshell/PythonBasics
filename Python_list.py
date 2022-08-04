'''
What is the data structure
数据结构是相互之间存在一种或多种特定关系的集合，也可以理解为数据结构就是将数据按照某种方式结合在一起的结构
这里的数据也就是python 中的基本数据类型，比如 整数型、浮点数 字符串等。
在python中，常见的内置数据结构（也就是自带的）是列表、元组、字典、集合等。
在Python的第三方包中还有其他的数据结构，比如Numpy中的Datafram or Series.
'''

'''
list[] 列表是由一系列特定顺序排列组合的元素构成，也就是列表是有序集合, use ，（coma)来分隔其中的元素
可以给列表起一个名字，并且使用 = 把列表名字和列表关联起来，这就叫列表赋值。具体如下：
语法定义：
列表名字 = [元素1,元素2,元素3,.......]
'''

# 定义一个列表
# 演员名单列表
names_python_pc = ['Jay', 'Tom', 'David']
print(f' 演员名单的成员有：{names_python_pc}')
# Always remember that List can be changed, we can easily add or deleter elements from list
# LIST 和 字符串的本质区别是字符串不是能被修改的，and List 是可变的

# LIST 列表的基本操作
print('\n names_python_pc的数据类型是:', type(names_python_pc))
'''
列表常见的操作有   访问元素、添加元素、修改元素、删除元素以及列表排序等等。
这些操作中经常使用的两个术语是函数和方法，我们需要知道他们的区别
函数是独自的一个功能单元，直接可以使用，比如函数 len(列表名)求列表的元素长度；
而方法是依附于对象的，调用方法是 对象.方法()，比如 列表名.sort()，对列表进行排序，方法是面向对象的一个重要概念。
'''
'''
列表是有序的，每一个元素都自动带有一个位置信息，也就是索引。在编程语言中，无论
Python 还是其他的语言，索引都是从 0 开始，而不是 1。第 0 个索引对应的元素就是第一个元素
语法：列表名[index] 
'''
# 根据索引访问列表元素，并且赋值给变量 three_str
three_str = names_python_pc[2]
print(names_python_pc[2])
print(f'列表中的第3个元素:{three_str}')

'''
访问列表中最后一个元素的方法有两个：第一个是通过索引号[-1]来获取。这个特殊的语法
特别有用，尤其在项目中，不知道一个 excel 文件具体有多少列，但是我们记得最后一列是想要
获取的信息，此时就可以使用该方法；第二个：明确知道列表有多少列，使用最后一列的索引即
可。
'''
# 两种方法访问列表最后一个元素
names_python_pc[-1]
print(f'使用第一种方法，获得列表的最后一个元素{names_python_pc[-1]}')
names_python_pc[2]
print(f'使用第一种方法，获得列表的最后一个元素{names_python_pc[2]}')

# 添加列表元素，列表是可以变的，一般在列表中添加元素有2中情况
# 第一种，在指定位置插入一个元素， insert（index,x) 方法，
# index 是准备插入到其前面的那个元素的索引; x 为需要插入的元素。
names_python_pc.insert(0, 'Bob')
print('插入新演员的名单后的列表:{}'.format(names_python_pc))

# 第二种，在列表的末尾添加元素 append(x) x 为需要插入的元素，并且是插入到列表的最后
names_python_pc.append('Lily')
print('插入新演员的名单后的列表:{}'.format(names_python_pc))

'''
在项目开发中，第二种方法经常被用来构建一个新的列表。首先，创建一个空
的列表，然后在程序运行的过程中使用 append()方法添加元素。
'''
# 构建新的列表
a = []
a.append('lol')
a.append('Ice')
a.append('fire')
a.append('wind')
print(f'使用append()方法构建列表:{a}')

# 修改列表元素，修改列表元素与访问列表元素一样，根据索引即可修改元素的值。
# 语法 列表名[index] = 'new value'

names_python_pc[2] = 'Coco'
print(f'修改后的成员名单:{names_python_pc}')

# 删除列表元素
'''
在项目中，我们经常需要删除列表中的元素。python 可以根据索引值删除，也可以根据元
素值删除。如果我们记得要删除的元素的位置，则可以根据索引值删除，用到的是语句 del()或
者方法 pop。语句 del(index) 根据索引值删除元素，并且删除后不可以赋值给任何变量；方法
pop()删除列表尾部的元素，或者 pop(index)感觉索引值删除，但是 pop 方法删除后的元素可以
赋值给变量。这就是两者的最大区别。
语法：
del 列表名[index]  也可以用切片删除 del index[0:2] 0 1 会被删除 
列表名.pop() or 列表名.pop(index) 
'''

# 删除列表中的Bob
del names_python_pc[0]
print('del 语句删除列表中的bob后的列表是{}'.format(names_python_pc))
# POP 方法删除列表Lily
delete_name = names_python_pc.pop()
print(f'pop() 方法删除的元素是{delete_name}')
# 根据位置删除 Coco
delete_name_index = names_python_pc.pop(1)
print(f'pop(index) 根据索引删除的元素值是{delete_name_index}')

'''
如何我们不记得要删除的列表元素的位置，只是记得值，可以采用的方法是 remove()。
如果列表中有多个类似的值，则 remove()方法一次只能删除一个。
语法：
列表名.remove('值')
'''

print('原来的列表是:',names_python_pc)
names_python_pc.remove('David')
print(f'删除后的列表是{names_python_pc}')

'''
列表排序及其他
很多时候，我们需要对列表中的元素进行排序，然后进行运算。列表排序分为永久性排序和临时性排序。

永久性排序是真正修改列表元素的排列顺序，用到的方法是 sort(),默认为升序。
如果是降序，添加参数 reverse=True。
另外 sort()中有一些选项很有用，比如使用字符串的长度排序；

临时性排序是不改变原来的排列顺序，用到的函数是 sorted()。它返回一个新建的已排序列表，原来的列表顺序不受影响。
语法：
永久排序：列表名.sort()
临时性排序: sorted(列表名)
除了列表排序，列表中还有很多其他重要的方法，比如
方法 copy()复制列表
函数 len()求列表长度、
函数 reverse()反转列表等
'''
'''
 copy 复制；
 count 方法计数
 index 方法返回索引位置；
 reverse 方法实现元素颠倒；
 sort 方法排序；
 sorted 临时排序
'''
# 构建列表
list_1 = ['p', 'f', 'b', 'd', 'e', 'f', 'g']
# 复制列表
list_2 = list_1.copy()
print('复制列表:', list_2)

# 统计列表中f出现的次数
print('统计列表中f出现的次数:', list_1.count('f'))

# 查看列表中b的所在位置
print('b所在的位置', list_1.index('b'))

# 永久颠倒顺序
list_1.reverse()
print('颠倒后的元素顺序：', list_1)

# 默认升序
list_1.sort()
print('升序排列元素', list_1)

# 默认降序
list_1.sort(reverse=True)
print('降序排列元素', list_1)

# 打印列表长度
print('列表list_1的列表长度是:', len(list_1))

#sort 根据长度排序, 默认升序
names_python_pc_2 = ['Baby', 'Andy Liu', 'We', 'TFboys']
print('原来的顺序是：', names_python_pc_2)
names_python_pc_2.sort(key=len)
print('根据元素长度排序后的结果是：', names_python_pc_2)















