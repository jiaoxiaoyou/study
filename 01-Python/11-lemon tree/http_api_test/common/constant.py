# @Author : 小坚强
# @StudentId : 2188
# @Time : 2019/9/2 12:48

import os
import time

"""
常量模块：存储项目路径
"""

# 项目路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 测试用例所在目录
CASES_DIR = os.path.join(BASE_DIR, 'testcases')

# 测试报告所在目录
REPORT_DIR = os.path.join(BASE_DIR, 'reports')

# 日志文件所在目录
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 配置文件所在目录
CONF_DIR = os.path.join(BASE_DIR, 'CONF')

# 用例数据所在目录
DATA_DIR = os.path.join(BASE_DIR, 'data')

# 日期格式
TIME = time.strftime("%Y%m%d%H%M")  # "%Y-%m-%d %H:%M:%S"
