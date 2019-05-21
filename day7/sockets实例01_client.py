# -*-coding:utf-8 -*-
"""
@project: code
@author: Administrator
@file: sockets实例01_client.py
@time: 2018-10-10 10:45:44
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

import socket

ip_port = ('127.0.0.1',8888)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

while True:
    data = sk.recv(1024).decode()
    print('receive:', data)
    inp = input('please input:').strip()
    sk.sendall(inp.encode())
    if inp == 'exit':
        break

sk.close()
