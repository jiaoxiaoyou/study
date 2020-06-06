# @Author : 小坚强
# @StudentId : 2188
# @Time : 2019/8/30 18:00

import requests
from requests import session


class HttpRequest(object):
    """直接发送请求，不记录cookies信息"""

    def http_request(self, method, url, data=None, headers=None):
        try:
            method = method.lower()  # 转换为小写
            if method == "post":
                return requests.post(url=url, data=data, headers=headers)
            elif method == "get":
                return requests.get(url=url, params=data, headers=headers)
            elif method == "put":  # 支持其他请求方式，以此举例
                return requests.put(url=url, params=data, headers=headers)
            else:
                print(f"不支持的请求方式：{method}")
        except Exception as e:
            print(f"发生异常：{e}")


class HttpSession(object):
    """使用Session对象发送请求，自动记录cookies信息"""

    def __init__(self):
        self.s = session()  # Session对象

    def http_session(self, method, url, data=None, headers=None, json=None):
        # 有一些post请求，若要指定json字符串传参，则需要用到json参数
        try:
            method = method.lower()  # 转换为小写
            if method == "post":
                return self.s.post(url=url, data=data, headers=headers, json=json)
            elif method == "get":
                return self.s.get(url=url, params=data, headers=headers)
            else:
                print(f"不支持的请求方式：{method}")
        except Exception as e:
            print(f"发生异常：{e}")

    def session_close(self):
        """关闭Session对象，否则使用Session对象后，不关闭一直占内存"""
        # self.s.cookies.clear()  # 如果s是类属性，必须清除cookies才可以关闭session关联
        self.s.close()

