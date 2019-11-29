from common.base import Base,open_browser

import time
class UserCenterPage(Base):
    '''封装表现层:制作定位器'''
    user_center_loc = ("link text","用户中心")    # 用户中心
    eceiving_addr_loc = ("link text","收货地址")    # 收货地址
    province_loc = ("xpath", "//form[last()]/table/tbody/tr[1]/td[2]/select[2]")   # 选择省份下拉框
    city_loc = ("xpath","//form[last()]/table/tbody/tr[1]/td[2]/select[3]")   # 选择市下拉框
    district_loc = ("xpath","//form[last()]/table/tbody/tr[1]/td[2]/select[4]")   # 选择区下拉框
    consignee_loc = ("xpath", "//form[last()]/table/tbody/tr[2]/td[2]/input")  # 收货人
    email_loc = ("xpath","//form[last()]/table/tbody/tr[2]/td[4]/input")   # 电子邮件地址
    address_loc = ("xpath","//form[last()]/table/tbody/tr[3]/td[2]/input")   # 详细地址
    zipcode_loc = ("xpath","//form[2]/table/tbody/tr[3]/td[4]/input")   # 邮政编号
    tel_loc = ("xpath","//form[last()]/table/tbody/tr[4]/td[2]/input")   # 电话
    mobile_loc = ("xpath","//form[2]/table/tbody/tr[4]/td[4]/input")   # 手机
    new_eceiving_addr = ("css selector","[value='新增收货地址']")   # 新增收货地址
    delect_loc = ("xpath","//form[2]/table/tbody/tr[5]/td[2]/input[2]")   # 删除
    amend_loc = ("xpath","//form[2]/table/tbody/tr[5]/td[2]/input")   # 修改

    '''元素操作层'''
    def consignee(self,text):
        '''
        收货人
        :return:
        '''
        self.send_keys(self.consignee_loc,text)
    def mobile(self,text):
        '''
        电话
        :return:
        '''
        self.send_keys(self.mobile_loc,text)
    def zipcode(self,text):
        '''
        邮政编号
        :return:
        '''
        self.send_keys(self.zipcode_loc,text)
    def email(self,text):
        '''
        电子邮件地址
        :return:
        '''
        self.send_keys(self.email_loc,text)
    def address(self,text):
        '''
        详细地址
        :return:
        '''
        self.send_keys(self.address_loc,text)
    def tel(self,text):
        '''
        手机
        :return:
        '''
        self.send_keys(self.tel_loc,text)
    def province(self):
        '''
        市
        :return:
        '''
        self.drop_down(self.province_loc)
    def city(self):
        '''
        省
        :return:
        '''
        self.drop_down(self.city_loc)
    def district(self):
        '''
        区
        :return:
        '''
        self.drop_down(self.district_loc)
    def eceivingAddr(self):
        '''
        点击收货地址
        :return:
        '''
        self.click(self.eceiving_addr_loc)
    def newEceivingAddr(self):
        '''
        新增收货地址
        :return:
        '''
        self.click(self.new_eceiving_addr)
    def accept_delect(self):
        '''确认删除'''
        self.click(self.delect_loc)
        alert = self.driver.switch_to.alert
        time.sleep(2)
        alert.accept()   # 点击确认按钮
    def dismiss_delect(self):
        '''取消删除'''
        self.click(self.delect_loc)
        alert = self.driver.switch_to.alert
        time.sleep(2)
        alert.dismiss()    # 点击确认按钮
    def amend(self):
        '''
        确认修改
        :return:
        '''
        self.click(self.amend_loc)

if __name__ == '__main__':
    # driver = open_browser()
    # from page.longin_page import LonginPage,url
    # login = LonginPage(driver)
    # login.open_url(url)
    # uasename = "张si"
    # password = "123456"
    # login.input_username(uasename)
    # login.input_password(password)
    # login.click_submit()
    # time.sleep(6)
    # # # 点击首页
    # # login.click_homepage()
    #
    # user = UserCenterPage(driver)
    # user.userCenter()   # 点击用户中心
    user.eceivingAddr()   # 收货地址

    # user.province()   # 选择市
    # time.sleep(2)
    # user.city()   # 选择省
    # time.sleep(2)
    # user.district()  # 选择区
    # time.sleep(2)
    # user.consignee("zhangsan")   # 输入收货人
    # user.address("地区haneh")   # 输入详细地址
    # user.tel(13524720252)   # 输入电话

    # user.zipcode("000000")    # 输入邮编
    # time.sleep(2)
    # user.mobile(13541202520)   # 输入手机号码
    # time.sleep(2)
    # user.amend()


    # user.delect()
    # time.sleep(2)


    # user.newEceivingAddr()   # 点击新增收货地址





