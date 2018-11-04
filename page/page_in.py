from base.get_driver import get_driver
from base.base import Base
from page.page_login import Page_login


class pagein():
    def __init__(self):
        self.driver = get_driver()
    def page_login(self):
        return  Page_login(self.driver)

