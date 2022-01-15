"""
    python操作mysql如何解决sql注入问题
"""

import pymysql


def connect(username, password):
    client = pymysql.connect(
        host='47.111.20.134',
        port=3306,
        user='root',
        password='123456',
        database='db16',
        charset='utf8'
    )

    # 拿到游标 mysql>  //只显示元组 ==>(('666', '6666', 1),)
    # cursor = client.cursor()

    # 显示字典 ==>[{'username': '666', 'password': '6666', 'id': 1}]
    cursor = client.cursor(pymysql.cursors.DictCursor)

    # 简单查询语句
    # # sql = 'select * from user;'
    # # rows = cursor.execute(sql)

    # 防止sql注入
    sql = 'select * from user where username=%s and password=%s;'
    rows = cursor.execute(sql, (username, password))

    # 打印所有的结果集
    # print(cursor.fetchall())

    cursor.close()
    client.close()

    return rows


if __name__ == '__main__':
    username = input('请输入用户名：')
    password = input('请输入密码：')
    result = connect(username, password)

    if result == 0:
        print('用户名或密码错误')
    else:
        print('登录成功！')
