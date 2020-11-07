#!/usr/bin/env python
# encoding: utf-8
"""
@author :gaoyuan
@contact:1103313679@qq.com
@time   :2020/5/12 14:30
"""
from datetime import datetime, date


class DirAndTime(object):

    # 静态方法，调用时可以选择传入参数
    @staticmethod
    def getCurrentDate():
        '''
        获取当前日期 格式: 2019-11-7
        :return:
        '''
        try:
            # 获取当前日期
            currentDate = date.today()
        except Exception as e:
            raise e
        else:
            return str(currentDate)

    @staticmethod
    def getCurrentTime():
        '''
        获取当前日期 格式: 2019-11-7
        :return:
        '''
        try:
            # 获取当前日期
            currentTime = datetime.now()
            currentTime = currentTime.strftime('%Y-%m-%d-%H-%M-%S')
        except Exception as e:
            raise e
        else:
            return currentTime



if __name__ == '__main__':
    print(DirAndTime.getCurrentDate())
    print(DirAndTime.getCurrentTime())