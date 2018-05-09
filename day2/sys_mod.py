__author__ = 'fke'


import sys, os

print(sys.argv)

# cmd_res = os.system("dir")  #执行命令，不保存结果
cmd_res = os.popen("dir").read()
print("-->", cmd_res)
try:
    os.mkdir("mew_dir")
except:
    print("目录已经存在")
