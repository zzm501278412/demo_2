
"""
1.login_page.py 需要继承Base类
2.封装表现层:页面上所有可见的元素
3.封装操作层:页面上可见元素的操作:点击\输入等
"""
from selenium import webdriver
from common.base import Base
from common.base import open_browser,url
import time



class ShoppingCarPage(Base): # 继承Base类
    """封装表现层--制作定位器"""

    login_loc=("link text","请登录")#请登录..
    homepage=("link text","首页")#首页..

    shopcar_loc = ("link text", "购物车(0)")  # 购物车连接
    continue_shop_loc=("css selector","a[href='./']")  #继续购买
    goods1_loc=("css selector","a[href='goods.php?id=72']")   #定位第一件商品
    im_buy=("css selector","a[href='javascript:addToCart(72)']")   #立即购买
    #购物车里修改商品数量
    update_goods1=("css selector","form> table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(5)>input")
    #删除商品
    delete_foods1=("css selector","form > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(7)>a")
    #够买商品时 输入数量 的输入框
    good_num_loc=("name","number")

    """封装操作层"""
    #点击登录
    def click_login(self):
        self.click(self.login_loc)

    #点击购物车
    def click_shopcar(self):
        self.click(self.shopcar_loc)
    #点击继续购物
    def click_continue_shop(self):
        self.click(self.continue_shop_loc)
    #点击第一件商品
    def click_goods1(self):
        self.click(self.goods1_loc)

    # 购买商品输入数量
    def input_num(self, text):
        """输入购买的数量"""
        self.send_keys(self.good_num_loc, text)

    #点击立即购买
    def click_im_buy(self):
        self.click(self.im_buy)
    #输入需要修改的数量
    def input_update_num(self,text):
        """输入需要修改的数量"""
        self.send_keys(self.update_goods1,text)

    # 确定修改("点击回车键")
    def keyboard_event(self):
        self.keyboard_envent_enter(self.update_goods1)
    # 点击删除商品
    def click_delete(self):
        self.click(self.delete_foods1)

    # 确定删除商品
    def real_delete(self):
        # 4.2 获取弹窗(进入弹窗)
        alert = self.driver.switch_to.alert
        # 4.3 操作弹窗
        # print("弹窗文本值:", alert.text)
        time.sleep(2)
        # 点击弹窗确定按钮,删除商品
        alert.accept()
        time.sleep(1)
    #返回首页
    def backhome(self):
        self.click(self.homepage)



    # #清空输入框
    # def clear_input(self):
    #     self.clear(self.good_num_loc)



    # def click_update_goods1(self):
    #     self.click(self.update_goods1)
if __name__ == '__main__':
    driver = open_browser()
    shop = ShoppingCarPage(driver)
    shop.open_url(url)
    #点击查看购物车
    shop.click_shopcar()
    time.sleep(1)
    # 点击继续购买
    shop.click_continue_shop()
    time.sleep(1)
    #点击第一件商品
    shop.click_goods1()
    time.sleep(1)
    #清空输入框
    # shop.clear_input()
    # time.sleep(2)

    #输入购买的数量
    num1=3
    shop.input_num(num1)
    time.sleep(3)
    #点击立即购买
    shop.click_im_buy()
    time.sleep(2)
    #修改商品数量
    num2="5"
    shop.input_update_num(num2)
    time.sleep(2)
    #确定修改
    shop.keyboard_event()
    time.sleep(4)
    #点击删除商品
    shop.click_delete()
    time.sleep(2)
    #确定删除商品
    shop.real_delete()
    time.sleep(1)
    #返回首页
    shop.backhome()

    # # print(login.is_successed(username))


# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('http://172.16.1.216/ecshop/')
# driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/a[2]').click()
#
# driver.find_element_by_xpath('/html/body/div[6]/div[1]/form/table[1]/tbody/tr[2]/td[5]/input').send_keys('2')


