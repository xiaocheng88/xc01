import os
import pytest
import sys
sys.path.append(os.getcwd())
from page.page_in import pagein
from base.read_yaml import ReadYaml
import allure

def get_data():
    list1 = []
    for data in ReadYaml("get_data.yaml").read_yaml().values():
        list1.append((data.get("username"), data.get("password"), data.get("expect_result"), data.get("expect_toast")))
    return list1

class Test_Login():

    def setup_class(self):
        #实例化统一入口类
        self.page = pagein()
        self.login = self.page.page_login()
        self.login.click_me()
        self.login.username_ok()
    def teardown_class(self):
        #注意pagein是没有driver的，所以用self.login来实现退出
        self.login.driver.quit()
    # @pytest.mark.parametrize("username,password,expect_result",ry())
    @pytest.mark.parametrize("username,password,expect_result,expect_toast",get_data())
    def test_login(self,username,password,expect_result,expect_toast):
        #如果条件成立就是正向用例
        if expect_result:
            try:
                self.login.login_username(username)
                self.login.login_password(password)
                self.login.login_btn()
                niname = self.login.get_niname()
                assert expect_result in niname
                self.login.click_setting()
                self.login.drog_drop()
                self.login.click_exit()
                self.login.click_exit_ok()
                self.login.click_me()
                self.login.username_ok()
            except:
                self.login.get_screenshot()
                with open("./Image/fild.png","rb")as f:
                    allure.attach("失败原因请看附加图",f.read(),allure.attach_type.PNG)
                raise
            #若if条件没有成立就是逆向用例，就是没有登录成功，所以要再次输入账号密码，然后断言toast消息，确定问题所在
        else:
            try:
                self.login.login_username(username)
                self.login.login_password(password)
                self.login.login_btn()
                assert expect_toast in self.login.get_toast(expect_toast)
            except:
                self.login.get_screenshot()
                with open("./Image/fild.png", "rb")as f:
                    allure.attach("失败原因请看附加图", f.read(), allure.attach_type.PNG)
                raise


