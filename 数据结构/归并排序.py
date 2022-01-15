from heapq import merge


def merge_sort(li,low,high):
    if low < high: #至少有两个元素，递归
        mid = (low + high)  // 2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)

li = list(range(1000))
import random
random.shuffle(li)
print(li)
merge_sort(li,0,len(li)-1)
print(li)