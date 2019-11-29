from common.base import Base,open_browser,login_url
from page.login_page1 import LogingPage
class ShoppingPage(Base):
    # username_loc = ("name", "username")  # 用户名输入框
    # password_loc = ("name", "password")  # 密码框
    # submit_loc = ("class name", "us_Submit")  # 立即登录按钮
    # result_loc = ("class name", "f4_b")  # 登录成功后的结果
    url = "http://172.16.1.244/ecshop/user.php"  # 网址
    gohome_loc=("css selector","#mainNav > div > ul > li:nth-child(1) > a")# 返回主页定位
    photo_loc = ("css selector", "body > div.index-body > div > div > "
                               "div:nth-child(2) > "
                               "div.goods-right > div "
                               "> a:nth-child(1) > "
                               "div.img-box > img")  # 智能相机商品
    instantBuy_loc = ("css selector", "#ECS_FORMBUY > ul > li.padd > "
                                    "table > tbody > tr > td.td1 > a > img")  # 立即购买按钮
    settling_loc = ("css selector", "body > div:nth-child(7) > div.flowBox "
                                  "> table > tbody > tr > td:nth-child(2) > a > img")  # 去结算按钮
    onBuy_loc = ("css selector", "body > div:nth-child(7) > div.flowBox > table > "
                               "tbody > tr > td:nth-child(1) > a > img")  # 继续购物按钮
    distribution_loc = ("name", "shipping")  # 配送方式的下拉框定位
    payment_loc = ("name", "payment")  # 支付方式的下拉框定位
    pack_loc = ("name", "pack")  # 商品包装的下拉框定位
    card_loc = ("name", "card")  # 贺卡的下拉框定位
    receipt_loc=("css selector","#ECS_NEEDINV")# 开发票点击
    receiptType_loc=("name","inv_type")# 发票类型下拉框的定位
    christmas_loc=("css selector","#cardTable > tbody > tr:nth-child(4) "
    "> td:nth-child(3) > textarea")# 祝福语框输入
    text_loc = ("css selector", "#postscript")  # 文本框定位
    oos_loc = ("name", "how_oos")  # 缺货处理
    refer_loc = ("css selector", "#theForm > div:nth-child(16) > div:nth-child(3) > "
                                "input[type=image]:nth-child(1)")  # 提交订单定位
    end_loc=("css selector","body > div:nth-child(7) > div > h6")# 订单号定位
    noLogin_loc=("css selector","#loginForm > table > tbody > tr:nth-child(5) "
        "> td > div > input.bnt_blue_2")# 不打算登录直接购买的定位
    def click_gohome(self):
        """
        点击返回首页
        :return:
        """
        self.click(self.gohome_loc)
    def click_photo(self):
        """
        点击相机
        :return:
        """
        self.click(self.photo_loc)
    def click_instantBuy(self):
        """
        点击立即购买
        :return:
        """
        self.click(self.instantBuy_loc)
    def click_settling(self):
        """
        点击去结算
        :return:
        """
        self.click(self.settling_loc)
    def click_distribution(self):
        """
        配送方式单选框
        :return:
        """
        self.drop_single(self.distribution_loc)
    def click_payment_loc(self):
        """
        支付方式单选框
        :return:
        """
        self.drop_single(self.payment_loc)
    def click_pack_loc(self):
        """
        商品包装单选框
        :return:
        """
        self.drop_single(self.pack_loc)
    def click_card(self):
        """
        贺卡单选框
        :return:
        """
        self.drop_single(self.card_loc)
    def input_christmas(self,text):
        """
        祝福语输入
        :param text: 
        :return: 
        """
        self.send_keys(self.christmas_loc,text)
    def click_receipt(self):
        """
        点击开发票
        :return: 
        """
        self.click(self.receipt_loc)
    def click_type(self):
        """
        点击类型选择下拉框
        :return:
        """
        self.drop_down(self.receiptType_loc)

    def input_text(self,text):
        """
        留言输入
        :param text:
        :return:
        """
        self.send_keys(self.text_loc,text)
    def oos(self):
        """
        缺货处理
        :return: 
        """
        self.click(self.oos_loc)
    
    def refer(self):
        """
        提交订单
        :return:
        """
        self.click(self.refer_loc)

    def is_sucess(self,text):
        """
        进行判断
        :param text:
        :return:
        """
        return self.is_text_inelement(self.end_loc,text)
    def no_Login(self):
        """
        点击不登录直接购买
        :return:
        """
        self.click(self.noLogin_loc)
    

if __name__ == '__main__':
    driver = open_browser("chrome")
    login = LogingPage(driver)
    login.open_url(login_url)
    login.input_username("lancer")
    login.input_password("123456")
    login.click_submit()
    print(login.is_sucess("lancer"))
    login=ShoppingPage(driver)
    login.click_gohome()
    login.click_photo()
    login.click_instantBuy()
    login.click_settling()
    login.click_distribution()
    login.click_payment_loc()
    login.click_pack_loc()
    login.click_card()
    login.click_receipt()
    login.click_type()
    login.input_text("wswsws")
    login.refer()
    login.close()