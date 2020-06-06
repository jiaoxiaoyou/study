# @Author : 小坚强
# @StudentId : 2188
# @Time : 2019/8/31 9:57

import os
import unittest
from common.mylogger import log
from common.config import config
from pack_lib.ddt import ddt, data
from common.do_excel import DoExcel
from common.do_mysql import DoMysql
from common.constant import DATA_DIR
from common.http_request import HttpRequest
from common.common_func import random_phone, sub_conf


@ddt
class RegisterTestCase(unittest.TestCase):
    """登录和注册接口的验证"""
    excel = DoExcel(os.path.join(DATA_DIR, "cases.xlsx"), "login&register")
    all_cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        cls.url = config.get("api", "url")
        cls.request = HttpRequest()
        cls.mysql = DoMysql()

    @classmethod
    def tearDownClass(cls):
        cls.mysql.close()

    @data(*all_cases)
    def test_register(self, case):
        log.info(f"验证接口：{case.interface}，接口url：{case.url}")
        # 第一步：准备测试数据，替换动态参数
        # 替换配置文件中的固定参数
        case.data = sub_conf(case.data)
        # 替换动态生成的参数
        if "*phone*" in case.data:
            # 注册时，手机号码为动态注册的号码
            phone = random_phone()
            case.data = case.data.replace("*phone*", phone)

        # 第二步：发送请求到接口，获取实际结果
        res_code = self.request.http_request(method=case.method,
                                        url=self.url + case.url,
                                        data=eval(case.data)).json()

        # 第三步：比对预期结果和实际结果，断言用例是否通过
        try:
            if case.check_sql:
                case.check_sql = case.check_sql.replace("*phone*", phone)
                count = self.mysql.find_count(case.check_sql)
                log.info(f"注册后数据库期望数据条数：1，注册后数据库实际数据条数：{count}")
                self.assertEqual(1, count)
            log.info(f"请求期望返回码：{eval(case.expected)}，请求实际返回码：{res_code}")
            self.assertEqual(eval(case.expected), res_code)
        except AssertionError as e:
            result = "未通过"
            log.exception(e)
            raise e
        else:
            result = "通过"
        finally:
            self.excel.write_data(row=case.code_id + 1, column=8, value=result)
            log.info(f"测试用例【{case.title}】执行【{result}】")
