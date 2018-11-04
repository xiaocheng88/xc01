import page
from base.base import Base

class Page_login(Base):
    def click_me(self):
        self.click_element(page.click_me)
    def username_ok(self):
        self.click_element(page.login_name_ok_link)
    def login_username(self,username):
        self.send_element(page.login_username,username)
    def login_password(self,password):
        self.send_element(page.login_password,password)
    def login_btn(self):
        self.click_element(page.login_btn)
        #get属性值以后必须返回
    def get_niname(self):
        return self.get_text(page.login_nickname)
    def click_setting(self):
        self.click_element(page.login_setting)
    def drog_drop(self):
        el1 = self.find_element(page.login_msg_send)
        el2 = self.find_element(page.login_modify_pwd)
        self.drog_and_drop(el1,el2)
    def click_exit(self):
        self.click_element(page.login_logout)
    def click_exit_ok(self):
        self.click_element(page.login_logout_ok)


