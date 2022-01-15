"""
    内容： 定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。
          模板方法是的子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。


"""
from abc import ABCMeta, abstractmethod
from time import sleep


class Windows(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def run(self):
        self.start()
        while True:
            try:
                self.repaint()
                sleep(5)
            except KeyboardInterrupt:
                break
        self.stop()


class MyWindow(Windows):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("窗口开始运行")

    def stop(self):
        print("窗口关闭")

    def repaint(self):
        print(self.msg)


MyWindow("Hello....").run()