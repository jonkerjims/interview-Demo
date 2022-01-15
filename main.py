from model_GCN import *
from GraphConstruction import *


def main(filename):
    ilearn(filename)
    # ilrean运行完毕后就已经把文件放到了固定位置
    # 判断文件是否合格
    if '合格':
        construct()
        convolution()
    else:
        


main('filename.txt')