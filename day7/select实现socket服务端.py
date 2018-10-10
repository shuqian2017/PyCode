# -*-coding:utf-8 -*-
"""
@project: code
@author: Administrator
@file: select实现socket服务端.py
@time: 2018-10-10 18:28:56
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

import select
import socket
import sys
import queue

# 创建套接字并设置该套接字为非阻塞模式
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# 绑定套接字
server_address = ('127.0.0.1', 8888)
print(sys.stderr, "starting up on %s port %s" % server_address)
server.bind(server_address)

# 将socket变成服务模式
server.listen(5)

# 初始化读取数据监听列表,最开始希望从server这个套接字上读取
inputs = [server]

# 初始化写入数据监听列表，最开始并没有客户端，所以列表为空
outputs = []

message_queues = {}
while inputs:
    print(sys.stderr, "waiting for the next event")
    # 调用select监听所有的监听列表中的套接字，并将准备好的套接字加入到对应的列表中
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    # 处理可读写套接字
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            print(sys.stderr, "connection from", client_address)
            connection.setblocking(0)  # 设置非阻塞
            inputs.append(connection)
            message_queues[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print(sys.stderr, "received '%s' from %s" % (data, s.getpeername()))
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                print(sys.stderr, "closing", client_address)
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]

    # 处理可写套接字
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            print(sys.stderr, "", s.getpeername(), "queue empty")
            outputs.remove(s)
        else:
            print(sys.stderr, "sending '%s' to %s" % (next_msg, s.getpeername()))
            s.send(next_msg)

    # 处理异常情况
    for s in exceptional:
        for s in exceptional:
            print(sys.stderr, "exception condition on", s.getpeername())
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
            del message_queues[s]
