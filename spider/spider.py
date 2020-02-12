from spiderRedis import myredis as spider_redis
import requests
import time
from bs4 import BeautifulSoup
import common
import sys
from xpinyin import Pinyin
import re


'''add equeue'''
def add_eq(eqKey, links = []):
    if len(links) == 0:
        return 0
    print(links)
    # spider_redis.sadd(common.eq_sets_key, eqKey)	# 记录有哪些队列
    # spider_redis.push(eqKey, links)					# 往队列里加入数据
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
    print("当前采集链接数：" + str(len(links)))
    exit()
    add_eq(eqKey, links)
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
    return links

def test():
    print(spider_redis)

if __name__ == "__main__":
    startTime = common.getNow()

    spider_redis = spider_redis.spiderRedis()
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