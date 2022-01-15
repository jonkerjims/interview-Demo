'''
    题目：使用dict中的value进行比较，获得value值最大的key值

    dict = {
        'aaa':8000000000,
        'bbb':90000,
        'ccc':55
    }

'''
dict = {
        'aaa': 8000000000,
        'bbb': 90000,
        'ccc': 55
    }

# max函数默认比较Key值
# 使用lambda函数指定key为value值
max_key = max(dict, key=lambda key: dict[key])
print(max_key)