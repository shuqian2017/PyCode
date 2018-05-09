# -*-coding:utf-8 -*-

import os
from core import db_handler
from conf import settings
from core import logger
import json
import time

def login_required(func):
    "验证用户是否登录"
    def wrapper(*args, **kwargs):
        if args[0].get('is_authenticated'):
            return func(*args, **kwargs)
        else:
            exit("User is not authenticated.")
    return wrapper

def acc_auth(account, password):
    """
    accounts auth func
    :param account:  credit accounts number
    :param password:  credit accounts password
    :return: if passed the authentication, return the accounts object, otherwise, return None
    """
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path, account)
    print(account_file)
    if os.path.isfile(account_file):
        with open(account_file, 'r') as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strftime(account_data['expire_date'], "%Y-%m-%d"))
                if time.time() > exp_time_stamp:
                    print("\033[31;1mAccount [%s] has expired, please contact the back to get a new card!\033[0m" % account)
                else:
                    return account_data
            else:
                print("\033[31;1mAccount ID pr password is incorrect!\033[0m")
    else:
        print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)

def acc_auth2(account, password):
    '''
    优化版认证接口
    :param account: credit accounts number
    :param password: credit card password
    :return: if passed the authentication, return the accounts object, otherwise, return None
    '''
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where accounts=%s" % account)

    if data['password'] == password:
        exp_time_stamp = time.mktime(time.strptime(data['expire_date'], "%Y-%m-%d"))
        if time.time() > exp_time_stamp:
            print("\033[31;1mAccount [%s] has expired, please contact the back to get a new card!\033[0m" % account)
        else:
            return data
    else:
        print("\033[31;1mAccount ID or password is incorrect!\033[0m")

def acc_login(user_data, log_obj):
    """
    accounts login func
    :param user_data: user info data, only saves in memory
    :param log_obj:
    :return:
    """
    retry_count = 0
    while user_data["is_authenticated"] is not True and retry_count < 3:
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth = acc_auth2(account, password)
        if auth:
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            return auth
        retry_count += 1
    else:
        log_obj.error("accounts [%s] too many login attempts" % account)
        exit()

