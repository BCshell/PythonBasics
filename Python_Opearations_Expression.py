# Python 运算符与表达式
'''
运算符用于执行程序代码运算，会针对一个以上操作数项目来进行运算。比如
10+4=14，其中操作数是 10 和 4，运算符是“+”。Python 语言主要支持运算符类型
有：算术运算符、比较（关系）运算符、赋值运算符、逻辑运算符、位运算运算符、
成员运算符以及身份运算符。

表达式是将不同类型的数据，比如常量、变量、字典、函数等，用运算符按照一定的
规则链接起来的式子。比如，算数表达式，又被称为数值表达式，x*y,举例 8*9 =72.
这些运算符表达式在 python 控制结构中经常被用到，比如条件控制，循环等。
'''

# 算数运算符
'''
算术运算符主要包括四则运算符、求模运算符等，如下表所示，其中：a b 为两个变量
运算符 +   -   *   /   %   **  //

表达式a+b  a-b  a*b a/b  a%b a**b  a//b

描述：两个数相加  两个数相减  两个数相乘  两个数相除  两个数取模-返回除法的余数  两个数幂。a 的 b 次幂 取整除-返回商的整数部分

'''

# 比较关系运算符号
'''
比较运算符是对两个对象进行比较，常见的有等于、不等于等.具体如下表所示,a b 为两个变量
运算符         表达式                 描述
==           a==b                 比较对象是否相等，若相等，反正True; 否则 False
!=           a!=b                 比较是否不想等。若是，返回True
>            a>b                  比较是否大于，若是，返回 True
<            a<b                  比较是否小于，若是，返回 True
>=           a>=b                 比较是否大于等于，若是，返回True
<=           a<=b                 比较是否小于等于，若是，返回True
'''

# 赋值运算符
'''
赋值运算符是把简单的赋值运算符与算术运算符结合，为了使简化写法。比如 +=，便是
加法赋值运算符，意思是先执行加法，然后赋值。例子 a+=b 等价于 c= a +b ;a= c 或
者 a = a+b。具体的赋值运算符，如下表所示，a b 为两个变量
运算符     表达式                     描述
=        c=a+b 简                 单赋值运算符
+=       a+=b 等价于 a =a+b        加法赋值运算符
-=       a-=b 等价于 a= a-b        减法赋值运算符
*=       a*=b 等价于 a =a*b        乘法赋值运算符
/=       a/=b 等价于 a =a/b        除法赋值运算符
%=       a%=b 等价于 a =a%b        取模赋值运算符
**=      a**=b 等价于 a = a**b     幂赋值运算符
//=      a//=b 等价于 a =a//b      取整赋值运算符
'''
a = 7
b = 3
a +=b
print('+=算符例子: a += b;', a)
a -=b
print('+=算符例子: a += b;', a)

# 位运算符
'''
按位运算符是把数字当作二进制（二进制只有 0 和 1 两个数字，十进制就是普通的数字。比如
4 的二进制就是 0100）进行计算的。Python 中的按位运算法则如下：下表中变量 a 为 60，
b 为 13 二进制格式如下：
a=0011 1100
b=0000 1101
-----------------
a&b=0000 1100
a|b=0011 1101
a^b=0011 0001
~a =1100 0011

具体的位运算符如下表所示，a b 为两个变量
运算符         表达式         描述
&             a &b         按位与运算符：参与运算的两个值,如果两个相应位都为 1,则该位的结果为 1,否则为 0
|             a|b          按位或运算符：只要对应的二个二进位有一个为 1 时，结果位就为 1。
^             a^b          按位异或运算符：当两对应的二进位相异时，结果为 1
~             ~a           按位取反运算符：对数据的每个二进制位取反,即把 1 变为 0,把0 变为 1。~x 类似于 -x-1
<<            a <<2        左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补 0。
>>            a >>2        右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数
'''

# 运算逻辑符
'''
逻辑运算符主要是 and or 等。具体的位运算符如下表所示，a b 为两个变量
运算符     表达式      描述
and      a and b    布尔"与" . 如果 a 为 False，a and b 返回 False，否则它返回 b的计算值。
or       a or b     布尔"或" - 如果 a 是 True，它返回 a 的值，否则它返回 b 的计算值。
not      not a      布尔"非" - 如果 a 为 True，返回 False 。如果 a 为 False，它返回 True。
'''

