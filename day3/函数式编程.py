__author__ = 'fke'

import time
def logger():
    time_format = "%Y-%m-%d %X"
    time_current = time.strftime(time_format)
    with open("test1.txt", "a+", encoding="utf-8") as f:
        f.write("书神那个最帅的男人\n")

def test1():
    print("第一个测试")
    logger()

def test2():
    print("第二个测试")
    logger()

def test3():
    print("第三个测试")
    logger()

test1()
test2()
test3()


"""
位置参数： *args  tuple
关键字参数 **kwargs  dict
"""

# TODO 局部变量和全局变量 \
# 定义的局部变量如果是[], {}, 集合等 局部被修改后，全局也生效


