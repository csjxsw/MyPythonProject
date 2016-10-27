import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

r = redis.Redis(connection_pool=pool)
r.set('myname','Tom')
print r.get('myname')