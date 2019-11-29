from common.base import Base,open_browser,login_url

class LonginPage(Base):
    '''封装表现层:制作定位器'''
    username_loc = ("name","username")  # 用户名输入框
    password_loc = ("name","password")  # 密码输入框
    remember_loc = ("id","remember")   # 记住密码
    submit_loc = ("name","submit")   # 登录
    password = ("link text","密码问题")   # 密码问题连接
    email_loc = ("link text","邮件")  # 邮件连接
    massage_loc =("link text","短信验证")  # 短信验证连接
    homepage_loc = ("link text","首页")   # 首页连接
    register_loc = ("css selector","a[href='user.php?act=register']>img")   # 立即注册
    result_loc = ("class name","f4_b")   # 登录成功后的结果
    '''封装操作层'''
    def input_username(self,username):
        '''
        输入账号
        :param text:
        :return:
        '''
        self.send_keys(self.username_loc,username)
    def input_password(self,password):
        '''
        输入密码
        :param password:
        :return:
        '''
        self.send_keys(self.password_loc,password)

    def click_remember(self):
        '''
        记住密码
        :return:
        '''
        self.click(self.remember_loc)
    def click_submit(self):
        '''
        点击登录
        :return:
        '''
        self.click(self.submit_loc)

    def click_password(self):
        '''
        问题密码
        :return:
        '''
        self.click(self.password)
    def click_email(self):
        '''
        邮件
        :return:
        '''
        self.click(self.email_loc)

    def click_massage(self):
        '''
        短信验证
        :return:
        '''
        self.click(self.massage_loc)

    def click_homepage(self):
        '''
        首页
        :return:
        '''
        self.click(self.homepage_loc)

    def click_register(self):
        '''
        首页
        :return:
        '''
        self.click(self.register_loc)
    def is_successd(self,text):
        '''
        判断是否登录成功
        :param text:
        :return:
        '''
        return self.is_text_inelement(self.result_loc,text)

if __name__ == '__main__':
    driver = open_browser()
    longin = LonginPage(driver)
    longin.open_url(login_url)

    # 输入用户名和密码   点击登录
    uasename = "张si"
    password = "123456"
    longin.input_username(uasename)
    longin.input_password(password)
    longin.click_submit()
    import time

    # 点击找回密码:密码问题
    # longin.click_password()
    # 点击找回密码:邮件
    # longin.click_email()
    # 点击首页
    # longin.click_homepage()
    time.sleep(5)
    longin.close()