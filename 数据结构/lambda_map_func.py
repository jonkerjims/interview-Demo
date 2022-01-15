'''
    lambda: 是一个匿名的函数
    map遍历函数时 使用
'''

lam = lambda x,y=1:x+y  # x,y相当于参数，y的默认值为1， 返回值时x+y， 把整个函数题赋给了lam
print(lam(1))   # 调用了函数lam 给了第一个参数赋值为1


'''
    map遍历函数时 使用
'''

def add(x):
    return x ** 2

mobj = map(add,[1,2,3,4])   # map将后面的列表一个个的遍历出来，放入add函数中执行

print(list(mobj))   # 将map对象转化为列表输出

'''
    map与lambda匿名函数联合使用
'''

mobj = map(lambda x:x**2,[1,2,3,4])
print(list(mobj))