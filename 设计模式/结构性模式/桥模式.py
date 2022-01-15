#
"""
    桥模式
    把代码完整的读完才能看懂
    内容： 把一个事务的两个维度分离，使其都可以独立的变化

"""
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    def __init__(self,color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):
    name = '长方形'
    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    name = '圆形'
    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print('红色的%s' % shape.name)


class Green(Color):
    def paint(self, shape):
        print('绿色的%s' % shape.name)


shape = Rectangle(Green())
shape.draw()



















# class Shape:
#     pass
#
#
# class Line(Shape):
#     pass
#
#
# class Rectangle(Shape):
#     pass
#
#
# class Circle(Shape):
#     pass
#
#
# class RedLine(Line):
#     pass
#
#
# class GreenLine(Line):
#     pass
#
#
# class BuleLine(Line):
#     pass



