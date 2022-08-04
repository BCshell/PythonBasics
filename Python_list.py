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

# 两种方法访问列表最后一个元素



