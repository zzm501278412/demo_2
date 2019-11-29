from common.base import Base,open_browser,login_url
class LogingPage(Base):
    username_loc=("name","username")#用户名输入框
    password_loc=("name","password")#密码框
    submit_loc = ("class name", "us_Submit")  # 立即登录按钮
    result_loc = ("class name", "f4_b")  # 登录成功后的结果
    def input_username(self,username):
        """
        输入用户名
        :param username:
        :return:
        """
        self.send_keys(self.username_loc,username)
    def input_password(self,password):
        """
        输入密码
        :param password: 
        :return: 
        """
        self.send_keys(self.password_loc,password)
    def click_submit(self):
        """
        点击登录
        :return:
        """
        self.click(self.submit_loc)
    def is_sucess(self,text):
        return self.is_text_inelement(self.result_loc,text)
if __name__ == '__main__':
    driver=open_browser("chrome")
    login=LogingPage(driver)
    login.open_url(login_url)
    login.input_username("lancer")
    login.input_password("123456")
    login.click_submit()
    print(login.is_sucess("lancer"))
    login.close()