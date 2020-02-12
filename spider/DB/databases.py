import pymysql
#连接mysql数据库配置
def get_conn():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        port=3307,
        db='test',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor, #返回dict,不设置默认返回tuple
        autocommit=True,#自动提交
    )
    return conn

if __name__ == "__main__":
    pass