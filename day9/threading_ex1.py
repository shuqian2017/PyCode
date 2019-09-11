# -*-coding:utf-8 -*-
"""
@project: code
@author: fke
@file: threading_ex1.py
@time: 2019-06-19 23:48:36
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

import threading
import time

"""
def run(n):
    print("task", n)
    time.sleep(3)

t1 = threading.Thread(target=run, args=("t1",))
t2 = threading.Thread(target=run, args=("t2",))

t1.start()
t2.start()
"""


class MyThread(threading.Thread):

    def __init__(self, n, times):
        super(MyThread, self).__init__()  # 集成父类的方法并且重构
        self.n = n
        self.sleep_time = times

    def run(self):
        print("running task", self.n)
        time.sleep(self.sleep_time)


tmp = []
start_time = time.time()
for i in range(40):
    t = MyThread(i, 2)
    t.start()
    tmp.append(t)

for t in tmp:
    t.join()

print("const:", time.time() - start_time)
