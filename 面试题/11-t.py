"""
    类生成的实例化对象怎么才可以调用
"""

class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name,self.age)

    def __call__(self, *args, **kwargs):
        print(self, args, kwargs)


obj = Foo(1,2)
obj()
obj(1,2,5,13,51,351,53,a=1,b=2)

# obj(1,2,5,13,51,351,53,a=1,b=2)相当于

obj.__call__(1,2,5,13,51,351,53,a=1,b=2)