'''
    写一个复制文件代码（用文件的读写）

'''

with open('aim.txt','rb') as f:
    a = f.read()

with open('copy.txt','wb') as f:
    f.write(a)