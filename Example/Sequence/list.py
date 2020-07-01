'''
Python创建列表
1）使用[]直接创建列表
2）使用list()函数创建列表
'''

from collections import deque

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


'''
# 在Python列表中删除元素分为3种场景
1. 根据目标元素所在位置的索引进行删除，可以使用del关键字或者pop()方法
2. 根据元素本身的值进行删除，可以使用列表（list类型）提供remove()方法
3. 将列表中所有的元素全部删除，可使用列表（list类型）提供的clear()方法
'''
# del 根据索引值删除元素
lang = ['Python', 'C++', 'Java', 'PHP', 'JavaScript', 'Go', 'Ruby']
del lang[3] # 删除单个元素
# print(lang)  # ['Python', 'C++', 'Java', 'JavaScript', 'Go', 'Ruby']
del lang[-2]
# print(lang)  # ['Python', 'C++', 'Java', 'JavaScript', 'Ruby']
del lang[1:3] # 删除一段连续的元素
# print(lang)

# pop(): 根据索引值删除元素
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
nums.pop(2)
# print(nums) # [1, 2, 4, 5, 6, 7, 8, 9, 0]
nums.pop()
# print(nums)  # [1, 2, 4, 5, 6, 7, 8, 9]

# remove(): 根据元素值进行删除
nums = [40, 36, 88, 36, 78, 95, 64, 28]
nums.remove(40)
# print(nums)  # [36, 88, 36, 78, 95, 64, 28]
nums.remove(36)
# print(nums)  # [88, 36, 78, 95, 64, 28]
nums.remove(36)
# print(nums)  # [88, 78, 95, 64, 28]

# clear(): 删除列表所有元素
name = list('yangfeilong')
# print(name) # ['y', 'a', 'n', 'g', 'f', 'e', 'i', 'l', 'o', 'n', 'g']
name.clear()
# print(name)  # []

'''
Python 提供了两种修改列表（list）元素的方法，你可以每次修改单个元素，也可以每次修改一组元素（多个）
'''
# 修改单个元素
# nums = [1, 2, 3, 4, 5]
nums = list(range(1, 6))
# print(nums)
nums[0] = 10
nums[-1] = 50
# print(nums)  # [10, 2, 3, 4, 50]

# 修改一组元素
nums[1:3] = [20, 30]  # 修改第 1~3 个元素的值（不包括第3个元素）
# print(nums)  # [10, 20, 30, 4, 50]


'''
Python 列表（list）提供了 index() 和 count() 方法，它们都可以用来查找元素。
'''
# index()方法
nums = [12, 23, 34, 45, 56, 67, 78, 89, 90, 12, 32, 23, 43, 34, 56]
# print(nums.index(12)) # 0
# print(nums.index(12, 1)) # 9  检索索引1后面的元素
# print(nums.count(12))  # 2

'''
collections模拟实现栈和队列
'''
stack = deque()
stack.append(1)
stack.append(2)
stack.append('yfl')
# print(stack) # deque([1, 2, 'yfl'])
# print(list(stack)) # [1, 2, 'yfl']

stack.popleft()
# print(stack)  # deque([2, 'yfl'])
stack.pop()
# print(stack)  # deque([2])
stack.append('abc')
# print(stack)  # deque([2, 'abc'])
