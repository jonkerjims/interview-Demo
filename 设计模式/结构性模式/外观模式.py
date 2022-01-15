"""
    内容：为子系统中的一组件接口提供一个一致的界面，外观模式顶一个了一个高层接口，这个接口使得这个子系统更加容易使用。

    角色：
        外观：（facade）
        子系统类：（subsystem classes）

    优点：
        减少系统依赖
        提高了灵活性
        提高了安全性

"""


class CPU:
    def run(self):
        print('CPU开始运行')

    def stop(self):
        print('CPU停止运行')


class Disk:
    def run(self):
        print('Disk开始运行')

    def stop(self):
        print('Disk停止运行')


class Memory:
    def run(self):
        print('Memory开始运行')

    def stop(self):
        print('Memory停止运行')


class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


p = Computer()
p.run()
p.stop()
