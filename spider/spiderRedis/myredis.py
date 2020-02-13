import redis

name = "reidc 模块"

class spiderRedis(object):
	def __init__(self):
		self.r = redis.Redis(host="127.0.0.1", port=6379)

	'''加入队列'''
	def push(self, key, dataList = []):
		for d in dataList:
			self.r.lpush(key, d)

	'''吐出队列'''
	def pop(self, key):
		return self.r.lpop(key)
	
	'''获取队列长度'''
	def getListLen(self, key):
		return self.r.llen(key)

	def keys(self):
		return self.r.keys("*");

	'''集合'''
	def sadd(self, key, val):
		self.r.sadd(key, val)
	def smembers(self, key):
		return self.r.smembers(key)

if __name__ == "__main__":
	pass
	