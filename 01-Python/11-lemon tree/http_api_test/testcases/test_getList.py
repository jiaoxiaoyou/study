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
from common.http_request import HttpSession
from common.common_func import CacheData, sub_conf, random_phone


@ddt
class GetListTestCase(unittest.TestCase):
    """所有获取列表，及生成回款计划接口的验证"""
    excel = DoExcel(os.path.join(DATA_DIR, "cases.xlsx"), "getlist")
    all_cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        cls.url = config.get("api", "url")
        cls.session = HttpSession()
        cls.mysql = DoMysql()

    @classmethod
    def tearDownClass(cls):
        cls.mysql.close()

    @data(*all_cases)
    def test_getList(self, case):
        log.info(f"验证接口：{case.interface}，接口url：{case.url}")
        # 第一步：准备测试数据，替换动态参数
        # 替换配置文件中的固定参数
        case.data = sub_conf(case.data)
        # 替换动态生成的参数
        if "*phone*" in case.data:
            # 注册时，手机号码为动态注册的号码
            phone = random_phone()
            case.data = case.data.replace("*phone*", phone)
        if "*memberId*" in case.data:
            # 想要用户id不存在，先找到最大用户id，加1即可
            member_id = self.mysql.find_one("select max(id) from member")[0]
            case.data = case.data.replace("*memberId*", str(member_id + 100))
        if "*loanId*" in case.data:
            # 想要项目id不存在，先找到最大项目id，加1即可
            loan_id = self.mysql.find_one("select max(id) from loan")[0]
            case.data = case.data.replace("*loanId*", str(loan_id + 100))

        if case.check_sql:
            # 生成回款计划前查找数据条数
            case.check_sql = sub_conf(case.check_sql)
            old_conut = self.mysql.find_count(case.check_sql)

        # 第二步：发送请求到接口，获取实际结果
        res_code = self.session.http_session(method=case.method,
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
            sql = f"select max(Id) from loan where MemberID = {eval(case.data)['memberId']}"
            setattr(CacheData, "loanId", str(self.mysql.find_one(sql)[0]))
        elif case.interface == "竞标":
            # 竞标成功后，将当前的investId写入配置文件中以便后面验证使用
            sql = f"select max(Id) from invest where MemberID = '{eval(case.data)['memberId']}' AND LoanId = '{getattr(CacheData, 'loanId')}'"
            setattr(CacheData, "investId", str(self.mysql.find_one(sql)[0]))

        # 第三步：比对预期结果和实际结果，断言用例是否通过
        try:
            log.info(f"请求期望返回码：{str(case.expected_code)}，请求实际返回码：{res_code}")
            self.assertEqual(str(case.expected_code), res_code)
            if case.check_sql:
                new_conut = self.mysql.find_count(case.check_sql)
                self.assertEqual(old_conut + 1, new_conut)
        except AssertionError as e:
            result = "未通过"
            log.exception(e)
            raise e
        else:
            result = "通过"
        finally:
            self.excel.write_data(row=case.code_id + 1, column=8, value=result)
            log.info(f"测试用例【{case.title}】执行【{result}】")
