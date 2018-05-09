__author__ = 'fke'

"""
Python函数是先定义再调用   先定义变量->>调用变量   函数可以理解为带引号的变量,先定义->>再调用
"""

'''
装饰器定义：


实现装饰器知识储备:
1. 函数即"变量"
2. 高阶函数

    a. 把一个函数名当作实參传给另外一个函数
    b. 返回值中包含函数名

3.  嵌套函数
'''

"""
def foo():
    print('in the foo!')
    def bar():
        print('in the bar!')
    # bar()
foo()
"""


import time

def timer(func):      # TODO 3. 相当于 func = test1   timer(test1)
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print("the func run time is %s" % (stop_time-start_time))
    return deco

@timer     # TODO 2. 相当于   test1 = timer(test1)   把deco的内存地址返回给变量test1
def test1():
    print("in the test1")
    time.sleep(1)

@timer
def test2(name, age):      # TODO 4.  执行deco("fke", 24)
    print("\033[31;1mname:\t%s\n age:\t%s\033[0m" % (name, age))
    time.sleep(1.5)

# test1()   #TODO 1. 运行test1， 但是想给test1添加统计时间的功能,所以用@给test1装饰一下，看上面代码
test1()
test2("fke", 24)

