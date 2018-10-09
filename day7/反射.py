# -*-coding:utf-8 -*-
"""
@project: code
@author: fke
@file: 反射.py
@time: 2018-09-27 01:26:
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG。   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

# 通过字符串映射或修改程序运行时的状态，属性，方法有如下的方法
'''
def getattr(object, name, default=None):
    """
    getattr(object, name[, default]) -> value
    Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
    When a default argument is given, it is returned when the attribute doesn't exist;; without it, an exception is raised in that case.
    """
    pass

def hasattr(object, name):
    """
    判断object 中有没有一个name字符串对应的方法或属性
    """
    pass

def setattr(x, y, v):
    """
    Sets the named attribute on the given object to the specified value.
    setattr(x, y, v) is equivalent to 'x.y = v'
    """
    pass

def delattr(x, y):
    """
    Deletes the named attribute from the given object.
    delattr(x, 'y') is equivalent to 'del x.y'
    """
    pass
'''

def bulk(self):
    print("%s is yelling..."% self.name)

class Dog(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating..." % self.name,food)

d = Dog("旺财")
choice = input(">>>").strip()

if hasattr(d, choice):
    print(getattr(d,choice))
else:
    # setattr(d,choice,bulk) # 动态的加载一个类以外的方法
    # d.talk(d)
    setattr(d,choice,bulk) # d.talk = bulk
    func = getattr(d, choice)
    func(d)
