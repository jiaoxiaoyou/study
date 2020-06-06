# @Author : 小坚强
# @StudentId : 2188
# @Time : 2019/9/7 0:46

import random
import re

from common.config import config
from common.do_mysql import DoMysql


# 临时缓存数据，通过反射机制动态设置属性
class CacheData(object):
    """临时缓存数据"""
    pass


# 随机创建手机号码：前两位写死了
def create_phone():
    phone = "13"
    for i in range(9):
        phone += str(random.randint(0, 9))
    return phone


# 随机生成数据库中没有的电话号码
def random_phone():
    mysql = DoMysql()
    while True:
        phone = create_phone()
        sql = f"select * from member where MobilePhone={phone}"
        if not mysql.find_count(sql):
            return phone


# 替换数据：参数化处理数据
def sub_conf(data):
    """替换动态参数为配置文件中的内容"""
    # 通过search方法进行匹配，能匹配到数据才进行数据处理
    while re.search(r"#(.+?)#", data):
        res = re.search(r"#(.+?)#", data)
        try:
            # 通过提取的字段，去配置文件中读取对应的数据内容
            value = config.get("data", res.group(1))
        except:
            value = getattr(CacheData, res.group(1))
        data = re.sub(res.group(), value, data)
    return data


# 这个是最新最全的规则，但业务接口中的手机号码匹配规则不是这个（比较笨的方法，但是逻辑好理解，规则比较全）
def create_phone_new():
    second = random.choice([3, 4, 5, 6, 7, 8, 9])
    third = {
        3: random.randint(0, 9),
        4: random.choice([5, 7, 8]),
        5: random.choice([0, 1, 2, 3, 5, 6, 7, 8, 9]),
        6: 6,
        7: random.choice([0, 1, 3, 5, 6, 7, 8]),
        8: random.randint(0, 9),
        9: random.choice([8, 9])
    }[second]
    other = random.randint(9999999, 100000000)

    return "1{}{}{}".format(second, third, other)
