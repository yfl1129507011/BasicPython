'''
Python字典（dict）是一种无序的、可变的序列
它的元素以“键值对（key-value）”的形式存储
相对的，列表（list）和元组（tuple）都是有序的序列
'''

# 使用{}创建字典
scores = {'数学': 145, '语文': 138, '英语': 147, '理综': 285}
# print(scores)   # {'数学': 145, '语文': 138, '英语': 147, '理综': 285}

# 通过fromkeys()方法创建字典
className = ['数学', '语文', '英语', '理综']
scoreDict = dict.fromkeys(className, 0)   # 可用于字典进行初始化操作
# print(scoreDict)   # {'数学': 0, '语文': 0, '英语': 0, '理综': 0}

# 通过dict()映射函数创建字典
demo = (['two', 2], ['one', 1], ['three', 3])
a = dict(demo)
# print(a)  # {'two': 2, 'one': 1, 'three': 3}


# 访问字典
三国 = {'曹魏': '曹操', '东吴': '孙权', '蜀汉': '刘备'}
# print(三国['东吴'])  # 孙权
# print(三国.get('曹魏', '该键不存在'))  # 曹操
# print(三国['ad'])   # KeyError: 'ad'
# print(三国.get('韩国', '该键不存在'))  # 该键不存在

# 删除字典
print(三国)  # {'曹魏': '曹操', '东吴': '孙权', '蜀汉': '刘备'}
del 三国
print(三国)  # NameError: name '三国' is not defined