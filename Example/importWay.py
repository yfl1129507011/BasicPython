'''
python包导入方式
如果模块名中包含空格或者以数字开头，就需要使用 Python 提供的 __import__() 内置函数引入模块
例如：1demo.py
__import__("1demo")
'''

# import Include.say
# Include.say.say()

# import Include.say as say
# say.say()

# from Include.say import say
# say()

# from Include.say import say as s
# s()

# import Include.say

if __name__ == "__main__":
    print(__doc__)