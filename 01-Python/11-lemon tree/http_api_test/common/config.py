# @Author : 小坚强
# @StudentId : 2188
# @Time : 2019/8/28 18:08

import os
from configparser import ConfigParser

from common.constant import CONF_DIR


class MyConfig(ConfigParser):
    def __init__(self):
        super().__init__()

        # 初始化时，确定测试环境
        c = ConfigParser()
        c.read(os.path.join(CONF_DIR, "env.ini"), encoding="utf8")
        env = c.getint("env", "switch")
        if env == 1:
            file_name = "conf.ini"
        elif env == 2:
            file_name = "conf_2.ini"
        elif env == 3:
            file_name = "conf_3.ini"
        else:
            file_name = "conf.ini"
        self.file_path = os.path.join(CONF_DIR, file_name)

        # 打开对应环境的配置文件
        self.read(self.file_path, encoding="utf8")

    def write_data(self, section, option, value):
        self.set(section, option, value)

        with open(self.file_path, "w", encoding="utf8") as fp:
            self.write(fp)


config = MyConfig()
