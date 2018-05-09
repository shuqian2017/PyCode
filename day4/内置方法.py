__author__ = 'fke'

code = "for i in range(10):print(i)"
compile(code, "error.log", "exec")
#exec(code)

print(divmod(5, 2))  # 商和余数

calc = lambda n: print(n)
calc(3.5)

res = filter(lambda n: n > 5, range(10))    # filter过滤
for i in res:
    print(i)

print('黄金分割线'.center(40, '-'))
res = map(lambda n: n * 2, range(10))
for i in res:
    print(i)

import functools
res = functools.reduce(lambda x,y: x*y, range(1, 10))
print(res)

print(round(3.1415926, 4))  # 保留几位小数

a = {6:2, 4:3, 9:1, 7:5, 3:8}
print(sorted(a))
print(sorted(a.items()))
print(sorted(a.items(), key=lambda x:x[1]))  # 按value排序 x[0]按key排序


a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd', 'e']
for i in zip(a, b):
    print(i)

import os, sys
print((__file__))
print(os.path.dirname((__file__)))
print(os.path.dirname(os.path.dirname((__file__))))
print(sys.path)


import random
print(random.random())
print(random.randint(1,5))
print(random.randrange(1,5))


import os
#os.chdir('c:\\Users\\fke')
#os.chdir(r'c:\Users\fke')

print(os.getcwd())
print(os.listdir('..'))   # '..'当前目录的父目录
#print(os.stat(r'C:\Users\Default'))

print(os.path.split(r'G:\old_boy(python)\day4\内置方法.py'))   # 拆分为2部分，路径+文件名

import shutil
shutil.make_archive("archive_test", "zip", root_dir=r'G:\old_boy(python)\day4')



