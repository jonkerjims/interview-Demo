"""
    可以把简单的事情， 组合起来， 形成复杂的模式

"""
from abc import ABCMeta, abstractmethod


class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '点(%s, %s)' % (self.x, self.y)

    def draw(self):
        print(str(self))


class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "线段[%s, %s]" % (self.p1, self.p2)

    def draw(self):
        print(str(self))


class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print('-------复合图形----------')
        for g in self.children:
            g.draw()
        print('-------简单图形----------')


Line(Point(1, 1), Point(2, 2)).draw()
