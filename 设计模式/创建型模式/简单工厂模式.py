"""
    优点：隐藏代码的内部实现细节

    缺点：违反了单一原则

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


# 创建一个工厂类调用支付方式
class PaymentFactory:
    def create_payment(self, methed):
        if methed == 'alipay':
            return AliPay().pay(1000)
        elif methed == 'wechat':
            return WechatPay().pay(1000)
        elif methed == 'huabei':
            return AliPay(use_huabei=True).pay(100000)
        else:
            raise TypeError('No such payment named %s' % methed)


pf = PaymentFactory()
pf.create_payment('huabei')
