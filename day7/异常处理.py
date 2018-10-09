# -*-coding:utf-8 -*-
"""
@project: code
@author: fke
@file: 异常处理.py
@time: 2018-10-10 01:14:
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
data={}

try:
    # data['name']
    open("test.txt")
except (KeyError, IndexError) as e:
    print("没有这样的Key:",e)
except IndexError as e:
    print("列表操作错误:",e)
except Exception as e:
    print("未知的错误",e)