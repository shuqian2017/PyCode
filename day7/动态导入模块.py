# -*-coding:utf-8 -*-
"""
@project: code
@author: fke
@file: 动态导入模块.py
@time: 2019-05-28 23:31:44
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
'''
(和本目录lib配合使用)
# 方式一: python解释器内部使用的
mod = __import__('lib.aa')  # 相当于mod = lib
obj = mod.aa.C()
print(obj.name)
'''


# 方式二:  官方建议使用的动态导入模块的方式
import importlib
aa = importlib.import_module('lib.aa')   # 官方建议使用这个
obj = aa.C()
print(obj.name)


assert type(obj.name) is str
print('assert 断言成功')



