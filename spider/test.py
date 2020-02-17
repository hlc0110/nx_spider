from DB.Db import Db as mysql
import random
import spider
from spiderRedis.myredis import spiderRedis as spider_redis_ys
from xpinyin import Pinyin
from bs4 import BeautifulSoup
import requests

# db = mysql("app")
# print(db.getPrikey())


'''
>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()
'''

# url = "https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/"

# print(url.split('/'))
# print(url.split('/')[4])
# 
# 
data = {
		"appId" : 'appId---', "app_name" : 'app_name---', 'intro' : 'intro---', 'link' : 'link---'
	}
keys = ','.join('`' + str(key) + '`' for key in data.keys())
values = ','.join('\'' + str(val) + '\'' for val in data.values())
print(keys)
print(values)