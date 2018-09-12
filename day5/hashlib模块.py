__author__ = 'fke'

"""
import hashlib

m = hashlib.md5()
m.update('书神'.encode(encoding="utf-8"))
m.update(b'fke')
print(m.digest())   # 2进制格式的hash
print(m.hexdigest())  # 16进制的hash

print("黄金分割线".center(40, "-"))
print("\n")



s = hashlib.sha256()
s.update('书神'.encode(encoding="utf-8"))
s.update(b'fke')
print(s.digest())   # 2进制格式的hash
print(s.hexdigest())  # 16进制的hash


print("黄金分割线".center(40, "-"))
print("\n")
import hmac
h = hmac.new('书神'.encode(encoding='utf-8'), b'fke')
print(h.digest())   # 2进制格式的hash
print(h.hexdigest())  # 16进制的hash

"""





import hashlib

'''
md5 = hashlib.md5()
md5.update('appVersion=1.6.0&'.encode('utf-8'))                        # appVersion
md5.update('channel=&'.encode('utf-8'))                             # channel
md5.update('device=&'.encode('utf-8'))                         # device
md5.update('deviceVersion=&'.encode('utf-8'))                     # deviceVersion
md5.update('packageId=156&'.encode('utf-8'))                           # packageId
md5.update('phone=13114725836&'.encode('utf-8'))                       # phone
md5.update('quantity=1&'.encode('utf-8'))                              # quantity
md5.update('system=&'.encode('utf-8'))                          # system
md5.update('timestamp=1529734229063&'.encode('utf-8'))                 # timestamp
md5.update('transactionPIN=123456&'.encode('utf-8'))                   # transactionPIN
md5.update('124uj13nejk31h4u3faenfiu3h923jalkd'.encode('utf-8'))
'''

md5 = hashlib.md5()
md5.update('appVersion=1.3.2&'.encode('utf-8'))                        # appVersion
md5.update('channel=shenyu&'.encode('utf-8'))                             # channel
md5.update('device=MI MAX 2&'.encode('utf-8'))                         # device
md5.update('deviceVersion=7.1.1&'.encode('utf-8'))                     # deviceVersion
md5.update('packageId=177&'.encode('utf-8'))                           # packageId
md5.update('phone=15338754623&'.encode('utf-8'))                       # phone
md5.update('quantity=1&'.encode('utf-8'))                              # quantity
md5.update('system=android&'.encode('utf-8'))                          # system
md5.update('timestamp=1529895220931&'.encode('utf-8'))                 # timestamp
md5.update('transactionPIN=123456&'.encode('utf-8'))                   # transactionPIN
md5.update('124uj13nejk31h4u3faenfiu3h923jalkd'.encode('utf-8'))



"""
# 登录
md5 = hashlib.md5()
md5.update('appVersion=1.3.2&channel=shenyu&code=604040&device=MI MAX 2&deviceVersion=7.1.1&phone=15338754623&system=android&timestamp=1529894009463&'.encode('utf-8'))
md5.update('124uj13nejk31h4u3faenfiu3h923jalkd'.encode('utf-8'))
"""

print(md5.hexdigest())

