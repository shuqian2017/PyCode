__author__ = 'fke'

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
