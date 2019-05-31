# -*-coding:utf-8 -*-
"""
@project: code
@author: fke
@file: ftp_client.py
@time: 2019-05-31 01:56:10
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

client = socket.socket()

client.connect(('localhost', 9999))

while True:
    shell = input('>>>:').strip()
    if len(shell) == 0:
        continue
    if shell.startswith('get'):
        client.send(shell.encode())
        server_response = client.recv(1024).decode()  # 服务端先给客户端发送文件的大小
        print('[ server response] :', server_response)
        client.send(b'ready to recv file')
        file_total_size = int(server_response)
        recevied_size = 0
        filename = shell.split()[1]  # 获取输入的文件名
        f = open('new_' + filename, 'wb')
        m = hashlib.md5()

        while recevied_size < file_total_size:
            if file_total_size - recevied_size > 1024:  # 说明要收不止一次
                size = 1024
            else:  # 最后一次收了,还剩余多少就收多少
                size = file_total_size - recevied_size
            data = client.recv(size)
            recevied_size += len(data)
            m.update(data)
            f.write(data)
        else:
            new_file_md5 = m.hexdigest()
            print('[ file recv done ] :', recevied_size, file_total_size)
            f.close()
        server_file_md5 = client.recv(1024)
        print('server_file_md5 : {}, client_file_md5 : {}'.format(server_file_md5, new_file_md5))

client.close()
