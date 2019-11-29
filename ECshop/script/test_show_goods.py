"""
test_login.py文件
    1.封装页面业务
    2.测试用例
"""
from page.show_goods_page import ShowPage
from common.base import open_browser,login_url
import unittest
import time


class TestShow(unittest.TestCase):
    def setUp(self) -> None:
        # 用例前置条件
        driver = open_browser()
        self.driver =driver
        self.show = ShowPage(driver)
        self.show.open_url(login_url)
        self.imgs = []

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())

    def tearDown(self) -> None:
        # 5.关闭浏览器
        self.show.close()

    def test_show(self):
        """商品浏览测试用例
        白文怡"""

        # 1.输入用户名
        self.show.input_username("max")
        # 2.输入密码
        self.show.input_password("123456")
        # 3.点击立即登录
        self.show.click_submit()
        # 点击首页
        self.show.click_home_page()
        # 点击搜索按钮
        self.show.click_grabble()
        time.sleep(2)
        #循环页面
        self.add_img()
        self.show.click_goods()



if __name__ == '__main__':
    unittest.main()
