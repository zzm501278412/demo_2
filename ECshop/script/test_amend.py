from page.user_address_page import UserAddressPage
from common.base import open_browser,login_url
from page.longin_page import LonginPage
from common.operartion_Excel import Operationxcel
import unittest,ddt

oper = Operationxcel(r"./datas/amend_data.xlsx")
test_data = oper.get_data_info()

@ddt.ddt
class TestAmend(unittest.TestCase):
    def setUp(self) -> None:
        # 用例前置条件
        driver = open_browser()
        self.driver = driver
        self.user = UserAddressPage(driver)
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
    @ddt.data(*test_data)
    def test_amend(self,data):
        """
        陈红琴
        :param data:
        :return:
        """
        self.user.eceivingAddr()  # 点击收货地址
        self.user.send_keys_consignee(data["index"],data["consignee"])   # 通过索引修改收货人
        self.user.send_keys_address(data["index"],data["address"])   # 通过索引修改邮政编号
        self.user.send_keys_mobile(data["index"],str(data["mobile"]))   # 通过索引修改手机
        self.user.send_keys_zipcode(data["index"],str(data["zipcode"]))   # 通过索引修改详细地址
        self.user.click_submit(data["index"])   # 通过索引点击确认修改
        self.add_img()

if __name__ == '__main__':
    unittest.main()
