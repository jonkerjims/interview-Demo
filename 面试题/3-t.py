'''
    定义一个函数，计算1到990的和
'''

def func(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

res = func(990)
print(res)