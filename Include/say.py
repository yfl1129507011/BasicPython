'''
此模块包含以下内容：
字符串变量 name
数字变量 age
say()函数
SayObj类：包含属性变量name和age, 以及say()方法
'''

name = "FenLon"
age = 27
print(name, ":", age)

def say():
    print("hello,world!")

class SayObj:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(self.name, ":", self.age)


# 测试代码 (直接运行该模块才会执行下面的代码)
if __name__ == '__main__':
    say()
    sayObj = SayObj("FenLon", 28)
    sayObj.say()
    print(__doc__)