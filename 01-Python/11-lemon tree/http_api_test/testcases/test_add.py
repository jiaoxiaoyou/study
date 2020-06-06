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
class AddTestCase(unittest.TestCase):
    """加标接口的验证"""
    excel = DoExcel(os.path.join(DATA_DIR, "cases.xlsx"), "add")
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
    def test_add(self, case):
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

        # 未登录时新增项目，没有返回码
        if case.expected_code:
            case.expected_code = str(case.expected_code)
        else:
            case.expected_code = None

        # 数据库校验，获取增加项目前当前用户的加标数量
        if case.check_sql:
            case.check_sql = sub_conf(case.check_sql)
            old_count = self.mysql.find_count(case.check_sql)

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

        # 第三步：比对期望结果和实际结果，进行断言
        try:
            log.info(f"请求期望返回码：{case.expected_code}，请求实际返回码：{res_code}")
            self.assertEqual(case.expected_code, res_code)
            if case.check_sql:
                new_count = self.mysql.find_count(case.check_sql)
                log.info(f"加标该用户期望标数：{old_count + 1}，加标该用户实际标数：{new_count}")
                self.assertEqual(old_count + 1, new_count)
        except AssertionError as e:
            result = "未通过"
            log.exception(e)
            raise e
        else:
            result = "通过"
        finally:
            self.excel.write_data(row=case.code_id + 1, column=8, value=result)
            log.info(f"测试用例【{case.title}】执行【{result}】")
