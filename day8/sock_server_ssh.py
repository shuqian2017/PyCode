# -*-coding:utf-8 -*-
"""
@project: code
@author: fke
@file: sock_server_ssh.py
@time: 2019-05-29 00:44:35
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
import os

server = socket.socket()
server.bind(('localhost', 9999))
server.listen()

while True:
    conn, addr = server.accept()
    print('[ new conn]:', addr)
    while True:
        print("等待新的操作指令")
        data = conn.recv(1024).decode()
        if not data:
            print("客户端已经断开连接")
            break
        print('[ 执行新的指令 ]', data)
        shell_res = os.popen(data).read()   # 接受的字符串指令，所以执行之前需要将bytes转化一下为str
        print('[ before send ]:', len(shell_res.encode()))
        if len(shell_res) == 0:
            shell_res = ' shell command is null...'

        conn.send(str(len(shell_res.encode())).encode())
        conn.send(shell_res.encode('utf-8'))
        print('[ send done ]')

server.close()
