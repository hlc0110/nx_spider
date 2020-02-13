from spiderRedis.myredis import spiderRedis as spider_redis
import requests
import time
from bs4 import BeautifulSoup
import common
import sys
from xpinyin import Pinyin
import re
import random


'''add equeue'''
def add_eq(eqKey, links = []):

    '''test'''
    # pyinyin = Pinyin()
    # eqKey = pyinyin.get_pinyin("策略", "_")

    # file = "/Users/jyair/Downloads/moni_after_sales/nx_spider/url.txt"
    # f = open(file, 'r')
    # urls = f.readlines()
    # f.close()
    # links = []
    # for link in urls:
    #     links.append(link.strip())
    '''test'''


    if len(links) == 0:
        return 0
    spider_redis.sadd(key=common.eq_sets_key, val=eqKey)	# 记录有哪些队列
    spider_redis.push(key=eqKey, dataList=links)					# 往队列里加入数据
    return 1

def getGameLink(word, p = 1):
    '''递归'''

    pyinyin = Pinyin()
    eqKey = pyinyin.get_pinyin(word, "_")
    url = "https://store.steampowered.com/search/?term=" + word + "&page=" + str(p)
    print(url)

    if p == 1:
        if (not hasattr(getGameLink, 'total')):  # hasattr函数的第一个变量为当前函数名，第二个为变量名，加单引号
            getGameLink.total = getTotal(url)  # 注意之后使用这个变量时一定要在变量名前加  函数名.


    r = requests.get(url, common.getHeaders())
    soup = BeautifulSoup(r.text, "lxml")

    if p == getGameLink.total:
        return True

    # print(p)
    # print(getGameLink.total)

    # 获取链接，保存
    links = getApplinks(soup)
    sleep_sec = random.randint(1,20)
    print("关键词：%s 共计 %d 页 | 当前采集第 %d页；采集链接数：%d | 休眠 %d 秒" % (word, getGameLink.total, p, len(links), sleep_sec))
    add_eq(eqKey, links)
    time.sleep(sleep_sec)
    p = p + 1
    getGameLink(word, p)

'''获取app总页数'''
def getTotal(url):
    total = 0
    r = requests.get(url, common.getHeaders())
    soup = BeautifulSoup(r.text, "lxml")
    pages = soup.find("div", class_='search_pagination_right')

    # 过滤非a链接
    for i in range(len(pages.contents)):
        if pages.contents[i].string.isdigit():
            total = int(pages.contents[i].string)
    return total

'''获取app 链接list'''
def getApplinks(soup):
    links = []
    for a in soup.find_all("a", class_="search_result_row"):
        links.append(a['href'])

    # 测试数据备份 start
    file = "/Users/jyair/Downloads/moni_after_sales/nx_spider/url.txt"
    f = open(file, 'a+')
    for link in links:
        f.write(link+"\n")
    f.close()
    # 测试数据备份 end

    return links

def test():
    # print(spider_redis)
    print("test")

if __name__ == "__main__":
    print("start spider...")
    startTime = common.getNow()

    spider_redis = spider_redis()
    # test()

    if len(sys.argv) == 1:
        print("请输入搜索参数!")
        exit()

    words = []
    words = words + sys.argv
    words.pop(0)

    for w in words:
        getGameLink(w)

    print("消耗时间:")
    
    print(common.getNow() - startTime)