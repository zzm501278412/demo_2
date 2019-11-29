"""
login_page
    对登陆页面封装
    封装页面表现层
    继承base.py
"""

from common.base import Base, open_browser,login_url


class Login_page(Base):
    """封装表现层,制作定位器"""
    username_loc = ('xpath', '/html/body/div[6]/div[1]/form/table/tbody/tr[1]/td[2]/input')  # 用户名输入框
    password_loc = ('xpath', '/html/body/div[6]/div[1]/form/table/tbody/tr[2]/td[2]/input')  # 密码输入框
    remember_loc = ('id', 'remember')  # 记住密码
    submit_loc = ('xpath', '/html/body/div[6]/div[1]/form/table/tbody/tr[4]/td[2]/input[3]')  # 立即登陆按钮
    question_loc = ('link text', "密码问题")  # 密码问题链接
    email_loc = ('link text', "邮件")  # 邮件链接
    message_loc = ('link text', "短信验证")  # 短信验证链接
    homepage_loc = ('link text', '首页')  # 首页链接
    register = ('css selector', 'body > div.usBox.clearfix > div.usTxt > a > img')  # 注册按钮
    result_loc = ('class name', 'f4_b')  # 登陆成功后的结果

 
    # 封装操作层
    def input_username(self, username):
        """
        输入用户名
        :param username:
        :return:
        """
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        self.send_keys(self.password_loc, password)

    def click_submit(self):
        self.click((self.submit_loc))

    def click_question(self):
        self.click(self.question_loc)

    def click_email(self):
        self.click(self.email_loc)

    def click_message(self):
        self.click(self.message_loc)

    def click_homepage(self):
        self.click(self.homepage_loc)

    def click_register(self):
        self.click(self.register)

    def is_successed(self,text):
        a=self.is_text_inelement(self.result_loc,text)
        return a
        

if __name__ == '__main__':
    import time
    driver = open_browser()
    login = Login_page(driver)
    driver.get('http://172.16.1.244/ecshop/user.php')
    username= 'zzm6226'
    password= 'zzm6226'
    login.input_username(username)
    login.input_password(password)

    login.click_submit()
    time.sleep(5)

    print(login.is_successed("zzm6226"))
