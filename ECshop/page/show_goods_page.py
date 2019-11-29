"""
login_page.py
    1.对登录页面封装
    2.封装页面表现层和操作层
    3.继承base.py
"""
from common.base import Base, open_browser,login_url
import time





class ShowPage(Base):
    """
    封装表现层:制作定位器
    """
    username_loc = ("name", "username")  # 用户名输入框
    password_loc = ("name", "password")  # 密码输入框
    remember_loc = ("id", "remember")  # 记住密码
    submit_loc = ("class name", "us_Submit")  # 立即登录按钮
    home_page_loc = ("link text", "首页")  # 首页按钮
    locator = ('class name', 'goodsimg')  #商品定位
    locator1 = ('xpath', '//*[@id="pager"]/a') #页数定位
    locator2=("class name","next")  #下一页
    register_loc = ("css selector", "a[href='<a href='user.php?act=register']>img")
    result_loc = ("class name", "f4_b")  # 登录成功后的结果
    grabble_loc=("name","imageField")
    """封装操作层"""

    def input_username(self, username):
        """
        输入用户名
        :param self:
        :param username:
        :return:
        """
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        """
        输入密码
        :param self:
        :param password:
        :return:
        """
        self.send_keys(self.password_loc, password)

    def click_submit(self):
        """
        点击立即登录
        :param self:
        :return:
        """
        self.click(self.submit_loc)

    def is_successd(self, text):
        """
        判断是否登录成功
        :param text:
        :return:
        """
        return self.is_text_inelement(self.result_loc, text)

    def click_home_page(self):
        """
        点击首页
        :param self:
        :return:
        """
        self.click(self.home_page_loc)

    def click_grabble(self):
        """
        点击搜索按钮
        :param self:
        :return:
        """
        self.click(self.grabble_loc)

    def click_goods(self,):
        self.click_show_goods(self.locator, self.locator1, self.locator2)
if __name__ == '__main__':
    driver = open_browser()
    login = ShowPage(driver)
    login.open_url(login_url)
    time.sleep(2)
    username = "max"
    password = "123456"
    login.input_username(username)
    login.input_password(password)
    login.click_submit()
    login.click_home_page()
    login.click_grabble()
    login.click_show_goods(login.locator,login.locator1,login.locator2)

    login.close()
