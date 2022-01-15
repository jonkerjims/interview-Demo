"""
    定义一个装饰器装饰多个函数,根据传入的不同值来修改
"""

# 创建装饰器
import time

def outer(arg):
    def decor(func):
        def inner():
            print(arg)
            if arg=='0':
                print('爱')
                func()
            elif arg=='1':
                print('不爱')
                func()

        return inner
    return decor


# 创建基础函数
@outer('0')
def love1(*yuanzu, **zidian):  # *yuanzu把所有的单个参数收集成为元组/**zidian把所有的关键字参数收集成为字典
    print("{}爱{}".format(yuanzu, zidian))
    return '爱'

@outer('1')
def love2(*yuanzu, **zidian):  # *yuanzu把所有的单个参数收集成为元组/**zidian把所有的关键字参数收集成为字典
    print("{}不爱{}".format(yuanzu, zidian))
    return '不爱'


# 调用函数

love2()
