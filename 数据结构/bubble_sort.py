import random


def bubble_sort1(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
        print(li)

# 优化
def bubble_sort2(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return
        print(li)
li = [random.randint(0, 10000) for i in range(10)]
print(li)

bubble_sort1(li)
print(li)

# 时间复杂度 o（n²）
