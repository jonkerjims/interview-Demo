# def qsort(List):
#     if len(List) <= 1: return List
#
#     return qsort([L for L in List[1:] if L < List[0]]) + List[0:1] + qsort([R for R in List[1:] if R >= List[0]])
#
#
# res = qsort([5, 3, 2, 1])
#
# print(res)
#
# List = [3, 5, 2, 1]
# print([L for L in List[1:] if L < List[0]])

'''

    时间复杂度： nlogn
'''

# 快速排序框架
def quick_sort(data, left, right):
    """

    """
    if left < right:  # 递归终止条件
        mid = partition(data, left, right)
        quick_sort(data, left, mid-1)
        quick_sort(data, mid+1, right)
             

def partition(li, left, right):
    tmp = li[left]
    
    while left < right:
        while left < right and li[right] >= tmp: # 从右面找比tmp小的数
            right -= 1 # 往左走一步
        li[left] = li[right] # 把右边填写到左边去
        print(li,'left')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left] # 把左边的值填写到右边
        print(li, 'right')
    li[left] = tmp # 此时li[left]与li[right]已碰头，所以写谁都可以，相当于又把tmp赋值给中间值
    return left

li = [5,7,4,6,3,1,2,9,8]
print(li)
quick_sort(li,0,len(li)-1)

print(li)
