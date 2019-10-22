# -*-coding:utf-8 -*-
"""
@project: code
@author: fke
@file: settings.py
@time: 2019-06-05 23:44:17
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

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_platform = sys.platform

USER_HOME = "%s/home" % base_dir
LOG_DIR = "%s/log" % base_dir
LOG_LEVEL = "DEBUG"

ACCOUNT_FILE = "%s/conf/accounts.cfg" % base_dir

HOST = "0.0.0.0"
PORT = 9999