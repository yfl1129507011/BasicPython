'''
Python创建列表
1）使用[]直接创建列表
2）使用list()函数创建列表
'''

num = [1, 2, 3, 4, 5, 6, 7]
# print(type(num))   # <class 'list'>
# print(num)    # [1, 2, 3, 4, 5, 6, 7]
# print(num[2])  # 3
# del num
# print(num)  # NameError: name 'num' is not defined

name = list("yangfeilong")
# print(type(name))   # <class 'list'>
# print(name)  # ['y', 'a', 'n', 'g', 'f', 'e', 'i', 'l', 'o', 'n', 'g']
# print(name[:6:2])   # ['y', 'n', 'f']

info = num + name
# print(info)   # [1, 2, 3, 4, 5, 6, 7, 'y', 'a', 'n', 'g', 'f', 'e', 'i', 'l', 'o', 'n', 'g']


'''
append()方法添加元素，用于在列表的末尾追加元素
'''

l = ['Python', 'C++', 'Java']
l.append('PHP')  # 追加元素
# print(l)  # ['Python', 'C++', 'Java', 'PHP']

# 追加元素，整个元组被当成一个元素
t = ('JavaScript', 'C#', 'Go')
l.append(t)
# print(l)  # ['Python', 'C++', 'Java', 'PHP', ('JavaScript', 'C#', 'Go')]

# 追加列表，整个列表也被当成一个元素
l.append(['Ruby', 'SQL'])
# print(l)  # ['Python', 'C++', 'Java', 'PHP', ('JavaScript', 'C#', 'Go'), ['Ruby', 'SQL']]

'''
extend()方法添加元素，extend()不会把列表或者元组视为一个整体，而是把他们包含的元素逐个添加到列表中
'''
l = ['Python', 'C++', 'Java']
l.extend('C')  # 追加元素
# print(l)  # ['Python', 'C++', 'Java', 'C']

# 追加元组，元组被拆分成多个元素
t = ('JavaScript', 'C#', 'Go')
l.extend(t)
# print(l)  # ['Python', 'C++', 'Java', 'C', 'JavaScript', 'C#', 'Go']

# 追加列表
l.extend(['Ruby', 'SQL'])
# print(l)  # ['Python', 'C++', 'Java', 'C', 'JavaScript', 'C#', 'Go', 'Ruby', 'SQL']

'''
insert()方法插入元素，append()和extend()方法只能在列表末尾插入元素，如果希望在列表中间位置插入元素，那么可以使用insert()方法
当插入列表或者元祖时，insert() 也会将它们视为一个整体，作为一个元素插入到列表中，这一点和 append() 是一样的
'''
l = ['Python', 'C++', 'Java']
# 插入元素
l.insert(2, 'PHP')
# print(l)  # ['Python', 'C++', 'PHP', 'Java']

# 插入元组
t = ('C#', '.NET')
l.insert(1, t)
# print(l)  # ['Python', ('C#', '.NET'), 'C++', 'PHP', 'Java']

# 插入列表
l.insert(0, ['Ruby', 'SQL'])
# print(l)  # [['Ruby', 'SQL'], 'Python', ('C#', '.NET'), 'C++', 'PHP', 'Java']
