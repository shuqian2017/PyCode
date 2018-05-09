# -*-coding:utf-8 -*-
import json
import time
from core import db_handler
from conf import settings

def load_current_balance(account_id):
    '''
    return accounts balance and other basic info
    :param account_id:
    :return:
    '''
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where accounts=%s" % account_id)
    return data

def dump_account(account_data):
    '''
    after updated transaction or accounts data, dump it back to file db
    :param account_data:
    :return:
    '''
    db_api = db_handler.db_handler()
    data = db_api("update accounts where accounts=%s" % account_data['id'], account_data=account_data)
    return True
