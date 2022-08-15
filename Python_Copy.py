'''

浅拷贝与深拷贝
为了让一个对象发生改变时，不对原对象产生副作用（也就是互不影响），此时，需
要一份这个对象的拷贝，python 提供了 copy 机制来完成这样的任务，对应的模块
是 copy。拷贝分为浅 copy 与深拷贝。

浅拷贝就是创建一个具有相同类型，相同值但不同 id的新对象。浅拷贝仅仅对对象自
身创建了一份拷贝，而没有在进一步处理对象中包含的子对象值（比如列表，字典等子对
象。也就是说浅拷贝对子对象不起作用，其中一个变量的子对象值被修改了，另外一个也
跟着被修改。因此使用浅拷贝的典型使用场景是：对象自身发生改变的同时需要保持对象
中的值完全相同，

比如 list 排序。
深拷贝不仅仅拷贝了原始对象自身，也对其包含的值进行拷贝，它会递归的查找对象
中包含的其他对象的引用，来完成更深层次拷贝。拷贝完成以后，两个变量为完全独立的
对象，互不影响。因此，深拷贝产生的副本可以随意修改而不需要担心会引起原始值的改变。

'''
# 浅拷贝
import copy   # 导入 copy模块
a = [7, 5, 6, ['m', 'o', 'p']]
b = copy.copy(a)   # a.copy()

print(id(a), id(b))
print(a is b)

print(F'a,{a}与 b,{b}有一样的值\n')
a.append(10)
print("浅 COPY是值互不影响\n")

print(id(a), id(b))
print('a被修改为：', a)
print('b没有被修改', b)

a[3].append('new')
print("浅 COPY不能 COPY自对象的值，a的子对象修改了， b也跟着修改\n")
print(id(a), id(b))
print('a的值也被修改为:', a)
print('b的值也被修改为:', b)
print(a is b)
print(a[3] is b[3])

# 深拷贝
print('深拷贝的例子\n')
a= [7, 5, 6, ['m', 'o', 'p']]
b= copy.deepcopy(a)
print(id(a), id(b))
print(a is b)
print(F'a,{a}与 b,{b}有一样的值\n')
a.append(10)
print("深 COPY是值互不影响\n")
print(id(a), id(b))
print('a被修改为：',a)
print('b没有被修改',b)
a[3].append('new')
print("深拷贝的子对象不会被拷贝\n")
print(id(a), id(b))
print('a的值也被修改为:',a)
print('b的值也被修改为:',b)
print(a is b)
print(a[3] is b[3])


