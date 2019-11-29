"""
login_page.py
    1.对登录页面封装
    2.封装页面表现层和操作层
    3.继承base.py中的Base类
"""
from common.base import Base, open_browser,login_url
import time




class RegisterPage(Base):
    """封装表现层:制作定位器"""
    username_loc = ("name", "username")  # 用户名输入框
    password_loc = ("name", "password")  # 密码输入框

    email_loc = ("name", "email")  # 邮箱输入框
    old_password_loc = ("name", "confirm_password")  # 确认密码输入框
    Phone_loc = ("name", "extend_field5")  # 手机
    redio_loc = ("name", "agreement")  # 用户协议
    login_submit_loc = ("name", "Submit")  # 资料输入后的注册
    homepage_loc = ("link text", "首页")  # 首页链接
    register_loc = ("css selector", "a[href='user.php?act=register']>img")  # 注册按钮
    qq_loc = ("name", "extend_field2")  # qq输入框
    tel_loc = ("name", "extend_field3")  # 办公室电话
    home_tel_loc = ("name", "extend_field4")  # 家庭电话
    password_question_loc = ("xpath", "/html/body/div[6]/div/form/table/tbody/tr[10]/td[2]/select")  # 密码问题
    password_answer_loc = ("xpath", "/html/body/div[6]/div/form/table/tbody/tr[11]/td[2]/input")  # 问题答案
    login_loc = ("xpath", "/html/body/div[6]/div/form/table/tbody/tr[17]/td[2]/a[1]")  # 我已有账号，我要登录的链接
    rem_password_loc = ("xpath", "/html/body/div[6]/div/form/table/tbody/tr[17]/td[2]/a[2]")  # 您忘记密码了吗？链接
    result_loc = ('class name', 'f4_b')

    """封装操作层"""

    def input_username(self, username):
        """
        输入用户名
        :param :
        :return:
        """
        self.send_keys(self.username_loc, username)

    def input_email(self, email):
        """
        输入邮箱
        :param :
        :return:
        """
        self.send_keys(self.email_loc, email)

    def input_password(self, password):
        """
        输入再次验证密码
        :param :
        :return:
        """
        self.send_keys(self.password_loc, password)

    def redio(self):
        """
        判断单选框
        :param :
        :return:
        """
        self.redio_is_selectde( self.redio_loc)

    def input_old_password(self, password):
        """
        输入再次验证密码
        :param :
        :return:
        """
        self.send_keys(self.old_password_loc, password)

    def input_Phone(self, Phone):
        """
        输入手机号
        :param :
        :return:
        """
        self.send_keys(self.Phone_loc, Phone)

    def click_submit(self):
        """
        点击立即注册
        :return:
        """
        self.click(self.register_loc)

    def login_submit(self):
        """
        点击输入资料以后的注册
        :return:
        """
        self.click(self.login_submit_loc)

    def click_login(self):
        """
        我已有账号,我要登录的链接
        :param :
        :return:
        """
        self.click(self.login_loc)
        time.sleep(1)
        self.click(self.register_loc)
        time.sleep(1)

    def click_rem_password(self):
        """
        点击忘记密码登录
        :param :
        :return:
        """
        self.click(self.rem_password_loc)
        time.sleep(1)
        self.back()
        time.sleep(1)
    def input_tel(self, tel):
        """
        输入办公电话
        :param :
        :return:
        """
        self.send_keys(self.tel_loc, tel)

    def input_home_tel(self, home_tel):
        """
        输入家庭电话
        :param :
        :return:
        """
        self.send_keys(self.home_tel_loc, home_tel)

    def input_qq(self, qq):
        """
        输入qq号
        :param :
        :return:
        """
        self.send_keys(self.qq_loc, qq)

    def choose_question(self):
        """
        随机筛选问题
        :return:
        """
        self.choose(self.password_question_loc)

    def input_password_answer(self, password_answer):
        """
        输入问题答案
        :return:
        """
        self.send_keys(self.password_answer_loc, password_answer)


    def alert_text(self):
       return self.alert()
    def alert_accept1(self):
        self.alert_accept()

    def is_successed(self, text):
        a = self.is_text_inelement(self.result_loc, text)
        return a

if __name__ == '__main__':
    driver = open_browser()
    register = RegisterPage(driver)
    register.open_url(login_url)
    register.click_submit()
    register.click_login()
    register.click_rem_password()
