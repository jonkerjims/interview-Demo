

def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new

def select_sort(li): # 优化后的
    for i in range(len(li)-1): #一共要遍历这么多次
        min_loc = i  # 设置无序区的最小值为min_loc
        for j in range(i,len(li)-1):
            if li[j+1] < li[min_loc]:
                li[min_loc],li[j+1] = li[j+1],li[min_loc]
    return li

li = [3,2,4,8,5,2,4,8,9,5,2]
print(select_sort(li))