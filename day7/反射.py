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

class Foo(object):

    def __init__(self):
        self.name = 'fke'

    def func(self):
        return 'func'

obj = Foo()

# ***检查是否含有成员***
print(hasattr(obj, 'name'))
print(hasattr(obj, 'func'))

# ***获取成员***
print(getattr(obj, 'name'))
print(getattr(obj, 'func'))

# ***设置成员***
setattr(obj, 'age', 10)
print(getattr(obj, 'age'))
setattr(obj, 'show', lambda num: num + 1)
print(getattr(obj, 'show'))

# ***删除成员***
# delattr(obj, 'name')
# delattr(obj, 'func')
