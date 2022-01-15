"""
    'r'模式操作text.txt文件， 如果文件存在，从中读取数据并打印： 如果这个文件不存在， 则捕获异常， 进行如下处理，
    新建该text.txt文件并写入想说的一些话，最后关闭文件

"""

try:
    with open('text.txt','r') as f:
        content = f.read()
        print(content)

except Exception as e:
    with open('text.txt', 'w', encoding='utf-8') as f:
        f.write('好好学习，天天向上')

finally:
    f.close()