# -*-coding:utf-8 -*-
"""
@project: code
@author: fke
@file: ftp_main.py
@time: 2019-06-05 22:48:10
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
import configparser
import os

from conf import settings
import subprocess
import hashlib
import re



STATUS_CODE = {
    200: "Task finished",
    250: "Invalid cmd format, e.g: {'action':'get', 'filename':'test.py', 'size':344}",
    251: "Invalid cmd",
    252: "Invalid auth data",
    253: "Wrong username or password",
    254: "Passed authentication",
    255: "Filename doesn't provided",
    256: "Filename doesn't exist on server",
    257: "ready to send file",
    258: "md5 verification",
    259: "path doesn't exist on server",
    260: "path changed",
}

platform = settings.base_platform  # win32

import json

class FTPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print('adderr:', self.client_address[0] +'\n'  'recv data:', self.data )
            if not self.data:
                print("client closed...")
                break
            data = json.loads(self.data.decode())
            print("data:", data)
            if data.get('action') is not None:
                if hasattr(self, "_%s" % data.get('action')):
                    func = getattr(self, "_%s" % data.get('action'))
                    func(data)
                else:
                    print("invalid cmd")
                    self.send_response(251)
            else:
                print("invalid cmd format")
                self.send_response(250)

    def send_response(self, status_code, data=None):
        '''向客户端返回数据'''
        response = {
            'status_code': status_code,
            'status_msg': STATUS_CODE[status_code],
        }
        if data:
            response.update({'data': data})
        self.request.send(json.dumps(response).encode())

    def _auth(self, *args, **kwargs):
        data = args[0]
        if data.get('username') is None or data.get("password") is None:
            self.send_response(252)

        user = self.authenticate(data.get("username"), data.get("password"))
        if user is None:
            self.send_response(253)
        else:
            print("passed authentication", user)
            self.user = user
            self.user['username'] = data.get("username")


            self.home_dir = "%s/home/%s" % (settings.base_dir, data.get("username"))
            self.current_dir = self.home_dir
            self.send_response(254)

    def authenticate(self, username, password):
        '''验证用户合法性, 合法就返回用户数据'''

        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():
            _password = config[username]["Password"]
            if _password == password:
                print("pass auth..", username)
                config[username]["Username"] = username
                return config[username]

    def _put(self, *args, **kwargs):
        "client send file to server"
        pass

    def _listdir(self, *args, **kwargs):
        """return file list on current dir"""
        if platform == "linux2":
            res = self.run_cmd("ls -lsh %s" % self.current_dir)
            self.send_response(200, data=res)
        else:
            self.send_response(251)


    def run_cmd(self, cmd):
        cmd_res = subprocess.getstatusoutput(cmd)
        return cmd_res

    def _change_dir(self, *args, **kwargs):
        """change dir"""
        if args[0]:
            dest_path = "%s/%s" % (self.current_dir, args[0]['path'])
        else:
            dest_path = self.home_dir

        real_path = os.path.realpath(dest_path)
        print("real path", real_path)
        if real_path.startswith(self.home_dir):
            if os.path.isdir(real_path):
                self.current_dir = real_path
                current_relative_dir = self.get_relative_path(self.current_dir)
                self.send_response(260, {'current_path': current_relative_dir})
            else:
                self.send_response(259)
        else:
            print("has no permission.... to access", real_path)
            current_relative_dir = self.get_relative_path(self.current_dir)
            self.send_response(260, {'current_path': current_relative_dir})


    def get_relative_path(self, abs_path):
        """return relative path of this user"""
        relative_path = re.sub("^%s" % settings.base_dir.replace('\\', '/'), '', abs_path.replace('\\', '/'))
        print('relative path', relative_path, abs_path)
        return relative_path


    def _pwd(self, *args, **kwargs):
        current_relative_dir = self.get_relative_path(self.current_dir)
        self.send_response(200, data=current_relative_dir)

    def _get(self, *args, **kwargs):
        data = args[0]
        if data.get('filename') is None:
            self.send_response(255)
        file_abs_path = "%s/%s" % (self.current_dir, data.get('filename'))
        print('file abs path', file_abs_path)

        if os.path.isfile(file_abs_path):
            file_obj = open(file_abs_path, "rb")
            file_size = os.path.getsize(file_abs_path)
            self.send_response(257, data={'file_size': file_size})
            self.request.recv(1)    # 等待客户端确认

            if data.get('md5'):
                md5_obj = hashlib.md5()
                for line in file_obj:
                    self.request.send(line)
                    md5_obj.update(line)
                else:
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()
                    self.send_response(258, {'md5': md5_val})
                    print("send file done...")
            else:
                for line in file_obj:
                    self.request.send(line)
                else:
                    file_obj.close()
                    print("send file done...")
        else:
            self.send_response(256)


# if __name__ == "__main__":
#     HOST, PORT = "localhost", 9500


