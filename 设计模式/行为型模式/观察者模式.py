"""


"""

from abc import ABCMeta,abstractmethod


class Observer(metaclass=ABCMeta):  # 抽象订阅者
    @abstractmethod
    def update(self, notice):  # notice 是一个Notice类的对象
        pass


class Notice:   # 抽象发布者
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)
        print(self.observers)

    def detach(self, obs):
        self.observers.remove(obs)
        print(self.observers)

    def notify(self): # 推送
        for obs in self.observers:
            obs.update(self)


class StaffNotice(Notice):
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()


# obj = StaffNotice('abc')
# obj.company_info = 'xyz'
# print(obj.company_info)


class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


notice = StaffNotice('初始公司信息')
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
# notice.detach(s2)
notice.company_info = "发工资了"

print(s1.company_info)
print(s2.company_info)
