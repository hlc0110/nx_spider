from spiderRedis import myredis as spider_redis
import requests
import time
from bs4 import BeautifulSoup
import common
import sys
from DB.Db import Db as mysql


'''从队列里消费数据'''
def consumer(eqKey):
	link = spider_redis.pop(eqKey).decode('ascii')
	print(link)
	r = requests.get(link)
	sp = BeautifulSoup(r.text, 'lxml')

	# 获取标题
	app_name = sp.find("div", class_='apphub_AppName').text.replace('\'','\\\'').replace('"','\"').strip()
	# 获取描述
	intro = sp.find("div", class_='game_area_description').text.replace('\'','\\\'').replace('"','\"').strip()
	appId = link.split('/')[4]

	data = {
		"appId" : appId, "app_name" : app_name, 'intro' : intro, 'link' : link
	}
	db = mysql("app")
	db.insert(data)


if __name__ == "__main__":
	spider_redis = spider_redis.spiderRedis()
	if len(sys.argv) == 1:
		print("请输入 要消费的队列 !")
		print("总共有这么几个队列:")
		print(spider_redis.smembers(common.eq_sets_key))
		exit()

	eqKey = sys.argv[1]
	i = 0
	while True:
		if i == 0:
			print("======================== 消费队列：%s ========================" % eqKey)

		if i == 20:
			i = 0
		else:
			i += 1

		if spider_redis.getListLen(eqKey) == 0:
			print("	队列没有数据,休眠15秒...")
			time.sleep(15)
			continue

		consumer(eqKey)
		