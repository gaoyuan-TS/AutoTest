#!/usr/bin/env python
# encoding: utf-8
"""
@author :gaoyuan
@contact:1103313679@qq.com
@time   :2020/5/12 11:13
"""

from selenium import webdriver
import time
import ConfigRead

path = ConfigRead.DRIVERS_PATH + 'firefox\\' + 'geckodriver.exe'
print(path)
driver = webdriver.Firefox(executable_path=path)
driver.maximize_window()
driver.get("https://www.baidu.com")
driver.close()
driver.quit()