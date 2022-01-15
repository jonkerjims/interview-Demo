"""
    内容： 为其他对象提供一种代理以控制对这个对象的访问。

"""

from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, outfile):
        pass


class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r', encoding='utf-8')
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding='utf-8')
        f.write(content)
        f.close()


# subj = RealSubject('text.txt')
# print(subj.get_content())
# subj.set_content('outfile.txt')

# 虚拟代理
class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)

# 保护代理
class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, outfile):
        raise PermissionError('无写入权限')

virsub = VirtualProxy('text.txt')
virsub.set_content('666')

# prosub = ProtectedProxy('text.txt')
# print(prosub.get_content())
# prosub.set_content('abc')
