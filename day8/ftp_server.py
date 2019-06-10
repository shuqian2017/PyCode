# -*-coding:utf-8 -*-
"""
@project: code
@author: fke
@file: ftp_main.py
@time: 2019-05-31 01:55:56
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
import hashlib
import os

server = socket.socket()
server.bind(('localhost', 9999))
server.listen()

while True:
    conn, addr = server.accept()
    print('[ new conn] :', addr)

    while True:
        print("服务端等待新的指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已经断开了")
            break

        shell, filename = data.decode().split()
        print('要发送的文件名为：', filename)
        if os.path.isfile(filename):
            f = open(filename, 'rb')
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode())  # 告诉客户端要发送的这个文件的大小
            conn.recv(1024)  # 中间加一个recv阻塞，解决粘包的问题，保证2个发送是分开的
            for line in f:
                m.update(line)
                conn.send(line)
            print('[ file md5 ] :', m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode())  # 把文件的源md5发送给客户端

        print("send done")
server.close()
