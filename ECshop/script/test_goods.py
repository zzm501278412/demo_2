from page.add_goods_page import Add_goods
from common.base import open_browser,url,admin_url2
import unittest
from common.add_data_faker import Add_data_feker
from time import sleep


class Test_Add_goods(unittest.TestCase):
    def setUp(self) -> None:
        driver = open_browser()
        self.driver =driver
        self.Add_goods = Add_goods(driver)
        self.Add_goods.open_url(admin_url2)
        self.Add_goods.add_submit()# 首页弹窗
        self.Add_goods.click_ecshop() # 进入ECshop进入界面
        self.Add_goods.input_username('admin') # 账号定位
        self.Add_goods.input_password('admin888')# 密码定位
        self.Add_goods.submit()# 登陆界面确定按钮
        self.imgs = []#添加截图容器

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
    def tearDown(self) -> None:
        self.Add_goods.close()

    def test_add_goods_run_(self):
        """
        曾智明
        验证后端是否添加商品成功
        :return:
        """
        self.Add_goods.switch_ifarme_clik()# 进入ifarme定位
        self.Add_goods.click_add_goods() # 添加商品定位按钮
        self.Add_goods.click_add_goods2()#  添加商品定位按钮
        self.Add_goods.alert_back()
        self.Add_goods.switch_ifarme_clik2() # 进入第二层iframe
        sleep(4)
        b=str(Add_data_feker().random_goods_name())# 商品名输入框定位
        self.Add_goods.send_keys_add_goodsname(b)# 商品编号输入框定位
        self.Add_goods.send_keys_oods_number(str(Add_data_feker().random_goods_numberid()))# 字体选择下拉菜单定位
        self.Add_goods.goods_name_style(str(Add_data_feker().random_name_style())) # 商品分类下拉菜单
        self.Add_goods.cat_id(str(Add_data_feker().random_cat_id())) # 添加分类
        self.Add_goods.add_goods_button()# 添加分类输入框
        self.Add_goods.add_goods_send(str(Add_data_feker().random_goods_name()))# 添加分类确定按钮
        self.Add_goods.add_goods_send_click()# 扩展分类
        self.Add_goods.add_goodes_addother()# 拓展分类下拉菜单
        self.Add_goods.add_goods_mennu_addother('智能硬件')# 品牌下拉菜单
        self.Add_goods.goods_brand(str(Add_data_feker().random_brand())) # 添加品牌按钮
        self.Add_goods.add_goods_brand()# 添加品牌输入框
        self.Add_goods.goods_brand_send(str(Add_data_feker().random_goods_name()))# 添加品牌确定按钮
        self.Add_goods.add_goods_brand_click()# 供应商下拉菜单
        self.Add_goods.goods_supplier(str(Add_data_feker().random_suppliers_id()))# 商品价格输入框
        self.Add_goods.goods_shop_price(str(Add_data_feker().random_goods_prcie())) # 优惠数量输入框
        self.Add_goods.goods_volume_number(str(Add_data_feker().random_goods_prcie())) # 优惠价格输入框
        self.Add_goods.goods_volume_price(str(Add_data_feker().random_goods_prcie()))# 市场价格输入框
        self.Add_goods.goods_market('140.5') # 市场价格取整数点击按钮
        self.Add_goods.goods_market_price_int()# 虚拟销量输入框
        self.Add_goods.goods_virtual_sales(str(Add_data_feker().random_goods_prcie()))# 消费赠送积分输入框
        self.Add_goods.goods_give_integral('-0.8')# 赠送等级积分输入框
        self.Add_goods.goods_rank_integral('-0.8')# 积分购买输入框
        self.Add_goods.goods_integral('3') # 点击促销价
        self.Add_goods.goods_is_promote() # 促销价输入框
        self.Add_goods.goods_promote_1(str(Add_data_feker().random_goods_prcie())) # 促销价输入框
        self.Add_goods.goods_promote_start_date_js()#去掉JS
        self.Add_goods.goods_promote_end_date_js()#去掉js
        self.Add_goods.goods_promote_start_date(str(Add_data_feker().random_start_time())) # 输入促销价开始日期
        self.Add_goods.goods_promote_end_date(str(Add_data_feker().random_end_time()))# 输入促销价结束日期
        self.Add_goods.goods_goods_img(str(Add_data_feker().random_goods_img())) # 上传商品图片
        self.Add_goods.goods_goods_img_url(str(Add_data_feker().random_goods_img()))# 输入图片URL
        self.Add_goods.goods_auto_thumb() # 点击自动生成略缩图
        self.Add_goods.goods_goods_thumb(str(Add_data_feker().random_goods_img())) # 上传略缩图
        self.Add_goods.goods_goods_thumb_url(str(Add_data_feker().random_goods_img())) # 输入略缩图url
        self.Add_goods.goods_descripitopn_click()# 点击详细描述
        self.Add_goods.goods_descripitopn_frame() # 进入详细描述frame
        self.Add_goods.goods_descripitopn_frame2() # 进入详细描述frame
        self.Add_goods.goods_descripitopn_send(str(Add_data_feker().random_goods_name()))# 详细描述输入内容
        self.Add_goods.alert_back()#退出上一层frame
        self.Add_goods.alert_back()#退出上上测frame
        self.Add_goods.goods_mix_tab_click()# 点击其他信息
        self.Add_goods.goods_mix_tab_click_goods_weight(str(Add_data_feker().random_goods_prcie())) # 重量输入框
        self.Add_goods.goods_mix_tab_weight_unit('克')# 重量单位下拉框
        self.Add_goods.goods_mix_tab_weight_goods_number(str(Add_data_feker().random_goods_prcie()))# 库存输入框
        self.Add_goods.goods_mix_tab_weight_warn_number(str(Add_data_feker().random_goods_prcie())) # 库存警告输入框
        self.Add_goods.goods_mix_tab_weight_is_best()# 加入推荐点击框
        self.Add_goods.goods_mix_tab_is_on_sale()# 勾选允许销售
        self.Add_goods.goods_mix_tab_is_alone_sale()# 勾选普通商品销售
        self.Add_goods.goods_mix_tab_is_shipping()# 勾选免运费
        self.Add_goods.goods_mix_tab_is_keywords(str(Add_data_feker().random_goods_name()))# 商品关键字输入框
        self.Add_goods.goods_mix_tab_is_goods_brief(str(Add_data_feker().random_goods_name())) # 商品简单描述输入框
        self.Add_goods.goods_mix_tab_is_seller_note(str(Add_data_feker().random_goods_name()))# 商家备注
        self.Add_goods.goods_properties_tab_click()#点击商品属性
        self.Add_goods.goods_properties_tab_goods_type('笔记本电脑')#商品属性下拉菜单
        self.Add_goods.goods_properties_tab_attr_value_list(str(Add_data_feker().random_goods_name()))#笔记本型号
        self.Add_goods.goods_properties_tab_attr_value_list1(str(Add_data_feker().random_goods_name()))#笔记规格
        self.Add_goods.goods_properties_tab_attr_value_list2(str(Add_data_feker().random_goods_name()))#笔记尺寸
        self.Add_goods.goods_properties_tab_attr_value_list3(str(Add_data_feker().random_goods_name()))#处理器类型
        self.Add_goods.goods_properties_tab_attr_value_list4(str(Add_data_feker().random_goods_name()))#处理器主频
        self.Add_goods.goods_properties_tab_attr_value_list5(str(Add_data_feker().random_goods_name()))#二级缓存
        self.Add_goods.goods_properties_tab_attr_value_list6(str(Add_data_feker().random_goods_name()))#系统总线
        self.Add_goods.goods_properties_tab_attr_value_list7(str(Add_data_feker().random_goods_name()))#主板芯片组
        self.Add_goods.goods_properties_tab_attr_value_list8(str(Add_data_feker().random_goods_name()))#内存容量
        self.Add_goods.goods_properties_tab_attr_value_list9(str(Add_data_feker().random_goods_name()))#内存类型
        self.Add_goods.goods_properties_tab_attr_value_list10(str(Add_data_feker().random_goods_name()))#硬盘
        self.Add_goods.goods_properties_tab_attr_value_list11(str(Add_data_feker().random_goods_name()))#屏幕尺寸
        self.Add_goods.goods_properties_tab_attr_value_list12(str(Add_data_feker().random_goods_name()))#显示芯片
        self.Add_goods.goods_properties_tab_attr_value_list13(str(Add_data_feker().random_goods_name()))#标称频率
        self.Add_goods.goods_properties_tab_attr_value_list14(str(Add_data_feker().random_goods_name()))#显卡显存
        self.Add_goods.goods_properties_tab_attr_value_list15(str(Add_data_feker().random_goods_name()))#显卡类型
        self.Add_goods.goods_properties_tab_attr_value_list16(str(Add_data_feker().random_goods_name()))#光驱类型
        self.Add_goods.goods_properties_tab_attr_value_list17(str(Add_data_feker().random_goods_name()))#电池容量
        self.Add_goods.goods_properties_tab_attr_value_list18(str(Add_data_feker().random_goods_name()))#其他配置
        self.Add_goods.add_goods_sure()#点击确定添加
        self.add_img()#添加截图
        sleep(5)
        self.Add_goods.surch_goods(b)#搜索框搜索添加的商品内容
        self.Add_goods.surch_goods_click()#点击搜索
        a=self.Add_goods.surch_goods_result('没有找到任何记录')
        self.assertFalse(a)#断言是否添加成功

    def test_add_goods_run2(self):
        """
        验证前端是是否添加商品成功
        :return:
        """
        self.Add_goods.switch_ifarme_clik()  # 进入ifarme定位
        self.Add_goods.click_add_goods()  # 添加商品定位按钮
        self.Add_goods.click_add_goods2()  # 添加商品定位按钮
        self.Add_goods.alert_back()
        self.Add_goods.switch_ifarme_clik2()  # 进入第二层iframe
        sleep(4)
        b = str(Add_data_feker().random_goods_name())  # 商品名输入框定位
        self.Add_goods.send_keys_add_goodsname(b)  # 商品编号输入框定位
        self.Add_goods.send_keys_oods_number(str(Add_data_feker().random_goods_numberid()))  # 字体选择下拉菜单定位
        self.Add_goods.goods_name_style(str(Add_data_feker().random_name_style()))  # 商品分类下拉菜单
        self.Add_goods.cat_id(str(Add_data_feker().random_cat_id()))  # 添加分类
        self.Add_goods.add_goods_button()  # 添加分类输入框
        self.Add_goods.add_goods_send(str(Add_data_feker().random_goods_name()))  # 添加分类确定按钮
        self.Add_goods.add_goods_send_click()  # 扩展分类
        self.Add_goods.add_goodes_addother()  # 拓展分类下拉菜单
        self.Add_goods.add_goods_mennu_addother('智能硬件')  # 品牌下拉菜单
        self.Add_goods.goods_brand(str(Add_data_feker().random_brand()))  # 添加品牌按钮
        self.Add_goods.add_goods_brand()  # 添加品牌输入框
        self.Add_goods.goods_brand_send(str(Add_data_feker().random_goods_name()))  # 添加品牌确定按钮
        self.Add_goods.add_goods_brand_click()  # 供应商下拉菜单
        self.Add_goods.goods_supplier(str(Add_data_feker().random_suppliers_id()))  # 商品价格输入框
        self.Add_goods.goods_shop_price(str(Add_data_feker().random_goods_prcie()))  # 优惠数量输入框
        self.Add_goods.goods_volume_number(str(Add_data_feker().random_goods_prcie()))  # 优惠价格输入框
        self.Add_goods.goods_volume_price(str(Add_data_feker().random_goods_prcie()))  # 市场价格输入框
        self.Add_goods.goods_market('140.5')  # 市场价格取整数点击按钮
        self.Add_goods.goods_market_price_int()  # 虚拟销量输入框
        self.Add_goods.goods_virtual_sales(str(Add_data_feker().random_goods_prcie()))  # 消费赠送积分输入框
        self.Add_goods.goods_give_integral('-0.8')  # 赠送等级积分输入框
        self.Add_goods.goods_rank_integral('-0.8')  # 积分购买输入框
        self.Add_goods.goods_integral('3')  # 点击促销价
        self.Add_goods.goods_is_promote()  # 促销价输入框
        self.Add_goods.goods_promote_1(str(Add_data_feker().random_goods_prcie()))  # 促销价输入框
        self.Add_goods.goods_promote_start_date_js()  # 去掉JS
        self.Add_goods.goods_promote_end_date_js()  # 去掉js
        self.Add_goods.goods_promote_start_date(str(Add_data_feker().random_start_time()))  # 输入促销价开始日期
        self.Add_goods.goods_promote_end_date(str(Add_data_feker().random_end_time()))  # 输入促销价结束日期
        self.Add_goods.goods_goods_img(str(Add_data_feker().random_goods_img()))  # 上传商品图片
        self.Add_goods.goods_goods_img_url(str(Add_data_feker().random_goods_img()))  # 输入图片URL
        self.Add_goods.goods_auto_thumb()  # 点击自动生成略缩图
        self.Add_goods.goods_goods_thumb(str(Add_data_feker().random_goods_img()))  # 上传略缩图
        self.Add_goods.goods_goods_thumb_url(str(Add_data_feker().random_goods_img()))  # 输入略缩图url
        self.Add_goods.goods_descripitopn_click()  # 点击详细描述
        self.Add_goods.goods_descripitopn_frame()  # 进入详细描述frame
        self.Add_goods.goods_descripitopn_frame2()  # 进入详细描述frame
        self.Add_goods.goods_descripitopn_send(str(Add_data_feker().random_goods_name()))  # 详细描述输入内容
        self.Add_goods.alert_back()  # 退出上一层frame
        self.Add_goods.alert_back()  # 退出上上测frame
        self.Add_goods.goods_mix_tab_click()  # 点击其他信息
        self.Add_goods.goods_mix_tab_click_goods_weight(str(Add_data_feker().random_goods_prcie()))  # 重量输入框
        self.Add_goods.goods_mix_tab_weight_unit('克')  # 重量单位下拉框
        self.Add_goods.goods_mix_tab_weight_goods_number(str(Add_data_feker().random_goods_prcie()))  # 库存输入框
        self.Add_goods.goods_mix_tab_weight_warn_number(str(Add_data_feker().random_goods_prcie()))  # 库存警告输入框
        self.Add_goods.goods_mix_tab_weight_is_best()  # 加入推荐点击框
        self.Add_goods.goods_mix_tab_is_on_sale()  # 勾选允许销售
        self.Add_goods.goods_mix_tab_is_alone_sale()  # 勾选普通商品销售
        self.Add_goods.goods_mix_tab_is_shipping()  # 勾选免运费
        self.Add_goods.goods_mix_tab_is_keywords(str(Add_data_feker().random_goods_name()))  # 商品关键字输入框
        self.Add_goods.goods_mix_tab_is_goods_brief(str(Add_data_feker().random_goods_name()))  # 商品简单描述输入框
        self.Add_goods.goods_mix_tab_is_seller_note(str(Add_data_feker().random_goods_name()))  # 商家备注
        self.Add_goods.goods_properties_tab_click()  # 点击商品属性
        self.Add_goods.goods_properties_tab_goods_type('笔记本电脑')  # 商品属性下拉菜单
        self.Add_goods.goods_properties_tab_attr_value_list(str(Add_data_feker().random_goods_name()))  # 笔记本型号
        self.Add_goods.goods_properties_tab_attr_value_list1(str(Add_data_feker().random_goods_name()))  # 笔记规格
        self.Add_goods.goods_properties_tab_attr_value_list2(str(Add_data_feker().random_goods_name()))  # 笔记尺寸
        self.Add_goods.goods_properties_tab_attr_value_list3(str(Add_data_feker().random_goods_name()))  # 处理器类型
        self.Add_goods.goods_properties_tab_attr_value_list4(str(Add_data_feker().random_goods_name()))  # 处理器主频
        self.Add_goods.goods_properties_tab_attr_value_list5(str(Add_data_feker().random_goods_name()))  # 二级缓存
        self.Add_goods.goods_properties_tab_attr_value_list6(str(Add_data_feker().random_goods_name()))  # 系统总线
        self.Add_goods.goods_properties_tab_attr_value_list7(str(Add_data_feker().random_goods_name()))  # 主板芯片组
        self.Add_goods.goods_properties_tab_attr_value_list8(str(Add_data_feker().random_goods_name()))  # 内存容量
        self.Add_goods.goods_properties_tab_attr_value_list9(str(Add_data_feker().random_goods_name()))  # 内存类型
        self.Add_goods.goods_properties_tab_attr_value_list10(str(Add_data_feker().random_goods_name()))  # 硬盘
        self.Add_goods.goods_properties_tab_attr_value_list11(str(Add_data_feker().random_goods_name()))  # 屏幕尺寸
        self.Add_goods.goods_properties_tab_attr_value_list12(str(Add_data_feker().random_goods_name()))  # 显示芯片
        self.Add_goods.goods_properties_tab_attr_value_list13(str(Add_data_feker().random_goods_name()))  # 标称频率
        self.Add_goods.goods_properties_tab_attr_value_list14(str(Add_data_feker().random_goods_name()))  # 显卡显存
        self.Add_goods.goods_properties_tab_attr_value_list15(str(Add_data_feker().random_goods_name()))  # 显卡类型
        self.Add_goods.goods_properties_tab_attr_value_list16(str(Add_data_feker().random_goods_name()))  # 光驱类型
        self.Add_goods.goods_properties_tab_attr_value_list17(str(Add_data_feker().random_goods_name()))  # 电池容量
        self.Add_goods.goods_properties_tab_attr_value_list18(str(Add_data_feker().random_goods_name()))  # 其他配置
        self.Add_goods.add_goods_sure()  # 点击确定添加
        self.add_img()  # 添加截图
        sleep(5)
        self.Add_goods.close()
        driver = open_browser()
        #返回首页搜索商品,进行断言
        self.Add_goods = Add_goods(driver)
        self.Add_goods.open_url(url)
        self.Add_goods.goods_centent_surch(b)
        self.Add_goods.goods_centent_surch_click()
        a=self.Add_goods.goods_centent_surch_is_sussecc('无法搜索到您要找的商品！')
        self.assertFalse(a)



if __name__ == '__main__':
    unittest.main()

