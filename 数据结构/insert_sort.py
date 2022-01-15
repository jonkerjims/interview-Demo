def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1 # j指手里牌的下标
        while j >= 0 and tmp < li[j]:
            li[j + 1] = li[j]
            j = j - 1
        li[j + 1] = tmp

li = [1,2,5,131,5,4,541,512,53,512,5]

insert_sort(li)

print(li)