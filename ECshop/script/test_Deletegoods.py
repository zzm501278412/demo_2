"""
test_login.py文件
    1.封装页面业务:对页面上面多个元素操作后所实现的功能
    2.测试用例
"""

from page.login_pages import LoginPage
from page.shoppingcar_page import ShoppingCarPage

from common.base import open_browser,login_url
import ddt,unittest
from common.operartion_Excel import Operationxcel
import time

#准备测试数据
oper = Operationxcel(r"./datas/shopcar_data.xls")
test_data = oper.get_data_info()

@ddt.ddt
class TextShop(unittest.TestCase):
    def setUp(self) -> None:
        # 用例前置条件
        driver = open_browser()
        self.driver = driver
        self.shop = ShoppingCarPage(driver)
        self.login=LoginPage(driver)
        self.shop.open_url(login_url)
        self.imgs = []

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())

    def tearDown(self) -> None:
        # 返回首页继续够吗
        self.shop.backhome()
        self.shop.close()

    @ddt.data(*test_data)
    def test_shop(self, data):

        """
        谢新源
        :param data:
        :return:
        """
        #先登录
        self.shop.click_login()
        self.login.input_username("qwer")
        time.sleep(1)
        # 2.输入密码
        self.login.input_password("123456")
        time.sleep(1)
        # 3.点击立即登录
        self.login.submit()
        time.sleep(5)

        """登录测试用例:添加商品数量"""
        # 用例前置条件
        # 1.点击第一件商品
        self.shop.click_goods1()
        time.sleep(1)
        #2.输入数量
        self.shop.input_num(1)
        time.sleep(2)
        # 3.点击立即购买
        self.shop.click_im_buy()
        time.sleep(2)
        # 4.在购物车里 修改 商品数量
        # num2 = "5"
        self.shop.input_update_num(str(data["num"]))
        time.sleep(2)
        # 5.确定修改
        self.shop.keyboard_event()
        time.sleep(4)
        # 6.点击删除商品
        self.shop.click_delete()

        # 7.确定删除商品
        self.shop.real_delete()
        self.add_img()
        time.sleep(3)

        # # login.close()
if __name__ == '__main__':
    # from common.operation_Excel import OperationExcel
    # testlogin = TextLogin()
    # username = "qwer"
    # password = "123456"
    # testlogin.test_login(username,password)

    # oper = OperationExcel("../data/login_data.xls")
    # data = oper.get_data_info()
    # for i in data:
    #     testlogin.test_login(str(i["username"]),str(i["password"]))
    unittest.main()