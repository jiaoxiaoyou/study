# @Author : 小坚强
# @StudentId : 2188
# @Time : 2019/8/31 9:50

import os
import unittest
from common.mylogger import log
from common.config import config
from pack_lib.HTMLTestRunnerNew import HTMLTestRunner
from common.constant import CASES_DIR, REPORT_DIR, TIME

"""项目启动文件"""

log.info("--------------正在开启测试运行程序--------------")

# 1、创建测试套件
suite = unittest.TestSuite()

# 2、将用例添加到测试套件中
loder = unittest.TestLoader()
suite.addTest(loder.discover(CASES_DIR, config.get("report", "case_name")))

# 3、执行测试用例，生成测试报告
with open(os.path.join(REPORT_DIR, TIME + "-" + config.get("report", "report_name")), "wb") as file:
    runner = HTMLTestRunner(
        stream=file,
        verbosity=2,
        title=config.get("report", "report_title"),
        description=config.get("report", "report_des"),
        tester=config.get("report", "report_tester")
    )
    runner.run(suite)

log.info("--------------测试运行程序执行完毕--------------")
