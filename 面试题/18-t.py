"""
    redis:相关问题

"""
import redis

redis_conn = redis.Redis(host='127.0.0.1', port=6379)

# 清理所有现在的数据， 方便测试

# print(redis_conn.keys())
# print(redis_conn.get("myKey"))

#删除redis中所有的数据
for key in redis_conn.keys():
    redis_conn.delete(key)

"""
    1、给文章新增几篇文章    
"""
# 使用hash，类似map的形式，存储(Id、标题) 数据
for idx in range(101,106):
    redis_conn.hset('articles', str(idx), f'this is {idx} article title')

"""
    2、给用户展示文章列表
"""
# 展示所有的文章列表
for article_id, article_title in redis_conn.hgetall('articles').items():
    print('#'*30)
    # 默认返回bytes类型
    print(article_id, article_title)
    # 转化成str类型
    print(article_id.decode('utf-8'), article_title.decode('utf-8'))

# 展示单个文章的标题
print(redis_conn.hget('articles','104').decode('utf-8'))

"""
    3、用户访问文章则产生行为记录
        产生了行为： uid访问了article_id
"""
def user_visit(uid, article_id):
    # 1. String结构， 文章的访问次数加1
    redis_conn.incr(f"article_counter_{article_id}")
    # 2. List结构， 记录uid的访问列表
    redis_conn.lpush(f"user_visit_{uid}", str(article_id))
    # 3. Set结构， 记录uid的全站集合
    redis_conn.sadd(f"all_visit_uids", str(uid))
    # 4. SortedSet结构， 文章的热度加1
    redis_conn.zincrby("article__hots", 1, str(article_id))

# 模拟3个用户的访问记录
user_visit('uid_01', '101')
user_visit('uid_01', '102')
user_visit('uid_01', '104')

user_visit('uid_02', '102')
user_visit('uid_02', '103')
user_visit('uid_02', '104')

user_visit('uid_03', '103')
user_visit('uid_03', '104')
user_visit('uid_03', '105')

"""
    4、查询文章访问次数
"""
print(redis_conn.get(f'article_counter_101'))
print(redis_conn.get(f'article_counter_102'))
print(redis_conn.get(f'article_counter_103'))
print(redis_conn.get(f'article_counter_104'))
print(redis_conn.get(f'article_counter_105'))

"""
    5、展示一个用户的访问历史
"""
print(redis_conn.lrange('user_visit_uid_01', 0, -1))
print(redis_conn.lrange('user_visit_uid_02', 0, -1))
print(redis_conn.lrange('user_visit_uid_03', 0, -1))

"""
    6、展示访问全站的用户集合
"""
print(redis_conn.smembers('all_visit_uids'))

"""
    7、展示文章热榜以及热度
"""
print(redis_conn.zrange("article__hots", 0, -1, withscores=True, desc=True))
