"""


"""

from abc import ABCMeta,abstractmethod

"""     项目一    """
# 继承抽象方法
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def pay(self, money):
        print('支付宝支付%d元' % money)


class WechatPay(Payment):
    def pay(self, money):
        print('微信支付支付%d元' % money)

"""     项目二     """

class Bankpay:
    def cost(self,money):
        print("银联支付%d元" % money)



# 类适配器

# class NewBankPay(Payment,Bankpay):
#     def pay(self, money):
#         self.cost(100)
#
# p = NewBankPay()
# p.pay(100)


# 对象适配器，通过组合来完成的代码复用
class PaymentAdapter(Payment):
    def __init__(self,payment):
        self.payment = payment

    def pay(self, money):
        if hasattr(self.payment,"cost"):
            self.payment.cost(money)
        else:
            self.payment.pay(money)


p = PaymentAdapter(Bankpay())
p.pay(100)