# 创建装饰器
import time


def decor(func):
    def inner(*w1, **w2):
        print('抱抱', time.time())
        time.sleep(1)
        var = func(*w1, **w2)

        print('亲亲', time.time())
        return var

    return inner


# 创建基础函数
@decor
def love(*yuanzu, **zidian):  # *yuanzu把所有的单个参数收集成为元组/**zidian把所有的关键字参数收集成为字典
    print("{}爱{}".format(yuanzu, zidian))
    return '♥'


# 调用函数

love('爸爸', '妈妈', son='儿子', gril='女孩')
