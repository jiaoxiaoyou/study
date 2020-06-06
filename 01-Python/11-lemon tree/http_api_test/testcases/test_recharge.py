# @Author : 小坚强
# @StudentId : 2188
# @Time : 2019/8/31 9:57

"""
测试用例模块：登录接口
"""

import os
import unittest
from common.mylogger import log
from common.config import config
from pack_lib.ddt import ddt, data
from common.do_excel import DoExcel
from common.do_mysql import DoMysql
from common.constant import DATA_DIR
from common.http_request import HttpSession
from common.common_func import random_phone, sub_conf, CacheData


@ddt
class RechargeTestCase(unittest.TestCase):
    """充值和取现接口的验证"""
    excel = DoExcel(os.path.join(DATA_DIR, "cases.xlsx"), "recharge&withdraw")
    all_cases = excel.read_data()
    url = config.get("api", "url")

    @classmethod
    def setUpClass(cls):
        cls.session = HttpSession()
        cls.mysql = DoMysql()

    @classmethod
    def tearDownClass(cls):
        cls.session.session_close()
        cls.mysql.close()

    @data(*all_cases)
    def test_recharge(self, case):
        log.info(f"验证接口：{case.interface}，接口url：{case.url}")
        # 第一步：准备测试数据，替换动态参数
        # 替换配置文件中的固定参数
        case.data = sub_conf(case.data)
        # 替换动态生成的参数
        if "*phone*" in case.data:
            # 注册时，手机号码为动态注册的号码
            phone = random_phone()
            case.data = case.data.replace("*phone*", phone)
        if "*amount*" in case.data:
            # 充值金额不足时，需要先获取库中的值
            sql = f"select LeaveAmount from member where MobilePhone = '{eval(case.data)['mobilephone']}'"
            money = float(self.mysql.find_one(sql)[0])
            case.data = case.data.replace("*amount*", str(money + 1000))

        # 未登录时取现/充值，没有返回码
        if case.expected_code:
            expected_code = str(case.expected_code)
        else:
            expected_code = None

        # 数据库校验
        if case.check_sql:
            case.check_sql = sub_conf(case.check_sql)
            old_money = float(self.mysql.find_one(case.check_sql)[0])

        # 第二步：发送请求到接口，获取实际结果
        res_code = self.session.http_session(method=case.method,
                                             url=self.url + case.url,
                                             data=eval(case.data)).json()["code"]

        # 处理上下接口关联问题
        if case.interface == "注册":
            # 注册后，将注册的账号和密码设置为缓存数据类的属性，以便其他用例读取
            setattr(CacheData, "phone", phone)
            setattr(CacheData, "pwd", "123qwe")

        # 第三步：比对预期结果和实际结果，断言用例是否通过
        try:
            log.info(f"请求期望返回码：{case.expected_code}，请求实际返回码：{res_code}")
            self.assertEqual(expected_code, res_code)
            if case.check_sql:
                new_money = float(self.mysql.find_one(case.check_sql)[0])
                log.info(f"充值/取现后金额为：{new_money}，充值/取现前金额为：{old_money}")
                if case.interface == "充值":
                    expected = old_money + eval(case.data)["amount"]
                elif case.interface == "取现":
                    expected = old_money - eval(case.data)["amount"]
                self.assertEqual(expected, new_money)
        except AssertionError as e:
            result = "未通过"
            log.exception(e)
            raise e
        else:
            result = "通过"
        finally:
            self.excel.write_data(row=case.code_id + 1, column=8, value=result)
            log.info(f"测试用例【{case.title}】执行【{result}】")
