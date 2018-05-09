__author__ = 'fke'
"""
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    return "---done---"

f = fib(6)
#  print(f.__next__())
# for i in f:
#     print(i)
while True:
    try:
        x = next(f)
        print("f:", x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break
"""

# 协程
import time
def consumer(name):
    print("%s 准备吃包子啦!" % name)
    while True:
        baozi = yield
        print("包子[%s]来了，被[%s]吃了!" % (baozi, name))

# 有yield时，函数变成了生成器(generator),通过next来执行。遇到yield时函数暂停跳出， send方法给yield传值
# c = consumer("fke")
# c.__next__()

def producer(name):
    c = consumer("A")
    c2 = consumer("B")
    c.__next__()
    c2.__next__()
    print("老子开始要准备做包子啦!")
    for i in range(1, 10):
        time.sleep(1)
        print("做了2个包子...")
        c.send(i)
        c2.send(i)

producer("fke")
