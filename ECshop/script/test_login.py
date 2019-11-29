"""
test_login.py文件
    封装页面业务
    测试用例
"""
from page.login_page import Login_page
from common.base import open_browser,login_url
import unittest
from common.operartion_Excel import Operationxcel
import ddt

oper = Operationxcel(r'./datas/login_datas.xlsx').get_data_info()

@ddt.ddt
class Test_login(unittest.TestCase):
    def setUp(self) -> None:
        driver=open_browser()
        self.driver = driver
        self.login=Login_page(driver)
        self.login.open_url(login_url)
        self.imgs = []

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())

    def tearDown(self) -> None:
        self.login.close()
    @ddt.data(*oper)
    def test_01(self,data):
        """登陆测试用例,不记住密码
        张无默
        """

        self.login.input_username(data['username'])
        self.login.input_password(data['password'])
        self.login.click_submit()
        result=self.login.is_successed(data['username'])
        self.assertEqual(result,data['exepct'])
        self.add_img()


if __name__ == '__main__':

    unittest.main()