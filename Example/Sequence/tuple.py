'''
元组和列表（list）的区别：
1、列表的元素是可以更改的，包括修改元素值，删除和插入元素，所以列表是可变序列
2、而元组一旦被创建，它的元素就不可更改了，所以元组是不可变序列
3、元组可以看做是不可变的列表，元组的所有元素都放在一对小括号（）中，相邻元素之间用逗号，隔开
'''


'''
Python创建元组
1、使用（）直接创建
2、使用tuple()函数创建元组
'''
num = (1, 2, 3, 4, 5)
# print(num)  # (1, 2, 3, 4, 5)
# print(type(num))  # <class 'tuple'>

course = ('数学', '语文', '英语')
# print(course)  # ('数学', '语文', '英语')
# print(type(course))  # <class 'tuple'>

abc = ('fenlon', 29, [1, 2], ('c', 3.9))
# print(abc)  # ('fenlon', 29, [1, 2], ('c', 3.9))
# print(type(abc))  # ('fenlon', 29, [1, 2], ('c', 3.9))

# 需要注意当创建元组中只有一个字符串类型的元素时，该元素后面必须要加一个逗号，否则Python解释器会将它视为字符串
a = ('fenlon', )  # 最后加逗号
# print(a)  # ('fenlon',)
# print(type(a)) # <class 'tuple'>

b = ('fenlon')
# print(b)  # fenlon
# print(type(b))  # <class 'str'>


# 将字符串转换成元组
tup1 = tuple('fenlon')
# print(tup1)  # ('f', 'e', 'n', 'l', 'o', 'n')

# 将列表转换成元组
list1 = ['a', 'b', 'c']
tup2 = tuple(list1)
# print(tup2)  # ('a', 'b', 'c')

# 将字典转换成元组
dict1 = {'a':1, 'b':2}
tup3 = tuple(dict1)
# print(tup3)  # ('a', 'b')

# 将区间转换成元组
range1 = range(1, 6)
tup4 = tuple(range1)
# print(tup4)  # (1, 2, 3, 4, 5)

'''
Python访问元组元素
'''
url = 'http://c.biancheng.net/view/4360.html'
# print(url[7])  # c
# print(url[-4])  # h
# print(url[2:8])  # tp://c
# print(url[7:20:3])  # cicnn

# 删除元组
# del url
# print(url)  # NameError: name 'url' is not defined


listDemo = []
# print(listDemo.__sizeof__())   # 40

tupleDemo = ()
# print(tupleDemo.__sizeof__())  # 24