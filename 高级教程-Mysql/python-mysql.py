import random
import time
from concurrent import futures

import pymysql

"""
    1、连接数据库
    2、获取操作游标
    3、执行SQL语句
    4、获取游标中的数据
    5、关闭数据库连接
"""


# db = pymysql.connect(user="root",password="Ahau@bioinfor",host="39.103.157.111",database="newyear",port=3360,charset="utf8")
#
# cursor = db.cursor()
#
# cursor.execute('SELECT VERSION()')
#
# data = cursor.fetchall()
#
# print(data)
#
# db.close()

class find_in_mysql:
    def __init__(self, user="root", password="Ahau@bioinfor", host="39.103.157.111", database="newyear", port=3360,
                 charset="utf8"):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.port = port
        self.chartset = charset
        self.count = 0

    def execute_sql(self, sql: str):
        self.count = self.count + 1
        data = "query OK {}".format(self.count)
        db = pymysql.connect(user=self.user, password=self.password, host=self.host, database=self.database,
                             port=self.port, charset=self.chartset)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            # data = cursor.fetchall()

        except BaseException as err:
            print('失败')
            db.rollback()

        db.close()
        print(data)
        return data


newyear = find_in_mysql()
sql1 = """
    SELECT * from NewYear_newyearrecords ORDER BY creation_time DESC;
"""
sql2 = """
    CREATE TABLE IF NOT EXISTS EMPLOYEE (
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT
    )
"""
sql3 = """
    INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Mac', 'Mohan', 20, 'M', {})
"""
sql4 = """
    DELETE FROM EMPLOYEE WHERE INCOME > 1
"""
# 导入线程池
# executor = futures.ThreadPoolExecutor(max_workers=1000)

# List = [random.randint(0,10000) for i in range(0,10000)]
# for i in List:
#
#     queryset = executor.submit(newyear.execute_sql,sql3.format(i))
#     # print(queryset.result())
queryset = newyear.execute_sql(sql4)

