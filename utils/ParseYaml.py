#!/usr/bin/env python
# encoding: utf-8
"""
@author :gaoyuan
@contact:1103313679@qq.com
@time   :2020/5/12 15:43
"""

"""
解析读取config下.yaml文件的值
"""
from utils.ReadFile import YamlRead
from ConfigRead import *


class ParseYaml(object):

    PARAMETER_PATH = CONFIG_PATH+'Parameter.yaml'
    GUISELECTVALUE_PATH = CONFIG_PATH+'GuiSelectValue.yaml'
    TIMEWAIT_PATH = CONFIG_PATH+'TimeWait.yaml'

    def __init__(self, parameter=PARAMETER_PATH, guiselectvalue=GUISELECTVALUE_PATH, timewait = TIMEWAIT_PATH):
        self.parameter = YamlRead(parameter).data
        self.guiselectvalue = YamlRead(guiselectvalue).data
        self.timewait = YamlRead(timewait).data

    def ReadParameter(self, element, index=0):
        return self.parameter[index].get(element)

    def ReadGuiSelectValue(self, element, index=0):
        return self.guiselectvalue[index].get(element)

    def ReadTimeWait(self, element, index=0):
        return self.timewait[index].get(element)


if __name__ == '__main__':
    print(ParseYaml().ReadGuiSelectValue('BrowserType').get('Chrome'))
    print(ParseYaml().ReadParameter('IP'))
    print(type(ParseYaml().ReadTimeWait('casetime')))