#!/usr/bin/env python
# encoding: utf-8
"""
@author :gaoyuan
@contact:1103313679@qq.com
@time   :2020/5/12 14:15
@desc : 生成日志
"""


import ConfigRead
import logging
import time
import sys
# 设置深度为100W
sys.setrecursionlimit(1000000)

class Logger(object):
    def __init__(self, loggers):
        self.loggers = logging.getLogger(loggers)
        self.loggers.setLevel(logging.DEBUG)
        # 清除handlers，防止日志出现重复打印的情况
        self.loggers.handlers.clear()
        # 设置日志名称
        now = time.strftime('%Y-%m-%d-%H_%M_%S')
        self.log_name = ConfigRead.LOGS_PATH + loggers + '-' + now + '.log'
        filehandles = logging.FileHandler(self.log_name, encoding='UTF-8')
        filehandles.setLevel(logging.INFO)

        # 创建一个输入到控制台的日志文件头
        consolehandles = logging.StreamHandler()
        consolehandles.setLevel(logging.INFO)

        # 将handles进行格式转化
        self.formaterr = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        filehandles.setFormatter(self.formaterr)
        consolehandles.setFormatter(self.formaterr)
        # 将头文件添加至logger中
        self.loggers.addHandler(filehandles)
        self.loggers.addHandler(consolehandles)

    def getlog(self):
        return self.loggers

    def getlog_name(self):
        return self.log_name

    def getlog_count(self):
        return self.formaterr


if __name__ == '__main__':
    ls = Logger('sogger').getlog()
    logger = Logger('sogger').getlog_name()
    ls.info('a')
