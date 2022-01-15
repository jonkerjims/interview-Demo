from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


class FastStrategy(Strategy):
    def execute(self, data):
        print('用较快的策略处理%s' % data)


class SlowStrategy(Strategy):
    def execute(self, data):
        print('用较慢的策略处理%s' % data)


class Context:
    def __init__(self, Strategy, data):
        self.data = data
        self.Strategy = Strategy

    def set_strategy(self, strategy):
        self.Strategy = strategy

    def do_strategy(self):
        self.Strategy.execute(self.data)


# Client

data = "{ ... }"
F = FastStrategy()
S = SlowStrategy()
context = Context(F, data)
context.do_strategy()

# 切换策略

context.set_strategy(S)
context.do_strategy()
