"""
    写一个用来遍历某目录所有内容的函数（使用OS模块）

"""

# 1.遍历某目录下的所有文件和文件夹


# 2.判断是文件还是文件夹


# 3. 如果是文件就直接打印，如果是文件夹就把他再判断一次 一直到没有文件为止（递归）

import os

def fun(path):
    list_path = os.listdir(path)
    # print(list_path)

    for i in list_path:
        full_path = os.path.join(path, i)
        if os.path.isdir(full_path):
            # print("[-----%s-----]" % i)
            fun(full_path)
        else:
            print(full_path)


path = r'C:\Users\80934\Desktop\面试练习'
fun(path)