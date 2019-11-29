from common.base import Base
class AdderPage(Base):
    province_loc = ("name", "province")  # 省份下拉框选择
    city_loc = ("name", "city")  # 城市下拉框选择
    district_loc = ("name", "district")  # 区域下拉框选择
    name_loc = ("css selector", "#consignee_0")  # 收获人名字定位
    email_loc=("css selector","#email_0")# 电子邮件定位
    adder_loc=("css selector","#address_0")# 收获定制定位
    tell_loc=("css selector","#tel_0")
    adderClick_loc=("css selector","#theForm > div > table > tbody > tr:nth-child(5) > td > input.bnt_blue_2")
    def province(self):
        """
        省份下拉框选择
        :return:
        """
        self.drop_down(self.province_loc)
    def city(self):
        """
        城市下拉框选择
        :return:
        """
        self.drop_down(self.city_loc)
    def district(self):
        """
        区域下拉框选择
        :return:
        """
        self.drop_down(self.district_loc)
    def name(self,text):
        """
        收货人姓名填写
        :param text:
        :return:
        """
        self.send_keys(self.name_loc,text)
    def email(self,text):
        """
        收货人邮箱
        :param text:
        :return:
        """
        self.send_keys(self.email_loc,text)
    def adder(self,text):
        """
        收货人地址
        :param text:
        :return:
        """
        self.send_keys(self.adder_loc,text)
    def tell(self,text):
        """
        电话
        :param text:
        :return:
        """
        self.send_keys(self.tell_loc,text)
    def click_tell(self):
        """
        点击配送至这个地址
        :return: 
        """
        self.click(self.adderClick_loc)