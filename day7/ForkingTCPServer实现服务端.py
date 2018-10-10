# -*-coding:utf-8 -*-
"""
@project: code
@author: Administrator
@file: ForkingTCPServer实现服务端.py
@time: 2018-10-10 18:03:36
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

import socketserver

class MyServer(socketserver.BaseRequestHandler):
    # ThreadingTCPServer实现的Socket服务器内部会为每个client创建一个"线程", 该线程用来和客户端进行交互
    def handle(self):
        conn = self.request
        conn.sendall("\033[31;1m欢迎致电10086, 请输入1xxx, 0转人工服务\033[0m.".encode())
        Flag = True
        while Flag:
            data = conn.recv(1024).decode()
            if data == 'exit':
                Flag = False
            elif data == '0':
                conn.sendall("\033[32;1m通话可能会被录音.balabala...\033[0m".encode())
            else:
                conn.sendall("\033[32;1m请重新输入\033[0m.".encode())

if __name__ == '__main__':
    # 如果此处使用ForkingTCPServer类来创建多进程的实例化链接，在windows下会报错；原因是os.fork在windows上是不可用的
    server = socketserver.ForkingTCPServer(('127.0.0.1', 8888), MyServer)
    server.serve_forever()