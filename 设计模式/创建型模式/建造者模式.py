"""
    建造者模式与抽象工厂模式相似，也用来创建复杂对象。主要区别是建造者模式着重一步步构造一个复杂对象，而抽象工厂模式着重于多个系列的产品对象
    优点：
        隐藏了一个产品的内部结构和装配过程
        将构造代码与表示代码分开
        可以对构造过程进行更精细的控制

"""


from abc import ABCMeta, abstractmethod

# 创建一个角色类
class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s,%s,%s,%s," % (self.face, self.body, self.arm, self.leg)

# 建立一个抽象类作为接口 //相当于文档
class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass

# 创建一个角色
class SexyGirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = '漂亮脸蛋'

    def build_body(self):
        self.player.body = '苗条'

    def build_arm(self):
        self.player.arm = '漂亮胳膊'

    def build_leg(self):
        self.player.leg = '大长腿'


# 创建一个怪兽角色
class guaisouBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = '漂亮脸蛋'

    def build_body(self):
        self.player.body = '苗条'

    def build_arm(self):
        self.player.arm = '漂亮胳膊'

    def build_leg(self):
        self.player.leg = '大长腿'

# 控制组装顺序
class PlayerDirector:
    def builder_player(self,builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player



builder = SexyGirlBuilder()
director = PlayerDirector()
p = director.builder_player(builder)
print(p)























# class Cat:
#     """定义一个猫类"""
#
#     def __init__(self, new_name, new_age):
#         """在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""
#         # self.name = "汤姆"
#         # self.age = 20
#         self.name = new_name
#         self.age = new_age  # 它是一个对象中的属性,在对象中存储,即只要这个对象还存在,那么这个变量就可以使用
#         # num = 100  # 它是一个局部变量,当这个函数执行完之后,这个变量的空间就没有了,因此其他方法不能使用这个变量
#
#     def __str__(self):
#         """返回一个对象的描述信息"""
#         # print(num)
#         return "名字是:%s , 年龄是:%d" % (self.name, self.age)
#
#     def eat(self):
#         print("%s在吃鱼...." % self.name)
#
#     def drink(self):
#         print("%s在喝可乐..." % self.name)
#
#     def introduce(self):
#         # print("名字是:%s, 年龄是:%d" % (汤姆的名字, 汤姆的年龄))
#         # print("名字是:%s, 年龄是:%d" % (tom.name, tom.age))
#         print("名字是:%s, 年龄是:%d" % (self.name, self.age))
#
#
# # 创建了一个对象
# tom = Cat("汤姆", 30).introduce()
# print(Cat("汤姆", 30))