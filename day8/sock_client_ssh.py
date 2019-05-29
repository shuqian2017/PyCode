# -*-coding:utf-8 -*-
"""
@project: code
@author: fke
@file: sock_client_ssh.py
@time: 2019-05-29 21:29:12
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

client = socket.socket()
client.connect(('localhost', 9999))

while True:
    shell = input('$:').strip()
    if len(shell) == 0:
        continue
    client.send(shell.encode('utf-8'))
    shell_res_size = client.recv(1024).decode()    # 接受命令的结果都bytes转为字符串的长度
    print('命令结果的长度为：', shell_res_size)
    client.send('消息长度收到了，请开始发送正式的内容吧'.encode('utf-8'))   # 配合server端解决粘包的问题
    received_size = 0
    received_data = b''
    while received_size < int(shell_res_size):
        data = client.recv(1024)
        received_size += len(data)              #
        received_data += data
    else:
        print('shell res receive done...', received_size)
        print(received_data.decode())

client.close()
