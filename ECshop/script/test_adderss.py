import time
from page.address_page import UserCenterPage
from common.base import open_browser,login_url
from common.operartion_Excel import Operationxcel
from page.longin_page import LonginPage
import unittest,ddt
import threading

oper = Operationxcel(r"./datas/adderss_data.xlsx")
test_data = oper.get_data_info()

@ddt.ddt
class TestAdderss(unittest.TestCase):
    def setUp(self) -> None:
        # 用例前置条件

        driver = open_browser()
        self.driver = driver
        self.user = UserCenterPage(driver)
        self.login = LonginPage(driver)
        self.imgs = []
        self.user.open_url(login_url)
    def tearDown(self) -> None:
        # 5.关闭浏览器
        self.user.close()


    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())

    @ddt.data(*test_data)
    def test_adderss(self,data):
        """
        陈红琴
        :param data:
        :return:
        """
        uasename = "张si"
        password = "123456"
        self.login.input_username(uasename)
        self.login.input_password(password)
        self.login.click_submit()
        self.user.eceivingAddr()   # 点击收货地址
        try:
            self.user.province()  # 选择市
            time.sleep(2)
            self.user.city()  # 选择省
            time.sleep(2)
            self.user.district()  # 选择区
            time.sleep(2)
            self.user.consignee(data["consignee"])  # 输入收货人
            self.user.address(data["address"])  # 输入详细地址
            self.user.tel(str(data["tel"]))  # 输入电话
            self.user.newEceivingAddr()  # 点击新增收货地址
            self.add_img()
            time.sleep(2)
        except:
            return False


if __name__ == '__main__':
    unittest.main()