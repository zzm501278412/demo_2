"""
1.login_page.py 需要继承Base类
2.封装表现层:页面上所有可见的元素

3.封装操作层:页面上可见元素的操作:点击\输入等

"""

from common.base import Base
from common.base import open_browser,login_url
import time



class LoginPage(Base): # 继承Base类
    """封装表现层--制作定位器"""
    username_loc = ("name","username")# 用户名输入框
    password_loc = ("name","password")# 密码输入框
    remember_loc = ("id","remember")# 记住密码
    submit_loc = ("class name","us_Submit")# 立即登录按钮
    question_loc = ("link text","密码问题")# 找回密码--密码问题
    email_loc = ("link text","邮件")# 找回密码--邮件
    message_loc = ("link text","短信验证")# 找回密码--短信验证

    register_loc = ("css selector","a[href='user.php?act=register']")# 立即注册按钮
    result_loc = ("class name", "f4_b")  # 登录成功后的结果

    homepage_loc = ("link text", "首页")  # 进入首页链接



    """封装操作层"""
    def input_username(self,text):
        """输入用户名"""
        self.send_keys(self.username_loc,text)

    def input_password(self,text):
        """输入密码"""
        self.send_keys(self.password_loc,text)

    def remember_password(self):
        """点击记住密码"""
        self.click(self.remember_loc)

    def submit(self):
        """点击登录"""
        self.click(self.submit_loc)

    def click_homepage(self):
        """点击首页链接"""
        self.click(self.homepage_loc)

    def is_successed(self,text):
        """
        判断是否登录成功
        :param text:
        :return:
        """
        return self.is_text_inelement(self.result_loc,text)



if __name__ == '__main__':
    driver = open_browser()
    login = LoginPage(driver)
    username = "qwer"
    password = "123456"
    login.open_url(login_url)
    login.input_username(username)
    time.sleep(1)
    login.input_password(password)
    time.sleep(1)
    login.submit()
    time.sleep(6)
    login.click_homepage()
    time.sleep(10)
    login.close()

    # print(login.is_successed(username))
