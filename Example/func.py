# 定义空函数
def func():
    pass

# print(func())  # None

# 定义普通函数
def func_1(a, b):
    print('a='+a+"\tb="+b)

# func_1('one', 'two')   # a=one	b=two

# python关键字参数，参数的顺序随意
# func_1(b='222', a='111')   # a=111	b=222


# 定义函数的默认参数
def func_2(a, b='hello'):
    print(b+' '+a)

# func_2('fenlon')  # hello fenlon
# func_2('fenlon', 'nihao')   # nihao fenlon


'''
定义python函数的可变参数的方式:
1、形参前添加一个'*'，如：*args，表示创建一个名为args的空元组，该元组可接受任意多个外界传入的非关键字实参
2、形参前添加两个'*'，如：**kwargs，表示创建一个名为kwargs的空字典
'''
def func_3(a, *b, **c):
    print(a)
    print(b)
    print(c)


'''
1
('1', '2')
{'aa': 1, 'bb': 2}
'''
# func_3(1, '1', '2', aa=1, bb=2)

'''
 传递元组*和字典**
 yfl
(1, 2, 3, 4, 5)
{'aaa': 'one', 'bbb': 'two'}
'''
tt = (1, 2, 3, 4, 5)
dd = {'aaa': 'one', 'bbb': 'two'}
# func_3('yfl', *tt, **dd)


# 返回多个值
def func_4():
    return ['曹操', '刘备', '孙权']

曹魏, 蜀汉, 东吴 = func_4()
# print(曹魏)  # 曹操
# print(蜀汉)  # 刘备
# print(东吴)  # 孙权


# 传递函数
def add(a, b):
    return a + b

def multi(a, b):
    return a * b
def my_def(a, b, dis):
    return dis(a, b)

# print(my_def(3, 4, add))  # 7
# print(my_def(3, 4, multi))  # 12


# 定义闭包函数
def aaa(a):
    def bbb(b):
        return a ** b
    return bbb

square = aaa(2)  # 计算平方
cube = aaa(3)  # 计算立方
# print(square(4))   # 16
# print(cube(3))    # 27

print()