import random
import time


def dazhuanpan(Dict,count):
    print(Dict)
    for i in range(3,0,-1):
        print(i,'秒后开奖~')
        time.sleep(1)
    index = random.randint(1,count)

    print('恭喜”',Dict[index],'“同学获奖，你是最棒的哦！')


if __name__ == '__main__':
    count = 1
    Dict = {}
    while True:
        name = input('请输入参与人（为空开始转盘）：')
        if name == None or name=='':
            break
        Dict[count]=name
        count += 1
    dazhuanpan(Dict,count)