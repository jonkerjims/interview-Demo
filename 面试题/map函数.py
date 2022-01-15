aList = [1, 2, 3, 4, 5]
bList = [5, 4, 3, 2, 1]


"""
    map函数是将alist、blist遍历传入lambda函数
"""
res = map(lambda x, y: x + y, aList, bList)

print(list(res))