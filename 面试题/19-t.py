"""
    在redis数据库中，插入一条hash类型的数据
        1、数据信息包含了用户以下的信息：
            姓名， 年龄， 住址， 爱好的信息

        2、修改一下用户的爱好

        3、删除用户的年龄

        4、查询一下用户的信息

"""
from redis import StrictRedis

# redis_conn = redis.Redis(host='127.0.0.1', port=6379)
# redis_conn = redis.Redis(host='127.0.0.1', port=6379)

if __name__ == '__main__':
    try:
        sr = StrictRedis(host='127.0.0.1', port=6379, db=0)
        # print(sr.keys("*"))
        # print(sr.zrange("a5",0,-1))

        # 1、数据信息包含了用户一下的信息：
        # 姓名， 年龄， 住址， 爱好的信息
        sr.hmset('userinfo', {'name':'haha','age':'18','hobby':'swim'})
        print(sr.hmget('userinfo', 'hobby'))

        # 2、修改一下用户的爱好
        sr.hset('userinfo','hobby','basketbool')
        print(sr.hmget('userinfo', 'hobby'))

        #3、删除用户的年龄
        sr.hdel('userinfo','age')
        print(sr.hmget('userinfo', 'age'))
        print(sr.hkeys('userinfo'))
    except:
        pass

