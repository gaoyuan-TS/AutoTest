#!/usr/bin/env python
# encoding: utf-8
"""
@author :gaoyuan
@contact:1103313679@qq.com
@time   :2020/4/29 18:05
"""
import json

import datetime


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        else:
            return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':
    data = {"name": "Tom", "birthday": datetime.datetime.now()}
    print(json.dumps(data, cls=DateEncoder))
    # {"name": "Tom", "birthday": "2019-06-06 17:24:19"}
