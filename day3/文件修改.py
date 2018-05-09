__author__ = 'fke'
"""
f = open("test.txt", "r", encoding="utf-8")
f_new = open("test.txt.bak", "w", encoding="utf-8")

for line in f:
    if "走过患难" in line:
        line = line.replace("伴我走过患难", "伴fke走过患难")
    f_new.write(line)

f.close()
f_new.close()
"""


"""
# 为了避免打开的文件后忘记关闭,可以使用下面的方法,
# TODO 同时为了避免一行文件太长，可以使用“\”进行换行如下 （python3支持同时打开多个文件）
with open("test.txt", "r", encoding="utf-8") as f, \
        open("test.txt.bak", "r", encoding="utf-8") as f_one:
    for line in f:
        print(line.strip())

"""


# TODO 字符编码转换
import sys
print(sys.getdefaultencoding())   # 打印系统的默认编码

msg = "书神那个最帅的男人"
msg_gb2312 = msg.encode("gb2312")    # 因为系统当前默认的编码就是unicode,就不用再decode,喜大普奔
gb2312_to_unicode = msg_gb2312.decode("gb2312")    # 告诉别人需要解码的字符串当前是gb2312
gb2312_to_utf8 = gb2312_to_unicode.encode("utf-8")

print(msg)
print(msg_gb2312)
print(gb2312_to_unicode)
print(gb2312_to_utf8.decode("utf-8"))
