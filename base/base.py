import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import page


class Base():
    def __init__(self,driver):
        self.driver = driver
        #查找封装
    def find_element(self,loc,poll = 0.5):
        return WebDriverWait(self.driver,timeout=15,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    #点击封装
    def click_element(self,loc):
        self.find_element(loc).click()
    #输入值封装
    def send_element(self,loc,text):
        send = self.find_element(loc)
        send.clear()
        send.send_keys(text)
    #获取text文本封装
    def get_text(self,loc):
        return self.find_element(loc).text
    # 截图封装
    def get_screenshot(self):
        filepath = os.getcwd()+os.sep+"Image"+os.sep+"fild.png"
        self.driver.get_screenshot_as_file(filepath)
        #获取toast封装
    def get_toast(self,message):
        msg = By.XPATH,"//*[contains(@text,'"+message+"')]"
        return self.find_element(msg,poll = 0.1)
    # 滑动封装
    def drog_and_drop(self,el1,el2):
        self.driver.drag_and_drop(el1, el2)



