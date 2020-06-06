# @Author : 小坚强
# @StudentId : 2188
# @Time : 2019/8/28 15:40

import os
import logging
from common.config import config
from common.constant import LOG_DIR, TIME


# 此方法日志无法输出到html报告，只是创建了日志对象（但修改了html源码可以做到）
class MyLogging(object):
    log_name = config.get("log", "log_name")
    log_level = config.get("log", "log_level")
    sh_level = config.get("log", "sh_level")
    fh_level = config.get("log", "fh_level")
    # 拼接日志文件路径
    file_path = os.path.join(LOG_DIR, TIME + "-" + config.get("log", "file_name"))

    def __new__(cls, *args, **kwargs):
        """创建对象"""
        # 第一步：创建日志收集器对象，并设置等级
        log = logging.getLogger(cls.log_name)
        log.setLevel(cls.log_level)

        # 第二步：创建日志输出渠道，并设置等级
        # 1、输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(cls.sh_level)
        # 2、输出到日志文件
        fh = logging.FileHandler(filename=cls.file_path, encoding="utf8")
        fh.setLevel(cls.fh_level)

        # 第三步：添加日志输出渠道到日志收集器中
        log.addHandler(sh)
        log.addHandler(fh)

        # 第四步：指定日志输出格式
        # 创建日志输出格式对象
        fot = logging.Formatter("[%(asctime)s][%(filename)s-->line:%(lineno)d][%(levelname)s] %(message)s")
        # 将日志输出格式对象绑定到日志输出渠道中
        sh.setFormatter(fot)
        fh.setFormatter(fot)

        # # 第五步：移除日志
        # log.removeHandler(sh)
        # log.removeHandler(fh)

        return log


# 创建一个日志收集器对象
log = MyLogging()


# 此方法可以在html报告中输出日志内容，但logging的任务方法都需要后续重写
class Mylogger(object):
    def __init__(self):
        """初始化方法，获取配置文件内容"""
        self.log_name = config.get("log", "log_name")
        self.log_level = config.get("log", "log_level")
        self.sh_level = config.get("log", "sh_level")
        self.fh_level = config.get("log", "fh_level")
        # 拼接日志文件路径
        self.file_path = os.path.join(LOG_DIR, config.get("log", "file_name"))

    def my_log(self, lavel, msg):
        """创建输出日志的方法"""
        # 第一步：创建日志收集器对象，并设置等级
        log = logging.getLogger(self.log_name)
        log.setLevel(self.log_level)

        # 第二步：创建日志输出渠道，并设置等级
        # 1、输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(self.sh_level)
        # 2、输出到日志文件
        fh = logging.FileHandler(filename=self.file_path, encoding="utf8")
        fh.setLevel(self.fh_level)

        # 第三步：添加日志输出渠道到日志收集器中
        log.addHandler(sh)
        log.addHandler(fh)

        # 第四步：指定日志输出格式
        # 创建日志输出格式对象
        fot = logging.Formatter("[%(asctime)s][%(filename)s-->line:%(lineno)d][%(levelname)s] %(message)s")
        # 将日志输出格式对象绑定到日志输出渠道中
        sh.setFormatter(fot)
        fh.setFormatter(fot)

        # 输出日志
        if lavel == "DEBUG":
            log.debug(msg)
        elif lavel == "INFO":
            log.info(msg)
        elif lavel == "WARNING":
            log.warning(msg)
        elif lavel == "ERROR":
            log.error(msg)
        elif lavel == "CRITICAL":
            log.critical(msg)

        # 第五步：移除日志
        log.removeHandler(sh)
        log.removeHandler(fh)

    def debug(self, msg):
        self.my_log("DEBUG", msg)

    def info(self, msg):
        self.my_log("INFO", msg)

    def warning(self, msg):
        self.my_log("WARNING", msg)

    def error(self, msg):
        self.my_log("ERROR", msg)

    def critical(self, msg):
        self.my_log("CRITICAL", msg)

    def exception(self, msg):
        log.exception(msg)
