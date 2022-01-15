"""
    写一个登录的装饰器对以下函数进行装饰，要求输入账号和密码才能运行改函数

"""

def login(func):
    def wrappedfun(username, passward):
        if username == 'root' and passward == '123':
            print('通过认证')
            return func()
        else:
            print('未登录状态')
            return
    return wrappedfun

@login
def run():
    print('程序开始运行')

# 调用函数
run('root','1234')