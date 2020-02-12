from datetime import datetime
import time

def getHeaders():
	header = {
		"Host": "steamcommunity.com",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}
	return header

def getNow():
	return datetime.now() #获得当前时间


eq_sets_key = "game_types"

if __name__ == "__main__":
	pass