# -*-coding:utf-8 -*-

"""
class Dog(object):
    '''属性方法的作用就是通过@property把一个方法变成一个静态属性'''

    def __init__(self, name):
        self.name = name

    @property
    def eat(self):
        print("%s is eating" % self.name)

d = Dog("ZhangSan")
# d.eat()   此时的eat已经变成一个静态属性，不是方法，想要调用不需要加()，直接d.eat即可
d.eat

"""


# 示例:
class Flight(object):

    def __init__(self, name):
        self.flight_name = name

    def checking_status(self):
        print("checking flight %s status" % self.flight_name)
        return 1

    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0:
            print("flight got canceled...")
        elif status == 1:
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")

    @flight_status.setter  #修改
    def flight_status(self, status):
        status_dic = {
            0: "canceled",
            1: "arrived",
            2: "departured"
        }
        print("\033[31;1mHas changed the flight status to \033[0m", status_dic.get(status))

    @flight_status.deleter  #删除
    def flight_status(self):
        print("status got removed...")

    def __call__(self, *args, **kwargs):
        print("构造方法的执行是由创建对象触发的，即：对象=类名();而__call__方法的执行是由对象后加括号触发的，即：对象()或者类()() ")


f = Flight("CA980")
f.flight_status
# f.flight_status = 2 此时不能在函数外直接给静态属性赋值，但是可以通过@proerty.setter装饰器再装饰一下
f.flight_status = 2  # 触发@flight_status.setter
del f.flight_status  # 触发@flight_status.deleter
f()

