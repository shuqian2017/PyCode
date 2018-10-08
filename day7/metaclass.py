__author__ = 'fke'

class MyType(type):

    def __init__(self, *args, **kwargs):
        print("Mytype __init__", *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("Mytype __call__", *args, **kwargs)
        obj = self.__new__(self)
        print("obj ", obj, *args, **kwargs)
        print(self)
        self.__init__(obj, *args, **kwargs)
        return obj
        # __call__ 调用 __new__ 调用 __init__

    def __new__(cls, *args, **kwargs):
        print("Mytype __new__", *args, **kwargs)
        return type.__new__(cls, *args, **kwargs)

print('here...')

class Foo(object, metaclass=MyType):

    def __init__(self, name):
        self.name = name
        print("Foo __init__")

    def __new__(cls, *args, **kwargs):
        print("Foo __new__", cls, *args, **kwargs)
        return object.__new__(cls)    # 继承父类的__new__方法,然后去调用构造函数

f = Foo("fke")
print("f", f)
print("fname:", f.name)
