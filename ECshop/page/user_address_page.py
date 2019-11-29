import time

from common.base import Base,open_browser,login_url

class UserAddressPage(Base):
    consignee_loc = ("name","consignee")    # 收货人
    address_loc = ("name","address")    # 详细地址
    zipcode_loc = ("name","zipcode")    # 邮政编号
    mobile_loc = ("name","mobile")    # 邮政编号
    submit_loc = ("name","submit")    # 确认修改
    eceiving_addr_loc = ("link text", "收货地址")  # 收货地址

    def send_keys_consignee(self,index,text):
        '''
        收货人
        :param index: 索引
        :param text: 收货人姓名
        :return:
        '''
        consignees = self.find_elements(self.consignee_loc)
        consignee = consignees[index]
        consignee.clear()
        consignee.send_keys(text)
    def send_keys_address(self,index,text):
        '''
        详细地址
        :param index: 索引
        :param text: 详细地址内容
        :return:
        '''
        addresss = self.find_elements(self.address_loc)
        address = addresss[index]
        address.clear()
        address.send_keys(text)
    def send_keys_zipcode(self,index,text):
        '''
        邮政编号
        :param index: 索引
        :param text: 编号
        :return:
        '''
        zipcodes = self.find_elements(self.zipcode_loc)
        zipcode = zipcodes[index]
        zipcode.clear()
        zipcode.send_keys(text)
    def send_keys_mobile(self,index,text):
        '''
        手机
        :param index: 索引
        :param text: 输入的内容
        :return:
        '''
        mobiles = self.find_elements(self.mobile_loc)
        mobile = mobiles[index]
        mobile.clear()
        mobile.send_keys(text)
    def click_submit(self,index):
        '''
        确认修改
        :param index:索引
        :return:
        '''
        submits = self.find_elements(self.submit_loc)
        submits[index].click()
    def eceivingAddr(self):
        '''
        点击收货地址
        :return:
        '''
        self.click(self.eceiving_addr_loc)

if __name__ == '__main__':
    driver = open_browser()
    from page.longin_page import LonginPage
    login = LonginPage(driver)
    login.open_url(login_url)
    uasename = "张si"
    password = "123456"
    login.input_username(uasename)
    login.input_password(password)
    login.click_submit()
    time.sleep(6)
    addressPage = UserAddressPage(driver)
    addressPage.eceivingAddr()

    index = 1
    addressPage.send_keys_consignee(index,"uyguihi")
    addressPage.send_keys_address(index,"d5rfyygui")
    addressPage.click_submit(index)