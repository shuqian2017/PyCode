# -*-coding:utf-8 -*-
"""
@project: code
@author: fke
@file: sockert_server 基本.py
@time: 2019-06-01 09:20:19
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
import os

class MyTCPHandler(socketserver.BaseRequestHandler):

    # 重写handle 所有与客户端的交互都在handle中完成
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print('[ recv data ]:', self.data.decode())
                self.shell_res = os.popen(self.data.decode()).read()        # 执行客户端指令
                self.request.send(str(len(self.shell_res.encode())).encode())        # 告诉客户端执行指令后的结果长度
                # self.client_ack = self.request.recv(1024).decode()   # 粘包，分开2次发送； 使用socket_server基本有bug所以注释

                if len(self.shell_res) == 0:
                    self.shell_res = '未知的命令行选项'
                self.request.send(self.shell_res.encode())
            except ConnectionResetError as e:
                print("[ Error ] ", e)
                break

if __name__ == "__main__":
    HOST, PORT = 'localhost', 9999
    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) # 将TCPServer 更新为ThreadingTCPServer用于支持多线程
    server.serve_forever()