"""
    单例模式：

"""

from abc import ABCMeta,abstractmethod

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):  # 如果没有实例就创造一个实例
            cls._instance = super(Singleton, cls).__new__(cls) # 用他的父类去创造一个实例出来
        return cls._instance

class MyClass(Singleton):
    def __init__(self,a):
        self.a = a


a = MyClass(10)
b = MyClass(20)
"""
    因为指向的是同一个实例所以值一样
    在创建两个实例后已经迭代覆盖了
    发生在打印前
"""
