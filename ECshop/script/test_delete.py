import time

from page.address_page import UserCenterPage
from common.base import open_browser,login_url
from page.longin_page import LonginPage
import unittest,ddt


@ddt.ddt
class TestDelete(unittest.TestCase):
    def setUp(self) -> None:
        # 用例前置条件
        driver = open_browser()
        self.driver = driver
        self.user = UserCenterPage(driver)
        self.login = LonginPage(driver)
        self.user.open_url(login_url)
        uasename = "张si"
        password = "123456"
        self.login.input_username(uasename)
        self.login.input_password(password)
        self.login.click_submit()
        self.imgs = []

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
    def tearDown(self) -> None:
        # 5.关闭浏览器
        self.user.close()
    def test_accept_delect(self):
        """
        陈红琴
        :return:
        """
        self.user.eceivingAddr()   # 点击收货地址
        self.user.accept_delect()   # 确认删除
        self.add_img()

    def test_dismiss_delect(self):
        self.user.eceivingAddr()   # 点击收货地址
        self.user.dismiss_delect()   # 取消删除
        self.add_img()

if __name__ == '__main__':
    unittest.main()



