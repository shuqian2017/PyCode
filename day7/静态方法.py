# -*-coding:utf-8 -*-

class Dog(object):

    def __init__(self, name):
        self.name =name

    @staticmethod  # 把eat方法变成静态方法
    def eat(self):
        print("%s is eating" % self.name)


d = Dog("ZhangSan")
#d.eat()
d.eat(d)

