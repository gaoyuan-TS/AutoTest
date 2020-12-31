#!/usr/bin/env python
# encoding: utf-8
"""
@author :gaoyuan
@contact:1103313679@qq.com
@time   :2020/5/12 15:34
"""
from selenium.webdriver.common.keys import Keys

from action.ObjectMap import ObjectMap
from utils.DirAndTime import DirAndTime
from action.WaitUnit import WaitUnit
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import *   # 导入所有异常类
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标操作
from utils.Logger import Logger
from ConfigRead import *
from utils.ParseYaml import ParseYaml
import time
import os
import win32gui
import win32con
import xlrd
import constants

logger = Logger('logger').getlog()


class PageAction(object):
    def __init__(self):
        self.parseyaml = ParseYaml()
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'css': By.CSS_SELECTOR,
            'link_text': By.LINK_TEXT,
            'xpath': By.XPATH,
            'class': By.CLASS_NAME,
            'tag': By.TAG_NAME,
            'link': By.PARTIAL_LINK_TEXT
        }

    def openBrowser(self):
        version = self.parseyaml.ReadParameter('Version')
        # 获取浏览器类型
        browser = self.parseyaml.ReadParameter('Browser')
        if browser == 'Google Chrome':
            logger.info("选择的浏览器为:%s浏览器" % browser)
            print("选择的浏览器为:%s浏览器" % browser)
            if '70' == version:
                path = DRIVERS_PATH + 'chrome\\' + '70.0.3538.97\\chromedriver.exe'
            elif '71' == version:
                path = DRIVERS_PATH + 'chrome\\' + '71.0.3578.137\\chromedriver.exe'
            elif '72' == version:
                path = DRIVERS_PATH + 'chrome\\' + '72.0.3626.69\\chromedriver.exe'
            elif '73' == version:
                path = DRIVERS_PATH + 'chrome\\' + '73.0.3683.68\\chromedriver.exe'
            elif '74' == version:
                path = DRIVERS_PATH + 'chrome\\' + '74.0.3729.6\\chromedriver.exe'
            elif '75' == version:
                path = DRIVERS_PATH + 'chrome\\' + '75.0.3770.140\\chromedriver.exe'
            elif '76' == version:
                path = DRIVERS_PATH + 'chrome\\' + '76.0.3809.126\\chromedriver.exe'
            elif '77' == version:
                path = DRIVERS_PATH + 'chrome\\' + '77.0.3865.40\\chromedriver.exe'
            elif '78' == version:
                path = DRIVERS_PATH + 'chrome\\' + '78.0.3904.11\\chromedriver.exe'
            elif '79' == version:
                path = DRIVERS_PATH + 'chrome\\' + '79.0.3945.16\\chromedriver.exe'
            elif '86' == version:
                path = DRIVERS_PATH + 'chrome\\' + '86.0.4240.22\\chromedriver.exe'
            else:
                logger.info('浏览器版本不符合，请检查浏览器版本')
                return
            option = Options()
            option.add_experimental_option('w3c', False)
            option.add_argument('--start-maximized')
            self.driver = webdriver.Chrome(executable_path=path, options=option)
            logger.info('启动谷歌浏览器')
            print('启动谷歌浏览器')
        elif browser == 'FireFox':
            logger.info("选择的浏览器为:%s浏览器" % browser)
            path = DRIVERS_PATH + 'firefox\\' + 'geckodriver.exe'
            self.driver = webdriver.Firefox(executable_path=path)
            self.driver.maximize_window()
            logger.info('启动火狐浏览器')
            print('启动火狐浏览器')
        else:
            # 驱动创建完成后，等待创建实例对象
            WaitUnit(self.driver)

    def openBrowsers(self, browser):
        try:
            version = self.parseyaml.ReadParameter('Version')
            # 获取浏览器类型
            if browser == 'Google Chrome':
                logger.info("选择的浏览器为:%s浏览器" % browser)
                print("选择的浏览器为:%s浏览器" % browser)
                if '70' == version:
                    path = DRIVERS_PATH + 'chrome\\' + '70.0.3538.97\\chromedriver.exe'
                elif '71' == version:
                    path = DRIVERS_PATH + 'chrome\\' + '71.0.3578.137\\chromedriver.exe'
                elif '72' == version:
                    path = DRIVERS_PATH + 'chrome\\' + '72.0.3626.69\\chromedriver.exe'
                elif '73' == version:
                    path = DRIVERS_PATH + 'chrome\\' + '73.0.3683.68\\chromedriver.exe'
                elif '74' == version:
                    path = DRIVERS_PATH + 'chrome\\' + '74.0.3729.6\\chromedriver.exe'
                elif '75' == version:
                    path = DRIVERS_PATH + 'chrome\\' + '75.0.3770.140\\chromedriver.exe'
                elif '76' == version:
                    path = DRIVERS_PATH + 'chrome\\' + '76.0.3809.126\\chromedriver.exe'
                elif '77' == version:
                    path = DRIVERS_PATH + 'chrome\\' + '77.0.3865.40\\chromedriver.exe'
                elif '78' == version:
                    path = DRIVERS_PATH + 'chrome\\' + '78.0.3904.11\\chromedriver.exe'
                elif '79' == version:
                    path = DRIVERS_PATH + 'chrome\\' + '79.0.3945.16\\chromedriver.exe'
                elif '86' == version:
                    path = DRIVERS_PATH + 'chrome\\' + '86.0.4240.22\\chromedriver.exe'
                else:
                    logger.info('浏览器版本不符合，请检查浏览器版本')
                    return
                option = Options()
                option.add_experimental_option('w3c', False)
                option.add_argument('--start-maximized')
                self.driver = webdriver.Chrome(executable_path=path, options=option)
                logger.info('启动谷歌浏览器')
                print('启动谷歌浏览器')
            elif browser == 'FireFox':
                logger.info("选择的浏览器为:%s浏览器" % browser)
                path = DRIVERS_PATH + 'firefox\\' + 'geckodriver.exe'
                self.driver = webdriver.Firefox(executable_path=path)
                self.driver.maximize_window()
                logger.info('启动火狐浏览器')
                print('启动火狐浏览器')
        except Exception as e:
            logger.info('浏览器类型不符，请选择Chrome或者Firefox')
            print('浏览器类型不符，请选择Chrome或者Firefox')
            print(e)
        else:
            # 驱动创建完成后，等待创建实例对象
            WaitUnit(self.driver)

    def quitBrowser(self):
        logger.info('退出浏览器')
        print('退出浏览器')
        self.driver.quit()

    def closeBrowser(self):
        logger.info('关闭当前页面')
        print('关闭当前页面')
        self.driver.close()

    def back(self):
        '''
        退回浏览器上一个页面
        :return:
        '''
        # try:
        if self.driver.current_url == 'data:,':
            self.driver.back()
            logger.info('返回到%s' % self.driver.current_url)
            print('返回到%s' % self.driver.current_url)
        # except Exception as e:
        #     logger.info('退回浏览器失败')
        #     print('退回浏览器失败')
        #     print(e)
        else:
            logger.info('已经是第一个页面')
            print('已经是第一个页面')
            return

    def foword(self):
        '''
        前进浏览器上一个页面
        :return:
        '''
        # try:
        self.driver.forward()
        logger.info('前进到%s' % self.driver.current_url)
        print('前进到%s' % self.driver.current_url)
        # except Exception as e:
        #     logger.info('前进页面失败')
        #     print('前进页面失败')
        #     print(e)

    def refresh(self):
        '''
        刷新浏览器
        :return:
        '''
        logger.info('刷新浏览器')
        print('刷新浏览器')
        self.driver.refresh()

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def getUrl(self, url):
        """
        加载网址
        :return:
        """
        # try:
        logger.info('进入%s' % url)
        print('进入%s' % url)
        self.driver.get(url)
        # except Exception as e:
        #     logger.info('%s进入失败' % url)
        #     print('%s进入失败' % url)
        #     print(e)

    def sleep(self, sleepSeconds):
        """
        强制等待时间，单位S
        :param sleepSeconds:
        :return:
        """
        # try:
        logger.info('休眠%s秒' % sleepSeconds)
        print('休眠%s秒' % sleepSeconds)
        time.sleep(int(sleepSeconds))
        # except Exception as e:
        #     print(e)

    def clear(self, by, locator):
        """
        清空输入框
        :return:
        """
        # try:
        logger.info('清空输入框')
        print('清空输入框')
        ObjectMap(self.driver).getElement(by, locator).clear()
        # except Exception as e:
        #     logger.info('清空失败')
        #     print('清空失败')
        #     print(e)

    def inputValue(self, by, locator, value):
        """
        输入框输入值
        :param by:
        :param locator:
        :param value:
        :return:
        """
        # try:
        logger.info('输入框输入%s' % value)
        print('输入框输入%s' % value)
        ObjectMap(self.driver).getElement(locator).send_keys(value)
        # except Exception as e:
        #     logger.info('输入框输入值错误')
        #     print('输入框输入值错误')
        #     print(e)

    def clearAndInput(self, by, locator, value):
        '''
        清除输入框再输入值
        :return:
        '''
        logger.info('清空输入框')
        print('清空输入框')
        ObjectMap(self.driver).getElement(by, locator).clear()
        logger.info('输入框输入%s' % value)
        print('输入框输入%s' % value)
        ObjectMap(self.driver).getElement(by, locator).send_keys(value)

    def uploadFile(self, by, locator, value):
        '''
        上传单个文件input标签  type="file"
        :param by:
        :param locator:
        :param value:
        :return:
        '''
        ObjectMap(self.driver).getElement(by, locator).send_keys(value)
        logger.info('上传文件%s' % value)
        print('上传文件%s' % value)

    def uploadFiles(self, by, locator, value):
        '''
        上传多个文件，value为文件夹路径，input标签
        :param by:
        :param locator:
        :param value:
        :return:
        '''
        for root, dirs, files in os.walk(value):
            for i in files:
                ObjectMap(self.driver).getElement(by, locator).send_keys(value + '\\' + i)
                logger.info('上传文件%s' % i)
                print('上传文件%s' % i)

    def upload_file_windows(self, file_path):
        '''
        :param file_path:上传文件的路径,需点击打开上传按钮，弹出windows窗口再调用 chrome 可调用
        :return:
        '''
        dialog = win32gui.FindWindow("#32770", u"打开") #窗口左上角文字
        comboxex32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        combox = win32gui.FindWindowEx(comboxex32, 0, "ComboBox", None)
        edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
        button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&0)")
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    def assertTitle(self, titlestr):
        """
        断言页面标题
        :param titlestr:
        :return:
        """
        # try:
        logger.info('"%s"标题存在' % titlestr)
        print('"%s"标题存在' % titlestr)
        assert titlestr in self.driver.title, '%s标题不存在' % titlestr
        # except AssertionError as e:
        #     logger.info('"%s"标题不存在' % titlestr)
        #     print('"%s"标题不存在' % titlestr)
        #     print(e)
        # except Exception as e:
        #     logger.info('断言失败')
        #     print('断言失败')
        #     print(e)

    def assert_string_in_pageSource(self, assstring):
        """
        断言字符串是否包含在源码中
        :param assstring:
        :return:
        """
        # try:
        logger.info('"%s"存在页面中' % assstring)
        print('"%s"存在页面中' % assstring)
        assert assstring in self.driver.page_source, "'%s'在页面中不存在" % assstring
        # except AssertionError as e:
        #     logger.info('"%s"在页面中未找到' % assstring)
        #     print('"%s"在页面中未找到' % assstring)
        #     print(e)
        # except Exception as e:
        #     logger.info('断言失败')
        #     print('断言失败')
        #     print(e)

    def assertEqule(self, by, locator, value):
        '''
        检查指定元素字符串与预期结果是否相同
        :return:
        '''
        # try:
        getValue = ObjectMap(self.driver).getElement(by, locator).get_attribute('value')
        getText = ObjectMap(self.driver).getElement(by, locator).text
        if getValue == getText:
            assert ObjectMap(self.driver).getElement(by, locator).get_attribute('value') == value
            logger.info('%s=%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
            print('%s=%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
        elif getValue == '' or getValue is None:
            assert ObjectMap(self.driver).getElement(by, locator).text == value
            logger.info('%s=%s' % (ObjectMap(self.driver).getElement(by, locator).text, value))
            print('%s=%s' % (ObjectMap(self.driver).getElement(by, locator).text, value))
        elif getText == '' or getText is None:
            assert ObjectMap(self.driver).getElement(by, locator).get_attribute('value') == value
            logger.info('%s=%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
            print('%s=%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
        else:
            assert ObjectMap(self.driver).getElement(by, locator).get_attribute('value') == value
            logger.info('%s=%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
            print('%s=%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
        # except AssertionError:
        #     getValue = ObjectMap(self.driver).getElement(by, locator).get_attribute('value')
        #     getText = ObjectMap(self.driver).getElement(by, locator).text
        #     if getValue == getText:
        #         logger.info('%s!=%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
        #         print('%s!=%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
        #     elif getValue == '' or getValue is None:
        #         logger.info('%s!=%s' % (ObjectMap(self.driver).getElement(by, locator).text, value))
        #         print('%s!=%s' % (ObjectMap(self.driver).getElement(by, locator).text, value))
        #     elif getText == '' or getText is None:
        #         logger.info('%s!=%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
        #         print('%s!=%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
        #     else:
        #         logger.info('%s!=%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
        #         print('%s!=%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
        # except AttributeError:
        #     logger.info('页面中未找到元素')
        #     print('页面中未找到元素')
        # except TimeoutError:
        #     logger.info('页面中未找到元素')
        #     print('页面中未找到元素')
        # except Exception:
        #     logger.info('断言失败')
        #     print('断言失败')

    def assertLen(self, by, locator, value):
        '''
        检查指定元素字符串长度
        :return:
        '''
        # try:
        getValue = ObjectMap(self.driver).getElement(by, locator).get_attribute('value')
        getText = ObjectMap(self.driver).getElement(by, locator).text
        if getValue == getText:
            assert len(ObjectMap(self.driver).getElement(by, locator).get_attribute('value')) == int(value)
            logger.info('"%s"长度为%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
            print('"%s"长度为%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
        elif getValue == '' or getValue is None:
            assert len(ObjectMap(self.driver).getElement(by, locator).text) == int(value)
            logger.info('"%s"长度为%s' % (ObjectMap(self.driver).getElement(by, locator).text, value))
            print('"%s"长度为%s' % (ObjectMap(self.driver).getElement(by, locator).text, value))
        elif getText == '' or getText is None:
            assert len(ObjectMap(self.driver).getElement(by, locator).get_attribute('value')) == int(value)
            logger.info(
                '"%s"长度为%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
            print('"%s"长度为%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
        else:
            assert len(ObjectMap(self.driver).getElement(by, locator).get_attribute('value')) == int(value)
            logger.info(
                '"%s"长度为%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
            print('"%s"长度为%s' % (ObjectMap(self.driver).getElement(by, locator).get_attribute('value'), value))
        # except AssertionError as e:
        #     logger.info('"%s" 在页面中未找到' % ObjectMap(self.driver).getElement(by,locator).get_attribute('value'))
        #     print('"%s" 在页面中未找到' % ObjectMap(self.driver).getElement(by,locator).get_attribute('value'))
        # except TimeoutException:
        #     logger.info('页面中未找到元素')
        #     print('页面中未找到元素')
        # except Exception as e:
        #     logger.info('断言失败')
        #     print('断言失败')

    def assertElement(self, by, locator):
        '''
        判断元素是否存在
        :return:
        '''
        # flag = True
        # try:
        assert ObjectMap(self.driver).getElement(by, locator)
        # return flag
        # except AssertionError as e:
        #     logger.info('页面中未找到元素')
        #     print('页面中未找到元素')
        # except TimeoutException:
        #     logger.info('页面中未找到元素')
        #     print('页面中未找到元素')
        # except Exception as e:
        #     logger.info('断言失败')
        #     print('断言失败')

    def assertUrl(self, Url):
        '''
        判断当前网址是否和指定网址相同
        :param Url:
        :return:
        '''
        assert self.driver.current_url == Url
        logger.info('%s==%s' % (self.driver.current_url, Url))
        print('%s==%s' % (self.driver.current_url, Url))

    def getTitle(self):
        """
        获取页面title
        :return:
        """
        try:
            logger.info('获取页面标题：%s' % self.driver.title)
            print('获取页面标题：%s' % self.driver.title)
            return self.driver.title
        except Exception as e:
            logger.info('获取页面标题失败')
            print('获取页面标题失败')

    def getPageSource(self):
        """
        获取页面源码
        :return:
        """
        # try:
        return self.driver.page_source
        # except Exception as e:
        #     print(e)

    def switchToFrame(self, by, locator):
        """
        切换到frame页面内
        :param by:
        :param locator:
        :return:
        """
        # try:
        self.driver.switch_to.frame(ObjectMap(self.driver).getElement(by, locator))
        # except Exception as e:
        #     print(e)

    def switchToDefault(self):
        """
        切换到默认的frame页面
        :return:
        """
        # try:
        self.driver.switch_to.default_content()
        # except Exception as e:
        #     print(e)

    def click(self, by, locator):
        """
        元素点击
        :return:
        """
        # try:
        logger.info('点击元素：%s' % locator)
        print('点击元素：%s' % locator)
        ObjectMap(self.driver).getElement(by, locator).click()
        # except Exception as e:
        #     logger.info('点击元素失败')
        #     print('点击元素失败')
        #     print(e)

    def saveScreeShot(self, file, casename):
        """
        屏幕截图
        :return:
        """
        picturename = SCREENSHOTS_PATH + file + '\\' + casename
        if not os.path.exists(picturename):
            os.makedirs(picturename)
            picturename = picturename + '\\' + DirAndTime.getCurrentTime() + '.png'
        else:
            picturename = picturename + '\\' + DirAndTime.getCurrentTime() + '.png'
        try:
            self.driver.get_screenshot_as_file(picturename)
        except Exception as e:
            print(e)
        else:
            return picturename

    def wait_find_element(self, by, locator):
        '''
        显性等待30S判断单个元素是否可见，可见返回元素，否则抛出异常
        :param loc: 传入参数为By.xx(xx为元素定位方式),Value(为元素定位内容)
        :return:
        '''
        # try:
        if by.lower() in self.byDic:
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((self.byDic[by.lower()], locator)))
            return element
        # except NoSuchElementException:
        #     logger.exception('找不到元素')
        #     print('找不到元素')
        # except TimeoutException:
        #     logger.exception('元素查找超时')
        #     print('元素查找超时')
        # except:
        #     logger.exception('查找失败')
        #     print('查找失败')

    def not_wait_find_element(self, by, locator):
        '''
        显性等待60S判断单个元素是否可见，可见返回元素，否则抛出异常
        :param loc: 传入参数为By.xx(xx为元素定位方式),Value(为元素定位内容)
        :return:
        '''
        # try:
        if by.lower() in self.byDic:
            element = WebDriverWait(self.driver, 30).until_not(
                EC.presence_of_element_located((self.byDic[by.lower()], locator)))
            return element
        # except NoSuchElementException:
        #     logger.exception('找不到元素')
        #     print('找不到元素')
        # except TimeoutException:
        #     logger.exception('元素查找超时')
        #     print('元素查找超时')
        # except:
        #     logger.exception('查找失败')
        #     print('查找失败')

    def text_wait_find_element(self, by, locator):
        '''
        显性等待30S判断单个元素是否可见，可见返回元素，否则抛出异常
        :param loc: 传入参数为By.xx(xx为元素定位方式),Value(为元素定位内容)
        :return:
        '''
        # try:
        if by.lower() in self.byDic:
            element = WebDriverWait(self.driver, 30).until(
                EC.text_to_be_present_in_element(self.byDic[by.lower()], locator))
            return element
        # except NoSuchElementException:
        #     logger.exception('找不到元素')
        #     print('找不到元素')
        # except TimeoutException:
        #     logger.exception('元素查找超时')
        #     print('元素查找超时')
        # except:
        #     logger.exception('查找失败')
        #     print('查找失败')

    def not_text_wait_find_element(self, by, locator):
        '''
        显性等待30S判断单个元素是否可见，可见返回元素，否则抛出异常
        :param loc: 传入参数为By.xx(xx为元素定位方式),Value(为元素定位内容)
        :return:
        '''
        # try:
        if by.lower() in self.byDic:
            element = WebDriverWait(self.driver, 30).until_not(
                EC.text_to_be_present_in_element(self.byDic[by.lower()], locator))
            return element
        # except NoSuchElementException:
        #     logger.exception('找不到元素')
        #     print('找不到元素')
        # except TimeoutException:
        #     logger.exception('元素查找超时')
        #     print('元素查找超时')
        # except:
        #     logger.exception('查找失败')
        #     print('查找失败')

    def move_to_element(self, by, locator):
        '''
        :param loc:loc = (By.xx,element)
        :return:
        '''
        # try:
        element = self.driver.find_element(by, locator)
        t = self.driver.find_element(by, locator).text
        ActionChains(self.driver).move_to_element(element).perform()
        logger.info("鼠标悬浮在%s" % t)
        print("鼠标悬浮在%s" % t)
        # except:
        #     logger.exception("未找到元素")
        #     print("未找到元素")

    def dropDown(self, p):
        """
        边框下拉滑动
        :param p:
        :return:
        """
        js = "var q=document.documentElement.scrollTop=%s" % p
        self.driver.execute_script(js)
        logger.info("滑动下拉框-距离%s" % p)
        print("滑动下拉框-距离%s" % p)

    def scroll_top(self):
        '''滚动到顶部'''
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)

    def scroll_end(self):
        '''滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def Enter(self, by, locator):
        # 模拟键盘回车
        ObjectMap(self.driver).getElement(by, locator).send_keys(Keys.ENTER)

    def Down_end(self, count):
        '''
        模拟按下键盘的 下 箭头 方向键,count 为按下的次数
        :return:
        '''
        for i in range(count):
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            ActionChains(self.driver).key_down(Keys.DOWN).perform()


if __name__ == '__main__':

    # try:
    #     p = PageAction()
    #     # p.openBrowsers('Google Chrome')
    #     p.openBrowsers('Google Chrome')
    #     o = ObjectMap(p.driver)
    #     p.getUrl("http://zs-beta.cntracechain.com/#/login")
    #     p.driver.maximize_window()
    #     p.driver.implicitly_wait(10)
    #     p.inputValue('xpath', '/html/body/div/div/section/main/div/div[2]/div/div/div[3]/form/div/div[2]/div/div/input',
    #                  'gaoyuan')
    #     p.inputValue('xpath', '/html/body/div/div/section/main/div/div[2]/div/div/div[3]/form/div/div[3]/div/div/input',
    #                  'zs666666')
    #
    #     p.click('xpath', '//*[@id="login"]/section/main/div/div[2]/div/div/div[3]/form/div/div[5]/div/button')
    #
    #     p.click('xpath', '//*[@id="home"]/section/section/main/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div/span')
    #     p.sleep(2)
    #     p.click('xpath', '//*[@id="home"]/section/section/main/div[2]/div[1]/button')
    #     p.sleep(2)
    #     print('下拉到底部')
    #     p.Down_end(4)
    #     p.click('xpath', '/html/body/div/div/section/section/main/div[2]/div/div[2]/div[3]/div[1]/div[2]/div[1]/div')
    #     print('上传图片')
    #     p.sleep(5)
    #     p.upload_file_windows(r'C:\Users\Administrator\Desktop\1.jpg')
    #     p.sleep(4)
    # except Exception as e:
    #     print(e)
    # finally:
    #     p.quitBrowser()
    path = 'D:\AutoTest\exceltemplate\测试.xlsx'
    book_data = xlrd.open_workbook(path)
    book_sheet = book_data.sheet_by_index(0)
    nrows = book_sheet.nrows
    ncols = book_sheet.ncols
    row1 = book_sheet.row_values(0)
    col = book_sheet._maxdatacolx
    # col = len(row1)
    print(row1)
    print(col)
    list = []
    for x in range(1,nrows):
        row_value = book_sheet.row_values(x)
        row_dis ={}
        for y in range(0,col):
            row_dis[row1[y]] = row_value[y]
            list.append(row_dis)

    print(list)
    # for y in range(0,ncols):
    #     col_value = book_sheet.col_values(y)
    #     print(col_value)
