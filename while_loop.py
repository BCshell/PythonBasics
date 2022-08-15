'''
while 循环
Python 提供了另一种循环模式即无限循环，不需要提前知道循环次数，那就是
while 环。while 循环一直执行，指导制定的条件不满足为止。
语法：
while 条件：
语句组 1
循环也是以冒号(:)结尾
条件为各种算术表达式，
a) 当为真时，循环体语句组 1，重复执行
b) 当为假是，循环体语句组 2，停止执行
如果循环体忘记累计，条件判断一直为真，则为死循环。循环体一直实行
a) 死循环有时候经常被用来构建无限循环
b) 可以使用 ctrl+c 终止，或者停止 IDE

for 适用于已知循环次数的循环
while 适用于未知循环次数的循环

for 通常用于遍历可迭代对象
while 很少进行遍历使用

for 循环是在序列穷尽时停止，
while 循环是在条件不成立时停止。
'''

#构造计数器，记录 5次
print('使用 while循环构造计数器，并且记录 5次')
count_number = 0
while count_number <= 5:
    print(f'\t当前数字是 {count_number}')
    count_number+=1  # z循环下一次的值，如果忘记则为死循环

'''
为了更好的体验，程序有时候使用用户输入。在 Python 中使用函数 input()让程序
暂停工作，等待用户输入后接着执行。当使用该函数时，一定要指出清晰而易于明白的指
示，否则用户不知道要输入什么内容。

'''
#计算任意数的和, 并计算出平均数.当用户输入 n时，退出
# sum = 0
# count = 0
# data = 'yes'
# while 'y' in data:
#     x = int((input('please enter a number:')))
#     sum = sum + x
#     count +=1
#     data = (input('do you have a number:(y or n)'))
#
# print('\nThe average of the nubers',sum/count)

'''
break 与 continue 语句 
break 与 continue 语句可以在循环结构中使用,比如 for,while。
break 语句是立即退出 while 循环，不再运行循环中余下的代码，也不管条件判断的结果是否为真。
break 语句经常被用来控制程序执行流，也就是控制哪些代码可以执行，哪些代码不执行。

continue 语句是结束本次循环，返回到 while 语句开始的位置，接着条件判断。如果为真，程序接着执行，
否则退出。也就是当循环或判断执行到 continue 语句时,continue 后的语句将不再执行,会跳出当次循环,
继续执行循环中的下一次循环.

两者的区别是
continue 语句跳出本次循环,只跳过本次循环 continue 后的语句
break 语句跳出整个循环体,循环体中未执行的循环将不会执行

'''
for i in range(101):
    if i == 50:
        print(f'你是第{i},请接着报数')
        continue
    if i==60:
        print(f'你是第{i},停止报数')
        break

'''
使用 while 操作列表和字典
列表和字典可以存储大量信息。for 循环可以变量其每一个元素或者键值对，但是最
好不要在 for 循环修改其值，否则导致 python 不能正常运行；如果遍历列表或字典的同
时，修改其值，可以使用 while 循环。

'''

