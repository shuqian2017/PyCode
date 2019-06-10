# -*-coding:utf-8 -*-
"""
@project: code
@author: fke
@file: ssh.py
@time: 2019-06-03 23:44:42
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

'''
import paramiko

# 创建ssh对象
ssh = paramiko.SSHClient()

# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname='192.168.1.171', port=22, username='fke', password='123')
print("连接成功")

# 执行命令
while True:
    shell = input('>>>').strip('')
    if not shell:
        continue
    if shell == 'exit':
        break
    stdin, stdout, stderr = ssh.exec_command(command=shell)

    # 获取命令结果
    result = stdout.read()
    print('[ 返回结果 ]', result.decode('utf-8'))

# 关闭连接
ssh.close()

'''


# SSHClient 封装Transport 基于公钥密钥连接SSH
import paramiko

private_key = paramiko.RSAKey.from_private_key_file('./fke.pem')
transport = paramiko.Transport(('13.231.13.154', 22))
transport.connect(username='shuqian', pkey=private_key)

ssh = paramiko.SSHClient()
ssh._transport = transport
while True:
    shell = input('>>>').strip('')
    stdin, stdout, stderr = ssh.exec_command(command=shell)
    result = stdout.read()
    print('[ 返回结果 ]', result.decode('utf-8'))

transport.close()

