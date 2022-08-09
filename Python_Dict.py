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

# 删除键值对
'''
如果字典中的键值对不再需要，我们可以彻底删除。Python 使用的是 del 语句，必须要指
定要删除的字典名和关键字。注意是永久删除
语法：
del 字典名[关键字]
'''
# 删除字典中的键值对，比如删除常在
del name_dictionary['常在']
print(f'删除常在后的后宫嫔妃年薪字典变成:{name_dictionary}')

'''
如果我们还需要用到被删除的键值对，则我们使用 pop(‘键的名字’)方法。
该方法是删除字典给定键所对应的值，并且返回该值。
'''
print('原来的字典是:', name_dictionary)
# 使用 pop 方法删除魏璎珞
name_pop = name_dictionary.pop('魏璎珞')
# 使用删除后的值
print('魏璎珞的年薪是:',name_pop)
print('使用 pop 方法删除后的字典是:',name_dictionary)

'''
除了 pop()方法以外， Python 中还有一个 popitem()方法。它可以随机删除字典中的一对
（一般删除末尾一对），并且可以被后续的程序使用。我们经常用此方法逐个删除字典中的所有键值对。
'''

# 随机删除字典中的一对
pop_name = name_dictionary.popitem()
print('使用 popitem 删除的是：', pop_name)
print('随机删除字典中一对键值对后：', name_dictionary)
pop2_name = name_dictionary.popitem()
print('再次使用 popitem 删除的是:', pop2_name)
print('再次随机删除字典中一对键值对后：', name_dictionary)

'''
如果需要删除所有的键值对，我们可以使用 clear()方法清空所有的数据。但是需要注意 del
语句是删除字典，此时打印删除后的字典则出错。两者是有区别的。
'''
# clear()方法清除字典中的所有数据
# print('原来字典的长度是:', len(name_dictionary))
# name_dictionary.clear()
# print('使用 clear 清除字典中的所有内容:', name_dictionary)
# print('清空以后字典的长度是:', len(name_dictionary))

# 使用 del 删除字典
# del name_dictionary
# 字典已经被删除，则再次打印则出错：name 'name_dictionary' is not defined
# print(name_dictionary)

# 创建空字典
'''
在实际项目中，我们可能不知道字典中存放的内容是什么。这时，我们可以采用从空的字典
开始动态创建，也就是在程序运行的时候添加具体的内容。
常见的使用场景是：第一个：需要用户输入数据存储为字典；第二个是自动生成大量的键值对，
比如爬虫，爬取豆瓣电影的排名信息。我们可以把排名放入空的字典中，然后每次爬取一个
电影，添加一个对应的键值对。
'''
# 从空的字典开始创建
douban_movies = {}  #定义空的字典
douban_movies['排名'] = 1
douban_movies['片名'] = '霸王别姬'
douban_movies['主演'] = '张国荣、张丰毅、巩俐'
douban_movies['导演'] = '陈凯歌'
print('从空的列表中构建字典:', douban_movies)

# 内置字典函数与方法
'''
内置函数
len(dict) #计算字典元素个数，即键的总数。
str(dict) #输出字典可打印的字符串表示。
and so on

内置方法
字典名.clear() # 删除字典内所有元素
字典名.copy() # 返回一个字典的浅复制
字典名.fromkeys() # 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的
初始值
字典名.get(key, default=None) # 返回指定键的值，如果值不在字典中返回 default 值
字典名.items() # 以列表返回可遍历的(键, 值) 元组数组
字典名.keys() # 以列表返回一个字典所有的键
字典名.setdefault(key, default=None) # 和 get()类似, 但如果键不已经存在于字典中，将
会添加键并将值设为 default
字典名.update(dict2) # 把字典 dict2 的键/值对更新到 dict 里
字典名.values() # 以列表返回字典中的所有值

'''
# 内置函数和方法
print('计算字典的个数：', len(name_dictionary))
print('输出字典可以打印的字符串', str(name_dictionary))
# 内置函数
print('返回指定的贵妃的年薪', name_dictionary.get('贵妃'))
print('以列表的形式返回字典中的所有关键字,', name_dictionary.keys())  #经常被用到
print('以元组形式返回所有的键值对', name_dictionary.items())  #经常被用到
print('返回键值中的所有值', name_dictionary.values()) #经常被用到

'''
在所有内置方法中，update()方法经常被用来合并两个字典。如果传给 update 方法的数据
也含有相同的键，则它的值将被覆盖。
'''

new_dictionary = {'皇后': 1000, '皇贵妃': 800, '贵妃': 600}
print('第一个字典：', new_dictionary)
name = {'魏璎珞': 300, '贵人': 100}
print('第二个字典:', name)
# 使用 update 方法合并两个字典
new_dictionary.update(name)
print('使用 update 方法合并两个字典:', new_dictionary)
# 如果有重复的值则替换
name_new = {'皇后':1500, '贵人':110}
# 使用 update 方法合并两个字典
new_dictionary.update(name_new)
print('使用 update 方法合并两个字典:', new_dictionary)

# 结合字典和列表
'''
字典和列表是 python 中经常用到的两个数据结构，并且都是可变的。有时候，我们需要把
两者结合起来使用。把一系列字典 存储在 列表 中，或 将列表作为值 放在 字典中，这称为 嵌套。

可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。这在项目中经常用到。
'''

'''
什么时候用列表什么时候用字典呢？面对这个问题笔者的想法是，当你存取的数据类型都
是一样的时候，使用列表，当你存取的数据类型不一样时就用字典, 这里说明一下数据类型不一样不是指整形或者字符型。
举个例子：如果你需要存很多人的姓名，仅仅这一个属性，就用列表来进行处理，
当你要存取不仅仅是人名，包括年龄，性别，国籍等等这些信息时，这时候用字典是最合适的。
'''

# 字典列表
'''
列表中的元素都是字典 为字典列表。一般用在列表的元素信息比较复杂，单一的字符串不能满足。
'''
# 两个字典合并为一个列表
dict_1 = {'name':'Python', 'age':18}
dict_2 = {'name':'Java', 'age':'unknown'}
name_list = [dict_1, dict_2]
print(name_list)
print('类型是：\n', type(name_list))

# 在字典中存储列表
'''
字典中的值有时候不是一个，而是多个。这时需要把字典中的值变成一个列表，而不是单个的值。
'''
# 字典中存储列表
favorite_actor = {
 '魏璎珞':['傅恒', '皇上', '富察皇后'],
 '皇上':['魏璎珞', '富察皇后', '纯妃', '高贵妃'],
 '高贵妃':'皇上'
}
print(favorite_actor)
print('类型是:\n',type(favorite_actor))

# 在字典中存储字典
'''
字典的值也可以是字典，称为字典中存储字典。一般用在键对应的值是二维的信息，比如登
录某一个网站的用户信息，用户名是键，用户名对应的值比较部分，既包括用户的地址、职业、
收入等信息。
'''
users = {
 '爱上不该爱的人': {
 '姓名':'魏璎珞',
 '职位':"妃子",
 '年薪':'300 两',},
 '只爱皇上':{
 '姓名':'高贵妃',
 '职位':'贵妃',
 '年薪':'800 两',}
}
print(users)
print('类型是',type(users))