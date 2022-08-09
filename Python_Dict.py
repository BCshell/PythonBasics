# 什么是字典 Dict
'''
字典是另外一个 可变的数据结构， 且可存储任意类型对象，比如字符串、数字、列表等。字
典是由关键字和值两部分组成，也就是 key 和 value，中间用冒号分隔。这种结构类似于新华
字典，字典中每一个字都有一个对应的解释，具体语法如下：
语法：
字典名 = { 关键字 1：值，关键字 2：值，关键字 3：值}

key必须独一无二，但value则不必。可以有任意多个键值对值可以取任何数据类型，
但key必须是不可变的，如字符串，数或元组。
'''

# 构建一个字典，记录各宫嫔妃的年薪银子
name_dictionary = {'魏璎珞':300,'皇后':1000,'皇贵妃':800,'贵妃':600,'斌':200}
print(name_dictionary)
print('字典的数据类型表示是:', type(name_dictionary))

# 字典特性
'''
字典值可以没有限制地取任何 python 对象，既可以是标准的对象，也可以是用户定义的，
但键不行。两个重要的点需要记住：
1. 不允许同一个键出现两次：
创建时如果同一个键被赋值两次，后一个值会被记住。
'''
# 定义两个同样的关键字 Name
Dict = {'Name': 'Python', 'Age': 7, 'Name': 'Java'}
print("dict['Name']: ", dict['Name'])  # Name will be Java

'''
2. 键必须不可变：所以可以用数，字符串或元组充当，所以用列表就不行
'''
# 关键字 Name 为列表
# Dict = {['Name']:'Python', 'Age': 7}
# print ("dict['Name']: ", dict['Name'])
# Dict = {['Name']:'Python', 'Age': 7}
# TypeError: unhashable type: 'list'

'''
字典在 python 中的类型表示是 <class 'dict'>。当查看到变量的类型是 dict,则可以对
其进行字典的操作。常见的字典操作是访问字典、遍历字典等。这些操作在实际项目中经常被使
用到，比如 excel 文件读入内存以后，按照字典的方法存放。然后对其增加或删除值。

'''
# 访问字典
weiyingLuo = name_dictionary['魏璎珞']
print(f'魏璎珞的年薪是:{weiyingLuo}两')

# 添加键值对
# 语法 字典名[关键子名] = 值 （value)
# 增加贵人和常在的年薪银子
print(f'原来的后宫年薪字典是:{name_dictionary}')
name_dictionary['贵人'] = 100
name_dictionary['常在'] = 50
print(F'增加键值后的后宫年薪字典变成：{name_dictionary}')

# 修改键值对
'''
如果字典中的值不是我们想要的，可以通过修改的方法达到。以此指定字典名、用方括号括
起的键以及与该键相对应的新值。
语法：
字典名[关键字名] = 新的值
'''
# 修改字典的值，比如修改常在的年薪为 70 两
print('常在原来的年薪是{} 两'.format(name_dictionary['常在']))
name_dictionary['常在']= 70
change_ChangZai = name_dictionary['常在']
print(f'常在修改后的年薪是{change_ChangZai} 两')