"""
    生产验证码函数 整型数字和字母随机组成 可以指定长度
"""
import random
def make_code(n):
    res = ""
    for i in range(n):
        mun = str(random.randint(0,9)) # 随机数字
        c = chr(random.randint(65,90)) # 随机生成大写字母
        d = chr(random.randint(65,90)).lower() #随机生成小写字母
        # 把所有的字符拼接到一起
        s = random.choice([mun, c, d])
        res += s
    return res


print(make_code(10))