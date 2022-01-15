from 算法入门.cal_time import cal_time


def count_sort (li, max_count = 100):
    count = [0 for _ in range(max_count+1)] # 初始化一个长度为100的空列表
    for val in li:
        count[val] += 1
    li.clear()
    for ind,val in enumerate(count):
        for i in range(val):
            li.append(ind)
    print(li)
@cal_time
def sys_sort(li):
    li.sort()
    print('sys_sort:',li)

# count = [0 for _ in range(100)]
# print(len(count))
li = [9,2,1,5,2,3,5,2,5,2,5,2,3,3,58,52,5,8,5,6,2,5,5,5,58,58,8,5,55,58]
count_sort(li)
sys_sort(li)