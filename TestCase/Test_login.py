#coding:utf-8

import unittest
from appium import webdriver
from PO import DashPage,BasePage
import time




class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', BasePage.Base.desired_caps)
        self.username = 'xxxxx'
        self.password = 'xxxx'

    def test_login(self):
        login_page = DashPage.Dash(self.driver)
        login_page.click_person()
        login_page.click_login_btn()
        login_page.input_username(self.username)
        login_page.input_password(self.password)
        login_page.submit_login()

    def tearDown(self):
        time.sleep(4)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()




