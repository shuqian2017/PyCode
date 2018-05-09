__author__ = 'fke'

import time
user, passwd = "fke", "123"

def auth(auth_type):
    print("auth_type:", auth_type)
    def outwrapper(func):
        def wrapper(*args, **kwargs):
            print("args fun kwargs:", *args, **kwargs)
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password").strip()
                if user == username and passwd == password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    res = func(*args, **kwargs)
                    print("\033[31;1m---after authenticaion---\033[0m")
                    return res
                else:
                    exit("\033[31;1mInvalid username or password\033[0m")
            elif auth_type == "ldap":
                print("搞个毛线的ldap,不懂啊。。。")

        return wrapper
    return outwrapper

def index():
    print("welcome to index page")

@auth(auth_type="local")           # home = wrapper()
def home():
    print("welcome to home page")
    return "from home"

@auth(auth_type="ldap")
def bbs():
    print("welcometo bbs page")


index()
print(home())
bbs()