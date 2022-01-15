"""
    优点：每个具体的产品都有一个具体的工程类，不许要修改代码
        隐藏了对象创建的现实细节

    缺点:
        每增加一个具体的产品类，就必须增加一个对应的具体工厂类

"""


from abc import ABCMeta, abstractmethod


# 创建一个支付方式的抽象类
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


# 继承Payment抽象类
class AliPay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei == False:
            print('支付宝支付{}元'.format(money))
        else:
            print('花呗支付{}元'.format(money))


# 继承Payment抽象类
class WechatPay(Payment):
    def pay(self, money):
        print('微信支付{}元'.format(money))


# 创建一个工厂抽象类，这是工程类接口
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

class AlipayFactory(PaymentFactory):
    # 实现接口中的抽象方法
    def create_payment(self):
        return AliPay()

class WechatFactory(PaymentFactory):
    # 实现接口中的抽象方法
    def create_payment(self):
        return WechatPay()

class HuabeiFactory(PaymentFactory):
    # 实现接口中的抽象方法
    def create_payment(self):
        return AliPay(use_huabei=True)


pf = HuabeiFactory()
print(pf.create_payment())
