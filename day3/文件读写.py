__author__ = 'fke'

f = open("test.txt", "r", encoding="utf-8")
"""
# 普通的写法（不推荐[特别是文件比较大的时候]）
for index, line in enumerate(f.readlines()):
    if index == 9:
        print(" 我是华丽的分割线 ".center(40, "☆"))
        break
    print(line.strip())
"""


'''
# 高逼格的写法(内存里面每次只保存一行)
count = 0
for line in f:
    if count == 9:
        print(" 我是华丽的分割线 ".center(40, "☆"))
        count += 1
        break
    print(line.strip())
    count += 1
'''


"""
print(f.tell())  # 获取文件光标的位置
print(f.readline())
f.seek(0)       # 将光标移回到指定的位置, 参数代表字符的位置
print(f.readline())

print(f.encoding)    # 显示打开文件的编码格式
"""

"""
print(f.flush())     # 强制刷新，一般写文件的时候，都是先存在内存里的缓存区，等到一定的时候再一起写入；
# f.flush举个栗子
import sys, time
for i in range(40):
    sys.stdout.write("#")    # std标准输入/输出 （屏幕）
    sys.stdout.flush()
    time.sleep(0.2)
"""

# f = open("test1.txt", "r+", encoding="utf-8")    # 文件句柄 读写
# f = open("test1.txt", "w+", encoding="utf-8")    # 文件句柄 写读
# f = open("test1.txt", "a+", encoding="utf-8")    # 文件句柄 追加读写
f = open("test1.txt", "wb")                      # 文件句柄 二进制文件
f.write("hello 书神\n".encode())
f.close()
