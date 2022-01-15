# 线性查找
import time

from 算法入门.cal_time import cal_time


@cal_time
def linear_search(li, val):
    for index, v in enumerate(li):
        if v == val:
            return index
        else:
            return None


@cal_time
def binary_search(li, val):
    time.sleep(1)
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None


li = list(range(10000000))

binary_search(li, 3600545)
linear_search(li, 3600545)
