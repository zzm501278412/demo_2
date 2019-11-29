from page.shopping_page import ShoppingPage
from page.login_page1 import LogingPage
from page.adder_page import AdderPage
from common.base import open_browser,login_url
import time
import unittest
class Test_Shopping(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=open_browser()
        self.login=LogingPage(self.driver)
        self.login.open_url(login_url)
        self.imgs = []

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
    def tearDown(self) -> None:
        self.login.close()
    def test_shopping01(self):
        """
        刘恒希
        先登录购买
        :return:
        """
        # 输入账号
        self.login.input_username("zzm6226")
        # 输入密码
        self.login.input_password("zzm6226")
        # 点击登录
        self.login.click_submit()
        # 使用购买流程
        shop=ShoppingPage(self.driver)
        # 进入主页面
        shop.click_gohome()
        # 点击商品
        shop.click_photo()
        # 点击立刻购买
        shop.click_instantBuy()
        # 点击去结算
        shop.click_settling()
        time.sleep(2)
        # 选择配送方式
        shop.click_distribution()
        # 选择支付方式
        shop.click_payment_loc()
        # 选择商品保证
        shop.click_pack_loc()
        # 选择贺卡
        shop.click_card()
        # 输入祝福语
        shop.input_christmas("测试祝福语")
        # 点击开发票
        shop.click_receipt()
        # 点击发票类型下拉框
        shop.click_type()
        # 输入附言
        shop.input_text("快发货")
        # 提交订单
        shop.refer()
        # 确认商品购买成功
        self.add_img()
        result=shop.is_sucess("感谢您在本店购物！您的订单已提交成功，请记住您的订单号: ")
        self.assertTrue(result,msg="失败了哦")

    def test_shopping02(self):
        """
        没有登录的时候购买流程
        :return:
        """
        # 使用购买流程
        shop = ShoppingPage(self.driver)
        # 进入主页面
        shop.click_gohome()
        # 点击商品
        shop.click_photo()
        # 点击立刻购买
        shop.click_instantBuy()
        # 点击去结算
        shop.click_settling()
        # 点击不打算登录直接购买
        shop.no_Login()
        # 开始填写地址簿
        adder=AdderPage(self.driver)
        # 选择省份
        adder.province()
        time.sleep(2)
        # 选择城市
        adder.city()
        time.sleep(2)
        # 选择区域
        adder.district()
        time.sleep(2)
        # 填写收货人姓名
        adder.name("小叮当")
        # 填写收货人邮箱
        adder.email("555555@qq.com")
        # 填写收货人地址
        adder.adder("保加利亚")
        # 填写电话
        adder.tell("13585421548")
        # 点击配送至这个地址
        adder.click_tell()
        # 开始填写下单信息
        shop = ShoppingPage(self.driver)
        # 选择配送方式
        shop.click_distribution()
        # 选择支付方式
        shop.click_payment_loc()
        # 选择商品保证
        shop.click_pack_loc()
        # 选择贺卡
        shop.click_card()
        # 输入祝福语
        shop.input_christmas("测试祝福语")
        # 点击开发票
        shop.click_receipt()
        # 点击发票类型下拉框
        shop.click_type()
        # 输入附言
        shop.input_text("快发货")
        # 提交订单
        shop.refer()
        # 确认商品购买成功
        self.add_img()
        result = shop.is_sucess("感谢您在本店购物！您的订单已提交成功，请记住您的订单号: ")
        self.assertTrue(result, msg="失败了哦")
if __name__ == '__main__':
    unittest.main()