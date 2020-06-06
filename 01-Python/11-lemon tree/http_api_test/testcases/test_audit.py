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
class AuditTestCase(unittest.TestCase):
    """审核接口的验证"""
    excel = DoExcel(os.path.join(DATA_DIR, "cases.xlsx"), "audit")
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
    def test_audit(self, case):
        log.info(f"验证接口：{case.interface}，接口url：{case.url}")
        # 第一步：准备用例数据
        # 替换配置文件中的固定参数
        case.data = sub_conf(case.data)
        # 替换动态生成的参数
        if "*phone*" in case.data:
            # 注册时，手机号码为动态注册的号码
            phone = random_phone()
            case.data = case.data.replace("*phone*", phone)
        if "*loanId*" in case.data:
            # 想要项目id不存在，先找到最大项目id，加1即可
            loan_id = self.mysql.find_one("select max(id) as loanId from loan")[0]
            case.data = case.data.replace("*loanId*", str(loan_id + 1))

        # 未登录时审核，没有返回码
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
                new_status = self.mysql.find_one(case.check_sql)[0]
                log.info(f"审核后该标期望状态：{eval(case.data)['status']}，审核后该标实际状态：{new_status}")
                self.assertEqual(eval(case.data)["status"], new_status)
        except AssertionError as e:
            result = "未通过"
            log.exception(e)
            raise e
        else:
            result = "通过"
        finally:
            self.excel.write_data(row=case.code_id + 1, column=8, value=result)
            log.info(f"测试用例【{case.title}】执行【{result}】")