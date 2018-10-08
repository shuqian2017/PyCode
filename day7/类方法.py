# -*-coding:utf-8 -*-

class Dog(object):
    '''类方法通过@classmethod装饰器实现，类方法和普通方法的区别是，类方法只能访问类变量，不能访问实例变量'''
    name = '我是类变量'

    def __init__(self, name):
        self.name = name    # 实例变量

    @classmethod
    def eat(self):
        print("%s is eating" % self.name)

d = Dog("ZhangSan")
d.eat()
