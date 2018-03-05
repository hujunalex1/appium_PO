#coding:utf-8

from  selenium.webdriver.common.by import By
import BasePage


class Dash(BasePage.Base):

    login_page_loc = (By.ID,'com.mzdk.app:id/profile_name')
    username_input = (By.ID,'com.mzdk.app:id/user_name')
    password_input = (By.ID,'com.mzdk.app:id/user_password')
    login_btn_submit = (By.ID,'com.mzdk.app:id/action_login')
    person_center = (By.NAME,u'我的')
    #进入我的页面
    def click_person(self):
        self.find_element(self.person_center).click()
    #点击登录按钮
    def click_login_btn(self):
        self.find_element(self.login_page_loc).click()
    #输入用户名
    def input_username(self,username):
        self.send_keys(self.username_input,username)
    #输入密码
    def input_password(self,password):
        self.send_keys(self.password_input,password)
    #点击确认登录按钮
    def submit_login(self):
        self.find_element(self.login_btn_submit).click()







