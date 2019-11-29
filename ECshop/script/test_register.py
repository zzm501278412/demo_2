"""
test_login.py文件
    1.封装页面业务
    2.测试用例

"""
from page.register_page import RegisterPage
from common.base import open_browser,login_url
import unittest,ddt
from common.operartion_Excel import Operationxcel
import time
# 准备测试数据
oper = Operationxcel(r"../datas/register_data.xls")
test_data = oper.get_data_info()
print(test_data)

@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        # 用例前置条件
        driver = open_browser()
        self.driver=driver
        self.register= RegisterPage(driver)
        self.register.open_url(login_url)
        self.imgs = []

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())

    def tearDown(self) -> None:
        # 5.关闭浏览器
        self.add_img()
        self.register.close()

    @ddt.data(*test_data)
    def test_lregister(self,data):
        """登录测试用例:不记住密码"""
        """张无默,白文怡"""
        # 点击立即注册注册
        self.register.click_submit()
        #点击我已有账号我要登陆
        # self.register.click_login()
        # #点击忘记密码
        # self.register.click_rem_password()
        # 1.输入用户名
        self.register.input_username(data["username"])

        # 3.输入邮件
        self.register.input_email(data["email"])

        # 2.输入密码
        self.register.input_password(str(data["password"]))
        # 2.确认密码
        self.register.input_old_password(str(data["confirm_password"]))

        # 2.输入qq号
        self.register.input_qq(str(data["extend_field2"]))

        # 2.输入办公电话
        self.register.input_tel(str(data["extend_field3"]))
        # 2.输入家庭电话
        self.register.input_home_tel(str(data["extend_field4"]))
        # 2.输入手机
        self.register.input_Phone(str(data["extend_field5"]))

        #随机生产密码问题
        self.register.choose_question()

        #输入密码问题的答案
        self.register.input_password_answer(data["password_answer"])

        self.register.redio()
        #点击注册
        self.register.login_submit()

        try:
            self.register.alert_accept1()
        except:
            pass
        finally:
            result = self.register.is_successed(data['username'])
            self.assertEqual(result, data['exepct'])
            self.add_img()







if __name__ == '__main__':
    unittest.main()
