"""
    用生成器来计算 1！ + 2！ + 3！

"""

def func(n):
    i = 1
    j = 1
    while i <= n:
        yield j
        i += 1
        j = j * i
        # print("%d * %d" % (j,i))

a = func(5)

for res in a:
    print(res)