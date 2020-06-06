# @Author : 小坚强
# @StudentId : 2188
# @Time : 2019/9/4 9:30

import pymysql

from common.config import config


class DoMysql(object):
    def __init__(self):
        # 连接数据库
        self.coon = pymysql.connect(
            host=config.get('mysql', 'host'),  # 数据库地址
            port=config.getint('mysql', 'port'),  # 端口
            user=config.get('mysql', 'user'),  # 账号
            password=config.get('mysql', 'password'),  # 密码
            database=config.get('mysql', 'database'),  # 数据库名
            charset="utf8"
        )
        # 创建一个游标
        self.cur = self.coon.cursor()

    def close(self):
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.coon.close()

    def find_one(self, sql):
        """查到的第一条数据"""
        self.coon.commit()  # 查询前刷新下状态
        self.cur.execute(sql)
        return self.cur.fetchone()

    def find_all(self, sql):
        """查到的全部数据"""
        self.coon.commit()  # 查询前刷新下状态
        self.cur.execute(sql)
        return self.cur.fetchall()

    def find_count(self, sql):
        """查到数据的条数"""
        self.coon.commit()  # 查询前刷新下状态
        return self.cur.execute(sql)

    def change_database(self, sql):
        """增、删、改数据库"""
        self.cur.execute(sql)
        self.coon.commit()  # 修改后提交事务才会有效
