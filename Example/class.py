class 三国:
    def __init__(self, *country):
        self.country = country

    # 定义类方法：类方法需要使用@classmethod，和至少一个参数cls
    @classmethod
    def decs(cls):
        print('滚滚长江东逝水，浪花淘尽英雄')

    # 定义静态方法：静态方法需要使用@staticmethod修饰
    @staticmethod
    def summary():
        print('三国演义')

    # 定义私有方法
    def __display(self):
        for c in self.country:
            print(c)

    def dis(self):
        self.__display()

# 调用类方法
三国.decs()   # 滚滚长江东逝水，浪花淘尽英雄

# 调用静态方法
三国.summary()  # 三国演义
cc = ('魏', '蜀', '吴')
SG = 三国(*cc)
SG.summary()   # 三国演义

'''
魏
蜀
吴
'''
SG.dis()