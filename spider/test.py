from DB.Db import Db as mysql
import random
import spider
from spiderRedis.myredis import spiderRedis as spider_redis_ys
from xpinyin import Pinyin

# db = mysql("app")
# print(db.getPrikey())


'''
>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()
'''
'''
file = "/Users/jyair/Downloads/moni_after_sales/nx_spider/url.txt"
f = open(file, 'a+')
links = [
	"http://www.jiayuan.com12345",
	"http://www.jiayuan.com123456",
	"http://www.jiayuan.com123457",
	"http://www.jiayuan.com123458",
	"http://www.jiayuan.com123459",
	"http://www.jiayuan.com123450",
]

for link in links:
	f.write(link+"\n")

f.close()
'''

# print(random.randint(1,10))


pyinyin = Pinyin()
eqKey = pyinyin.get_pinyin("策略", "_")

file = "/Users/jyair/Downloads/moni_after_sales/nx_spider/url.txt"
f = open(file, 'r')
links = f.readlines()
f.close()
urls = []
for link in links:
	urls.append(link.strip())

spider_redis = spider_redis_ys()
spider.add_eq(eqKey=eqKey, links=urls)