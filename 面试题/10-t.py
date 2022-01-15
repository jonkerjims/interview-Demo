"""
    查看以下两种输出分别是什么
"""
# class Foo:
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         self.f1()
#
#
# class Bar(Foo):
#     def f1(self):
#         print("Bar.f1")
#
#
# obj = Bar()
# obj.f2()
# ------------result-----------
# Foo.f2
# Bar.f1

class Foo:
    def __f1(self):
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        self.__f1()


class Bar(Foo):
    def __f1(self):
        print("Bar.f1")


obj = Bar()
obj.f2()