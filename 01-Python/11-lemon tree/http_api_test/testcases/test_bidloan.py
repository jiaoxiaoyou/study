# @Author : 小坚强
# @StudentId : 2188
# @Time : 2019/9/9 18:03

import os
import unittest
from common.mylogger import log
from common.config import config
from common.do_mysql import DoMysql
from pack_lib.ddt import data, ddt
from common.do_excel import DoExcel
from common.constant import DATA_DIR
from common.http_request import HttpSession
from common.common_func import random_phone, sub_conf, CacheData

@ddt
class BidloanTestCase(unittest.TestCase):
    """投资竞标接口的验证"""
    excel = DoExcel(os.path.join(DATA_DIR, "cases.xlsx"), "bidloan")
    all_cases = excel.read_data()
    url = config.get("api", "url")

    @classmethod
    def setUpClass(cls):
        cls.http = HttpSession()
        cls.mysql = DoMysql()

    @classmethod
    def tearDownClass(cls):
        cls.http.session_close()
        cls.mysql.close()

    @data(*all_cases)
    def test_bidloan(self, case):
        log.info(f"验证接口：{case.interface}，接口url：{case.url}")
        # 第一步：准备用例数据
        # 替换配置文件中的固定参数
        case.data = sub_conf(case.data)
        # 替换动态生成的参数
        if "*phone*" in case.data:
            # 注册时，手机号码为动态注册的号码
            phone = random_phone()
            case.data = case.data.replace("*phone*", phone)
        if "*memberId*" in case.data:
            # 想要用户id不存在，先找到最大用户id，加1即可
            member_id = self.mysql.find_one("select max(id) as memberId from member")[0]
            case.data = case.data.replace("*memberId*", str(member_id + 1))
        if "*loanId*" in case.data:
            # 想要项目id不存在，先找到最大项目id，加1即可
            loan_id = self.mysql.find_one("select max(id) as loanId from loan")[0]
            case.data = case.data.replace("*loanId*", str(loan_id + 1))
        if "*amount*" in case.data:
            # 想要可投金额不足，先找到可投金额的最大值，加大值即可
            sql = f"select Amount from loan where Id = {eval(case.data)['loanId']}"
            case.data = case.data.replace("*amount*", str(self.mysql.find_one(sql)[0] + 1000))

        # 未登录时投资竞标，没有返回码
        if case.expected_code:
            case.expected_code = str(case.expected_code)
        else:
            case.expected_code = None

        # 第二步：访问接口，获取实际结果
        res_code = self.http.http_session(method=case.method,
                                     url=self.url + case.url,
                                     data=eval(case.data)).json()["code"]

        # 处理上下接口关联问题
        if case.interface == "注册":
            # 注册后，将注册的账号和密码设置为缓存数据类的属性，以便其他用例读取
            setattr(CacheData, "phone", phone)
            setattr(CacheData, "pwd", "123qwe")
        elif case.interface == "登录":
            # 登录后后，将用户id设置为缓存数据类的属性，以便其他用例读取
            sql = f"select id from member where MobilePhone='{getattr(CacheData, 'phone')}'"
            setattr(CacheData, "memberId", str(self.mysql.find_one(sql)[0]))
        elif case.interface == "加标":
            # 加标成功后，将当前的loanId写入配置文件中以便后面验证使用
            sql = f"select max(id) as loanId from loan where memberId = {eval(case.data)['memberId']}"
            setattr(CacheData, "loanId", str(self.mysql.find_one(sql)[0]))

        # 第三步：比对期望结果和实际结果，进行断言I
        try:
            log.info(f"请求期望返回码：{case.expected_code}，请求实际返回码：{res_code}")
            self.assertEqual(case.expected_code, res_code)
            if case.check_sql:
                case.check_sql = sub_conf(case.check_sql)
                count = self.mysql.find_count(case.check_sql)
                log.info(f"竞标后数据库期望数据条数：1，竞标后数据库实际数据条数：{count}")
                self.assertEqual(1, count)
        except AssertionError as e:
            result = "未通过"
            log.exception(e)
            raise e
        else:
            result = "通过"
        finally:
            self.excel.write_data(row=case.code_id + 1, column=8, value=result)
            log.info(f"测试用例【{case.title}】执行【{result}】")