#coding:utf-8

from selenium.webdriver.support.ui import WebDriverWait
import time

class Base:
    driver = None
    desired_caps={}
    desired_caps['platformName'] = 'Android' #设备系统
    desired_caps['platformVersion'] = '6.0.1' #设备系统版本
    desired_caps['deviceName'] = '127.0.0.1:62001' #设备名称
    desired_caps['appPackage'] = 'com.mzdk.app' #测试app包名
    desired_caps['appActivity'] = '.activity.MainActivity'  #测试appActivity
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    def __init__(self,appium_driver):
        self.driver = appium_driver

#重新封装单个元素定位方法

    def find_element(self,loc):
        try:
            WebDriverWait(self.driver,15).until(lambda driver:driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print u'%s 页面中未能找到 %s 元素' %(self,loc)

#重新封装输入方法
    def send_keys(self,loc,value,clear_first=True,click_first=True):
        try:
            if click_first:
                self.find_element(loc).click()
            if clear_first:
                self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)
        except AttributeError:
            print '%s 页面未能找到 %s 元素' %(self,loc)




