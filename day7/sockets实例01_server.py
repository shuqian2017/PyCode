# -*-coding:utf-8 -*-
"""
@project: code
@author: Administrator
@file: sockets实例01_server.py
@time: 2018-10-10 10:18:09
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
sk.bind(ip_port)
sk.listen(10)

while True:
    conn,address = sk.accept()
    conn.sendall("\033[31;1m欢迎致电10086，请输入1xxx, 0转人工服务\033[0m.".encode())
    Flag = True
    while Flag:
        data = conn.recv(1024).decode()
        if data == 'exit':
            Flag = False
        elif data == '0':
            conn.sendall('\033[32;1m通过可能会被录音.balabala...\033[0m'.encode())
        else:
            conn.sendall('\033[32;1m信息有误,请重新输入.\033[0m'.encode())
    conn.close()

