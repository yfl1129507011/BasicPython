'''
Python中的序列类型包括列表（list），元组（tuple），字典（dict）和集合（set）
列表（list）和元组（tuple）比较相似，他们按顺序保存元素并占用一块连续的内存，每个元素都有自己的索引，
都可以通过索引来访问。他们的区别在于：列表是可以修改的，尔元组不可修改
字典（dict）和集合（set）存储的数据都是无序的，每份元素占用不同的内存，其中字典元素以key-value的形式保存
集合和字典不支持索引、切片、相加和相乘操作
'''

str1 = "Python序列索引"
str1_len = len(str1)
print("字符【", str1, "】的长度为", str1_len);
print(str1[0], "==", str1[0-str1_len])  # P == P
print(str1[5], "==", str1[5-str1_len])  # n == n

str2 = "Python序列切片"
print(str2[0:2], "==", str2[:2], "==", str2[:2:1])  # Py == Py
print(str2[:])  # Python序列切片
print(str2[::2])   # Pto序切


str3 = "Python序列相加"
print("fenlon"+"学习："+str3)   # fenlon学习：Python序列相加

str4 = "Python序列相乘"
print(str4 * 3)   # Python序列相乘Python序列相乘Python序列相乘

str5 = "检查元素是否包含在序列中"
print('元' in str5)   # True
print('f' not in str5)   # True

