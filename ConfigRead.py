#!/usr/bin/env python
# encoding: utf-8
"""
@author :gaoyuan
@contact:1103313679@qq.com
@time   :2020/5/12 11:47
"""

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

'''通过BASE_DIR获取项目所在的路径（相对路径），然后根据项目路径获取其他文件的相对路径'''

# action(公共文件)路径
ACTION_PATH = BASE_DIR + '\\action\\'
# config(配置文件)路径
CONFIG_PATH = BASE_DIR + '\\config\\'
# drivers(驱动文件)路径
DRIVERS_PATH = BASE_DIR + '\\drivers\\'
# exceltemplate(用例模板)路径
EXCELTEMPLATE_PATH = BASE_DIR +'\\exceltemplate\\'
#logs(日志文件)路径BASE_DIR
LOGS_PATH = BASE_DIR + '\\logs\\'
# report(报告文件)路径
REPORT_PATH = BASE_DIR + '\\report\\'
# screenshots(截图文件)路径
SCREENSHOTS_PATH = BASE_DIR + '\\screenshots\\'
# testcase(测试文件)路径
TESTCASE_PATH = BASE_DIR+ '\\testcase\\'
# testdata(用例文件)路径
TESTDATA_PATH = BASE_DIR+ '\\testdata\\'
# Utils(驱动文件)路径
UTILS_PATH = BASE_DIR + '\\Utils\\'
# resource(资源文件)路径
RESOURSE_PATH = BASE_DIR+ '\\resource\\'


'''EXCEL测试用例部分字段的列号'''

# 用例编号
testCase_Num = 2
# 用例工作表
testCase_Sheet = 3
# 是否执行
testCase_Isimplement = 6
# 执行结束时间
testCase_EndTime = 7
# 结果
testCase_Result = 8


'''EXCEL用例步骤部分字段的列号'''

# 用例编号
testStep_Num = 1
# 工作表
testStep_Moudle = 2
# 预置条件
testStep_Preset = 3
# 用例标题
testSteo_Title = 4
# 预期结果
testStep_Expect = 5
# 测试步骤描述
testStep_Describe = 6
# 关键字
testStep_KeyWord = 7
# 定位方式
testStep_Location = 8
# 表达式
testStep_Locator = 9
# 操作值
testStep_Value = 10
# 测试执行时间
testStep_EndTime = 11
# 测试结果
testStep_Result = 12
# 错误信息
testStep_Error = 17
# 截图
testStep_Picture = 18

print(DRIVERS_PATH)