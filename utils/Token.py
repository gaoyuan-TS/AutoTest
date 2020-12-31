#!/usr/bin/env python
# encoding: utf-8
"""
@author :gaoyuan
@contact:1103313679@qq.com
@time   :2020/12/30 14:29
"""

import time
import hashlib
#获取时间戳


class Time(object):
    def t_stamp(self):
        t = time.time()
        t_stamp = int(t)
        # print('当前时间戳：', t_stamp)
        return t_stamp


#根据账号名称,时间戳生成token对象
class Token(object):
    def __init__(self,account):
        self.account = account

    def get_token(self):
        strs = self.account + str(Time().t_stamp())
        hl = hashlib.md5()
        hl.update(strs.encode("utf8"))
        token = hl.hexdigest()
        print('MD5加密前',strs)
        print('MD5加密后',token)
        return token

if __name__ == '__main__':
    tokenprogramer = Token('gaoyuan').get_token()