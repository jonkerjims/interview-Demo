# -*- coding: utf-8 -*-

import keyword

print(keyword.kwlist)

if True:
    print("True")
else:
    print("False")

'''
    python中数字有四种类型：整数、布尔型、浮点数和复数。
        int
        bool
        float
        complex
'''
'''
    Python3 中有六个标准的数据类型：
        Number（数字）
        String（字符串）
        List（列表）
        Tuple（元组）
        Set（集合）
        Dictionary（字典）
        
        不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
        可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
'''
'''
    isinstance 和 type 的区别在于：
        type()不会认为子类是一种父类类型。
        isinstance()会认为子类是一种父类类型。
        
        >>> class A:
        ...     pass
        ... 
        >>> class B(A):
        ...     pass
        ... 
        >>> isinstance(A(), A)
        True
        >>> type(A()) == A 
        True
        >>> isinstance(B(), A)
        True
        >>> type(B()) == A
        False
'''
'''
                """中括号包前不包后""" 
    str = 'Runoob'
                       
    print (str)          # 输出字符串
    print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
    print (str[0])       # 输出字符串第一个字符
    print (str[2:5])     # 输出从第三个开始到第五个的字符
    print (str[2:])      # 输出从第三个开始的后的所有字符
    print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
    print (str + "TEST") # 连接字符串
'''
x = 1 + 2j
print(x)

str = '123456789'

print(str)  # 输出字符串
print(str[0:-2:5])  # 输出第一个到倒数第二个的所有字符

"""
    List列表
"""
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表


def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


# ============================================================
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d.get('Thomas', -1))
print(d.pop('Bob1', None))
# ============================================================
s = set([1, 1, 2, 2, 3, 3])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)

s2 = set([2, 3, 4])
s1 = set([1, 2, 3])
print(s2 & s1)
print(s2 | s1)
# =====================可变对象 和 不可变对象========================================
'''
    list 和 dict是可变对象：是指在原来的基础上改变的
    tuple 和 str是不可变的
'''
# ==================================十六进制===============================================

print(hex(100))


# ========================================================================================
def calc(*numbers):
    print(type(numbers))
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


res = calc(1, 2)
print(res)
print(type(res))


# ===========================================================================================
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


# 位置参数 *
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f2(1, 2, d=99, ext=None)


# ============================================================================================
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# ===================================================================
s = "as  dasdasdasdas"
s = [i for i in s]
print(s)


# ===========================递归＋切片========================================
def trim(s):
    if 0 == len(s):
        return s
    while ' ' == s[0]:
        s = s[1:]
        if 0 == len(s):
            return s

    while ' ' == s[-1]:
        s = s[:-1]
        if 0 == len(s):
            return s
    return s


if trim('hello  ') != 'hello':
    print('测1试失败!')
    print(trim('hello  '))
elif trim('  hello') != 'hello':
    print('测11试失败!')
elif trim('  hello  ') != 'hello':
    print('测试111失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失1111败!')
elif trim('') != '':
    print('测试失11111败!')
elif trim('    ') != '':
    print('测111111试失败!')
else:
    print('测试成功!')

# ==============================================
d = {'a': 1, 'b': 2, 'c': 3}
for key, val in d.items():
    print(key, ':', val)

from collections.abc import Iterable

print(isinstance('abc', Iterable))


# ==============================================
def findMinAndMax(L):
    max = L[0]
    min = L[0]
    for i in L:
        max = i if i > max else max
        min = i if i < min else min

    return (max, min)


print(findMinAndMax([1, 2, 5, 2, 5, 2, 65]))
# ===================列表生成式===========================
s = [i ** 2 for i in range(1, 11)]
s = [i ** 2 for i in range(1, 11) if i % 2 == 0]
str = [m + n for m in 'XV' for n in 'ca']
print(s)
print(str)

import os

dirList = [d for d in os.listdir('../')]
print(dirList)
# ========================================================
import requests
import json
import geoip2.database

def IPsearch(ip):

    # client = geoip2.webservice.Client(651126, 'Pc3DOQ2YnPga')
    #
    # response = client.insights(ip)
    reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
    response = reader.city(ip)  # 有多种语言，我们这里主要输出英文和中文print("你查询的IP的地理位置是:")
    address = response.country.names["zh-CN"]+';'+response.subdivisions.most_specific.names["zh-CN"]+';'+response.city.names["zh-CN"]
    position = (response.location.longitude,response.location.latitude)

    return address,position