# 成员运算符
'''
成员运算符是判断一个变量的值是不是另外一个的一部分，变量的类型可以是字符串、
列表或元组等。具体的成员运算符如下表所示，a b 为两个变量

运算符    表达式                                         描述
in      a 在 b 序列中 , 如果 a 在 b序列中返回 True。      如果在指定的序列中找到一个变量的值，则返回true，否则返回 false。
not in  a 不在 b 序列中 , 如果 a 不在 b 序列中返回 True。  如果在指定序列中找不到变量的值，则返回 true，否则返回 false。
'''
#成员运算符
my_pet = 'dog'
your_pet = 'cat'
animals = ['dog', 'rabbit', 'elephant']
if(my_pet in animals ):
    print(f"mypet,{my_pet} ,is in all animals, {animals}")
else:
    print(f'"mypet,{my_pet} ,is not in all animals, {animals}"')

if(your_pet not in animals):
    print(f'yourpet ,{your_pet}, is not in all animals, {animals}')
else:
    print(f'yourpet ,{your_pet}, is in all animals, {animals}')

# 身份运算符
'''
身份运算符是用来比较两个对象是否为同一个对象，也就是判断两个变量引用对象是
否为同一个。。而之前比较运算符中的 == 则是用来比较 2 个对象的值是否相等。在
Python 中，每一个变量有 3 个属性：name、id、value。

name 是变量名；内存的名称就是变量名。实质上，内存数据都是以地址来
标识的，根本没有内存的名称这个说法，这只是高级语言提供的抽象机制 ，方便我们操作内存数据

id 是查看该对象所在内存地址，内存的地址用于标识这个内存块

value 是变量的值。内存的数据就是变量的值对应的二进制，一切都是二进制

身份运算符则是通过这个 id 来进行判断的，id 一样就返回 true，否则返
回 false。但是对于小的整数，Python 缓存了-5 到 257 之间的所有整数，共
262 个。如果对象的类型为整数或字符串且值一样，则 x == y 和 x is y 的值都为 True。
（经测试浮点型数值，只有正浮点数符合这条规律，负浮点数不符合）；如何对象是列表、
字典、集合等，x is y 则为 False；

具体的身份运算符如下，a b 为两个变量。

运算
符      表达式                                                            描述
is     a is b, 类似 id(a) == id(b) , 如果引用的是同一个对象则返回 True         is 是判断两个标识符是不是引用自一个对象
is not a is not b ,类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True  is not 是判断两个标识符是不是引用自不同对象
'''
# 整数的比较
int_data=30
int_data_2=30
print('== 判断变量的值是不是相等：',int_data==int_data_2)
print('is 判断是不是引用同一个对象:',int_data is int_data_2)
print('变量 int_data 的内存地址是:',id(int_data))
print('变量 int_data_2 的内存地址是:',id(int_data_2))
print('\n')

#字符串的比较
str_data='dog'
str_data_2='dog'
print('== 判断变量的值是不是相等：',str_data==str_data_2)
print('is 判断是不是引用同一个对象:',str_data is str_data_2)
print('变量 str_data 的内存地址是:',id(str_data))
print('变量 str_data_2 的内存地址是:',id(str_data_2))
print('\n')

#列表比较
list_data=[1,2,3]
list_data_2=[1,2,3]
print('== 判断变量的值是不是相等:',list_data==list_data_2)
print('is 判断是不是引用同一个对象:',list_data is list_data_2)
print('变量 list_data的内存地址是',id(list_data))
print('变量 list_data_2的内存地址是',id(list_data_2))
print('\n')

#元组比较
tuple_data=('name','age','location')
tuple_data_2=('name','age','location')
print('== 判断变量的值是不是相等:',tuple_data==tuple_data_2)
print('is 判断是不是引用同一个对象:',tuple_data is tuple_data_2)
print('变量 tuple_data的内存地址是',id(tuple_data))
print('变量 tuple_data_2的内存地址是',id(tuple_data_2))
print('\n')

#字典比较
dict_data={"employee id":"0001","employeename":"Nelson",'age':38}
dict_data_2={"employee id":"0001","employeename":"Nelson",'age':38}
print('== 判断变量的值是不是相等:',dict_data==dict_data_2)
print('is 判断是不是引用同一个对象:',dict_data is dict_data_2)
print('变量 dict_data的内存地址是',id(dict_data))
print('变量 dict_data_2的内存地址是',id(dict_data_2))
print('\n')

