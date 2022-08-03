# format格式化输出
name = 'python'
print('my favorite program langauge is {}'.format(name))
print(f'my favorite program langauge is {name}') # python 3.6后的用法

# 字符串的基本用法
# \n change lines
# \t 制表符，添加空格的方法
print('welcome to python real world,\n')
print('\t what kind of centents you want to study from python,please leave the message')

# 链接字符串，使用加号+
log_1_str = 'The error is a bug,'
log_2_str = 'We should fix it.'
log_str = log_1_str + log_2_str
print('\n 拼接后的字符串是: ',log_str)

#字符串的常见运算
#函数和方法，函数是一个独自完成特定任务的独立代码块，可以被调用；方法是面向编程语言中使用的名词.
#Python是面向对象的编程语言，面向对象 就是一切都是对象，比如你我他，统一是people,人就是一个对象。
#人可以run,run就是一个方法。合起来就是people.run()

#使用方法修改字符串的大小写
welcome = 'hell0, Welcome to python pratical circle'
# 每个单词的首字母大写，title()
print('\n 每个单词的首字母大写:',welcome.title())
# 段落的首字母大写， capitalize()
print('\n 段落的首字母大写:', welcome.capitalize())
# lower(),所以字母小写
print('\n 所有字母小写:',welcome.lower())
# upper,所有字母大写
print('\n 所有字母大写: ',welcome.upper())
# 大写转小写，小写转大写
print('\n 大写转小写，小写转大写: ',welcome.swapcase())

# String.isalnum() 判断字符串中是否全部为数字或者英文,符合就返回 True，
# 不符合就返回 False，如果里面包含有符号或者空格之类的特殊字符也会返回False
print('\n 半段字符串是否全部为数字或者英文False',welcome.isalnum())

#String.isdigit()判断字符串是否全部为整数
print('\n 判断字符串是否全部为整数',welcome.isdigit())

# 字符串分割
# 按照某种特定的方法，把字符串分割开成列表，这个在数据分析中经常用到
string_example = 'Now is better than ever.'
print('分割字符串:', string_example.split())
#按某个一个字母分割
print('按照指定的字母分割字符串:',string_example.split('n'))

#去掉换行符，以换行符分割成列表
print('以换行符为分割','1+2\n+3+4'.splitlines())

# 字符串删除两边空白，在数据清理的时候经常被用到。常见的操作是去除两端或者一段的空白
love_python = ' Hello, Python Pratical Circle '
# 去除字符串两边的空白
print('去除字符串两边的空白',love_python.strip())
# 去除字符串右边的空白
print('去除字符串右边的空白',love_python.rstrip())
# 去除字符串左边的空白
print('去除字符串左边的空白',love_python.lstrip())
# python 中的字符串操作非常的多，以上只是列出了部分常用的操作。以后我们学习
# 过程中慢慢补充。有一点需要注意的是 python 中的字符串并不允许修改值，只允许覆盖值。
# 也就是字符串只能重新赋值，不能修改其中的一个字母。

# 字符串的切片
# 切片操作(slice)是Python中经常用到的操作，字符串的切片就是可以从一个字符串中获取字符串（字符串的一部分）
# 我们使用一对括号、起始偏移量是start、终止偏移量end以及可选的步长step来定义一个分片
# 格式 [start:end:step], 左侧第一个字符的位置/偏移量为 0，右侧最后一个字符的位置/偏移量为-1
# [:]提取从开头（默认位置0)到结尾（默认位置-1)的整个字符床
# [start:] 从start提取到结尾
letter = 'ancgfdjjksjkskjk'
print(letter[-3:])
print(letter[0:])
# [:end] 从开头取到end -1
print(letter[:-1])
# [start:end] 从start提取到end-1
print(letter[0:-1])
#[start:end:step] 从 start 提取到 end - 1，每 step 个字符提取一个
print(letter[0:-1:2])

# 字符串的编码问题，当我们的源代码里面包含中文的时候，就需要务必指定保存为UTF-8编码
