from common.base import Base, open_browser, admin_url2


class Add_goods(Base):
    add_submit_loc = ('xpath', '//*[@id="panelCloud"]/div[1]/span')  # 首页弹窗
    click_ecshop_loc = ('id', 'cloudLogin')  # 进入ECshop进入界面
    username_loc = ('name', 'username')  # 账号定位
    password_loc = ('name', 'password')  # 密码定位
    submit_loc = ('class name', 'btn-a')  # 登陆界面确定按钮
    iframe_loc = ('menu-frame')  # 进入ifarme定位
    add_goods_loc = ('xpath', '/html/body/div/div[3]/div[1]/ul/li[2]')  # 添加商品定位按钮
    add_goods2_loc = ('xpath', '//*[@id="sub-menu-02_goods_add"]/a')
    iframe_loc2 = ('main-frame')  # 进入第二层iframe
    goods_name_loc = ('name', 'goods_name')  # 商品名输入框定位
    goods_number_loc = ('name', 'goods_sn')  # 商品编号输入框定位
    goods_name_style_loc = ('name', 'goods_name_style')  # 字体选择下拉菜单定位
    cat_id_loc = ('name', 'cat_id')  # 商品分类下拉菜单
    add_goods_button_loc = ('xpath', '//*[@id="general-table"]/tbody/tr[3]/td[2]/button')  # 添加分类
    add_goods_send_loc = ('name', 'addedCategoryName')  # 添加分类输入框
    add_goods_send_click_loc = ('xpath', '//*[@id="category_add"]/button[1]')  # 添加分类确定按钮
    add_goodes_addother_loc = ('xpath', '//*[@id="general-table"]/tbody/tr[4]/td[2]/input')  # 扩展分类
    add_goods_mennu_addother_loc = ('xpath', '//*[@id="general-table"]/tbody/tr[4]/td[2]/select')  # 拓展分类下拉菜单
    goods_brand_loc = ('name', 'brand_id')  # 品牌下拉菜单
    add_goods_brand_loc = ('xpath', '//*[@id="general-table"]/tbody/tr[5]/td[2]/button')  # 添加品牌按钮
    goods_brand_send_loc = ('name', 'addedBrandName')  # 添加品牌输入框
    add_goods_brand_click_loc = ('xpath', '//*[@id="brand_add"]/button[1]')  # 添加品牌确定按钮
    goods_supplier_loc = ('name', 'suppliers_id')  # 供应商下拉菜单
    goods_shop_price_loc = ('name', 'shop_price')  # 商品价格输入框
    goods_volume_number_loc = ('name', 'volume_number[]')  # 优惠数量输入框
    goods_volume_price_loc = ('name', 'volume_price[]')  # 优惠价格输入框
    goods_market_price_loc = ('name', 'market_price')  # 市场价格输入框
    goods_market_price_int_loc = ('xpath', '//*[@id="general-table"]/tbody/tr[10]/td[2]/input[2]')  # 市场价格取整数点击按钮
    goods_virtual_sales_loc = ('name', 'virtual_sales')  # 虚拟销量输入框
    goods_give_integral_loc = ('name', 'give_integral')  # 消费赠送积分输入框
    goods_rank_integral_loc = ('name', 'rank_integral')  # 赠送等级积分输入框
    goods_integral_loc = ('name', 'integral')  # 积分购买输入框
    goods_is_promote_loc = ('xpath', '//*[@id="general-table"]/tbody/tr[15]/td[1]/label')  # 点击促销价
    goods_promote_1_loc = ('name', 'promote_price')  # 促销价输入框
    goods_promote_start_date_loc = ('name', 'promote_start_date')  # 输入促销价开始日期
    goods_promote_start_date_js_loc = "document.getElementById('promote_start_date').removeAttribute('readonly')"
    goods_promote_end_date_loc = ('name', 'promote_end_date')  # 输入促销价结束日期
    goods_promote_end_date_js_loc = "document.getElementById('promote_end_date').removeAttribute('readonly')"
    goods_goods_img_loc = ('name', 'goods_img')  # 上传商品图片
    goods_goods_img_url_loc = ('name', 'goods_img_url')  # 输入图片URL
    goods_auto_thumb_loc = ('xpath', '//*[@id="auto_thumb_3"]/label')  # 点击自动生成略缩图
    goods_goods_thumb_loc = ('name', 'goods_thumb')  # 上传略缩图
    goods_goods_thumb_url_loc = ('name', 'goods_thumb_url')  # 输入略缩图url
    add_goods_sure_loc = ('xpath', '//*[@id="tabbody-div"]/form/div/input[2]')  # 点击确定按钮
    add_goods_reset_loc = ('xpath', '//*[@id="tabbody-div"]/form/div/input[3]')  # 点击重置键
    surch_goods_loc = ('name', 'keyword')  # 搜索框
    surch_goods_click_loc = ('xpath', '/html/body/div[3]/form/button')  # 点击搜索
    surch_goods_result_loc = ('xpath', '//*[@id="listDiv"]/table[1]/tbody/tr[3]/td')  # 搜索结果

    goods_descripitopn_click_loc = ('id', 'detail-tab')  # 点击详细描述
    goods_descripitopn_frame_loc = ('goods_desc___Frame')  # 进入详细描述frame
    goods_descripitopn_frame2_loc = ('xpath', '//*[@id="xEditingArea"]/iframe')  # 进入详细描述frame
    goods_descripitopn_send_loc = ('xpath', '/html/body')  # 详细描述输入内容

    goods_mix_tab_click_loc = ("id", 'mix-tab')  # 点击其他信息
    goods_mix_tab_click_goods_weight_loc = ('name', 'goods_weight')  # 重量输入框
    goods_mix_tab_weight_unit_loc = ('name', 'weight_unit')  # 重量单位下拉框
    goods_mix_tab_weight_goods_number_loc = ('name', 'goods_number')  # 库存输入框
    goods_mix_tab_weight_warn_number_loc = ('name', 'warn_number')  # 库存警告输入框
    goods_mix_tab_weight_is_best_loc = ('xpath', '//*[@id="mix-table"]/tbody/tr[4]/td[2]/input')  # 加入推荐点击框
    goods_mix_tab_is_on_sale_loc = ('name', 'is_on_sale')  # 勾选允许销售
    goods_mix_tab_is_alone_sale_loc = ('name', 'is_alone_sale')  # 勾选普通商品销售
    goods_mix_tab_is_shipping_loc = ('name', 'is_shipping')  # 勾选免运费
    goods_mix_tab_is_keywords_loc = ('name', 'keywords')  # 商品关键字输入框
    goods_mix_tab_is_goods_brief_loc = ('name', 'goods_brief')  # 商品简单描述输入框
    goods_mix_tab_is_seller_note_loc = ('name', 'seller_note')  # 商家备注

    goods_properties_tab_click_loc = ('id', 'properties-tab')  # 点击商品属性
    goods_properties_tab_goods_type_loc = ('name', 'goods_type')  # 商品属性下拉菜单
    goods_properties_tab_attr_value_list_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[1]/td[2]/input[2]')  # 笔记本型号
    goods_properties_tab_attr_value_list1_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[2]/td[2]/input[2]')  # 笔记规格
    goods_properties_tab_attr_value_list2_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[3]/td[2]/input[2]')  # 笔记尺寸
    goods_properties_tab_attr_value_list3_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[4]/td[2]/input[2]')  # 处理器类型
    goods_properties_tab_attr_value_list4_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[5]/td[2]/input[2]')  # 处理器主频
    goods_properties_tab_attr_value_list5_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[6]/td[2]/input[2]')  # 二级缓存
    goods_properties_tab_attr_value_list6_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[7]/td[2]/input[2]')  # 系统总线
    goods_properties_tab_attr_value_list7_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[8]/td[2]/input[2]')  # 主板芯片组
    goods_properties_tab_attr_value_list8_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[9]/td[2]/input[2]')  # 内存容量
    goods_properties_tab_attr_value_list9_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[10]/td[2]/input[2]')  # 内存类型
    goods_properties_tab_attr_value_list10_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[11]/td[2]/input[2]')  # 硬盘
    goods_properties_tab_attr_value_list11_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[12]/td[2]/input[2]')  # 屏幕尺寸
    goods_properties_tab_attr_value_list12_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[13]/td[2]/input[2]')  # 显示芯片
    goods_properties_tab_attr_value_list13_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[14]/td[2]/input[2]')  # 标称频率
    goods_properties_tab_attr_value_list14_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[15]/td[2]/input[2]')  # 显卡显存
    goods_properties_tab_attr_value_list15_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[16]/td[2]/input[2]')  # 显卡类型
    goods_properties_tab_attr_value_list16_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[17]/td[2]/input[2]')  # 光驱类型
    goods_properties_tab_attr_value_list17_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[18]/td[2]/input[2]')  # 电池容量
    goods_properties_tab_attr_value_list18_loc = ('xpath', '//*[@id="attrTable"]/tbody/tr[19]/td[2]/input[2]')  # 其他配置

    goods_centent_surch_loc = ('name', 'keywords')  # 首页搜索框
    goods_centent_surch_click_loc = ('name', 'imageField')  # 首页点击搜索框
    goods_centent_surch_is_sussecc_loc = ('xpath', '/html/body/div[6]/div/div[1]/div/div')  # 定位搜索结果

    def add_submit(self):
        """
        点击进入界面取消按钮
        :return:
        """
        self.click(self.add_submit_loc)

    def click_ecshop(self):
        # 点击进入账号密码输入框
        self.click(self.click_ecshop_loc)

    def input_username(self, username):
        # 输入账号
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        # 输入密码
        self.send_keys(self.password_loc, password)

    def submit(self):
        # 点击确定
        self.click(self.submit_loc)

    def switch_ifarme_clik(self):
        # 进入iframe
        self.switch_iframe(self.iframe_loc)

    def click_add_goods(self):
        # 进入添加商品管理
        self.click(self.add_goods_loc)
        # 点击添加商品

    def click_add_goods2(self):
        self.click(self.add_goods2_loc)
        # 进入第二层farme

    def switch_ifarme_clik2(self):
        self.switch_iframe(self.iframe_loc2)

    def send_keys_add_goodsname(self, text):
        # 输入商品名
        self.send_keys(self.goods_name_loc, text)

    def send_keys_oods_number(self, text=None):
        # 输入商品编号
        self.send_keys(self.goods_number_loc, text)

    def goods_name_style(self, text):
        # 选择字体样式,text填写字体样式
        self.select(self.goods_name_style_loc, text)
        # 商品分类下拉菜单

    def cat_id(self, text):
        self.select(self.cat_id_loc, text)

        # 点击商品添加商品分类按钮

    def add_goods_button(self):
        self.click(self.add_goods_button_loc)

    def add_goods_send(self, text):
        # 添加商品分类输入框输入内容
        self.send_keys(self.add_goods_send_loc, text)

    def add_goods_send_click(self):
        # 点击添加商品分类确定按钮
        self.click(self.add_goods_send_click_loc)

    def add_goodes_addother(self):
        # 点击拓展分类
        self.click(self.add_goodes_addother_loc)

    def add_goods_mennu_addother(self, text):
        # 添加拓展分类下拉菜单
        self.select(self.add_goods_mennu_addother_loc, text)

    def goods_brand(self, text):
        # 商品牌下拉菜单
        self.select(self.goods_brand_loc, text)

    def add_goods_brand(self):
        # 点击添加品牌
        self.click(self.add_goods_brand_loc)

    def goods_brand_send(self, text):
        # 添加品牌输入框输入内容
        self.send_keys(self.goods_brand_send_loc, text)

    def add_goods_brand_click(self):
        # 店家添加品牌确定按钮
        self.click(self.add_goods_brand_click_loc)

    def goods_supplier(self, text):
        # 供应商下拉菜单
        self.select(self.goods_supplier_loc, text)

    def goods_shop_price(self, text):
        # 本店售价输入框
        self.send_keys(self.goods_shop_price_loc, text)

    def goods_volume_number(self, text):
        # 优惠数量输入
        self.send_keys(self.goods_volume_number_loc, text)

    def goods_volume_price(self, text):
        # 优惠价格输入
        self.send_keys(self.goods_volume_price_loc, text)

    def goods_market(self, text):
        # 市场价格输入
        self.send_keys(self.goods_market_price_loc, text)

    def goods_market_price_int(self):
        # 点击取整数按钮
        self.click(self.goods_market_price_int_loc)

    def goods_virtual_sales(self, text):
        # 虚拟销量输入
        self.send_keys(self.goods_virtual_sales_loc, text)

    def goods_give_integral(self, text):
        # 赠送消费积分输入
        self.send_keys(self.goods_give_integral_loc, text)

    def goods_rank_integral(self, text):
        # 赠送等级消费积分输入
        self.send_keys(self.goods_rank_integral_loc, text)

    def goods_integral(self, text):
        # 积分购买输入框
        self.send_keys(self.goods_integral_loc, text)

    def goods_is_promote(self):
        # 点击促销价
        self.click(self.goods_is_promote_loc)

    def goods_promote_1(self, text):
        # 促销价输入
        self.send_keys(self.goods_promote_1_loc, text)

    def goods_promote_start_date_js(self):
        # 去掉开始日期JS
        self.js(self.goods_promote_start_date_js_loc)

    def goods_promote_start_date(self, text):
        # 输入促销价开始日期
        self.send_keys(self.goods_promote_start_date_loc, text)

    def goods_promote_end_date_js(self):
        # 去掉结束日期js
        self.js(self.goods_promote_end_date_js_loc)

    def goods_promote_end_date(self, text):
        # 输入促销价结束日期
        self.send_keys(self.goods_promote_end_date_loc, text)

    def goods_goods_img(self, text):
        # 上传商品图片
        self.send_keys(self.goods_goods_img_loc, text)

    def goods_goods_img_url(self, text):
        # 输入商品图片URL
        self.send_keys(self.goods_goods_img_url_loc, text)

    def goods_auto_thumb(self):
        # 点击自动生成略缩图
        self.click(self.goods_auto_thumb_loc)

    def goods_goods_thumb(self, text):
        # 上传略缩图
        self.send_keys(self.goods_goods_thumb_loc, text)

    def goods_goods_thumb_url(self, text):
        # 输入略缩图url
        self.send_keys(self.goods_goods_thumb_url_loc, text)

    def add_goods_sure(self):
        # 点击确定
        self.click(self.add_goods_sure_loc)

    def add_goods_reset(self):
        # 点击重置按键
        self.click(self.add_goods_reset_loc)

    def surch_goods(self, text):
        # 搜索框输入内容
        self.send_keys(self.surch_goods_loc, text)

    def surch_goods_click(self):
        # 点击搜索
        self.click(self.surch_goods_click_loc)

    def surch_goods_result(self, text):
        # 比对搜索结果
        a = self.is_text_inelement(self.surch_goods_result_loc, text)
        return a

    def goods_descripitopn_click(self):
        # 点击详细描述
        self.click(self.goods_descripitopn_click_loc)

    def goods_descripitopn_frame(self):
        # 进入详细描述frame
        self.switch_iframe(self.goods_descripitopn_frame_loc)

    def goods_descripitopn_frame2(self):
        frame = self.find_element(self.goods_descripitopn_frame2_loc)
        self.switch_iframe(frame)

    def goods_descripitopn_send(self, text):
        # 详细描述输入内容
        self.send_keys(self.goods_descripitopn_send_loc, text)

    def goods_mix_tab_click(self):
        # 点击其他信息
        self.click(self.goods_mix_tab_click_loc)

    def goods_mix_tab_click_goods_weight(self, text):
        # 重量输入框输入内容
        self.send_keys(self.goods_mix_tab_click_goods_weight_loc, text)

    def goods_mix_tab_weight_unit(self, text):
        # 重量单位下拉菜单
        self.select(self.goods_mix_tab_weight_unit_loc, text)

    def goods_mix_tab_weight_goods_number(self, text):
        # 库存输入框输入内容
        self.send_keys(self.goods_mix_tab_weight_goods_number_loc, text)

    def goods_mix_tab_weight_warn_number(self, text):
        self.send_keys(self.goods_mix_tab_weight_warn_number_loc, text)

    def goods_mix_tab_weight_is_best(self):
        # 多选框
        self.is_lists(self.goods_mix_tab_weight_is_best_loc)

    def goods_mix_tab_is_on_sale(self):
        # 勾选允许销售
        self.is_list(self.goods_mix_tab_is_on_sale_loc)

    def goods_mix_tab_is_alone_sale(self):
        # 勾选普通商品销售
        self.is_list(self.goods_mix_tab_is_alone_sale_loc)

    def goods_mix_tab_is_shipping(self):
        # 勾选免运费
        self.is_list(self.goods_mix_tab_is_shipping_loc)

    def goods_mix_tab_is_keywords(self, text):
        # 关键字输入
        self.send_keys(self.goods_mix_tab_is_keywords_loc, text)

    def goods_mix_tab_is_goods_brief(self, text):
        # 商品简单描述
        self.send_keys(self.goods_mix_tab_is_goods_brief_loc, text)

    def goods_mix_tab_is_seller_note(self, text):
        # 商家备注
        self.send_keys(self.goods_mix_tab_is_seller_note_loc, text)

    def goods_properties_tab_click(self):
        # 点击商品属性
        self.click(self.goods_properties_tab_click_loc)

    def goods_properties_tab_goods_type(self, text):
        # 下拉菜单选择
        self.select(self.goods_properties_tab_goods_type_loc, text)

    def goods_properties_tab_attr_value_list(self, text):
        # 输入笔记本型号
        self.send_keys(self.goods_properties_tab_attr_value_list_loc, text)

    def goods_properties_tab_attr_value_list1(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list1_loc, text)

    def goods_properties_tab_attr_value_list2(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list2_loc, text)

    def goods_properties_tab_attr_value_list3(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list3_loc, text)

    def goods_properties_tab_attr_value_list4(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list4_loc, text)

    def goods_properties_tab_attr_value_list5(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list5_loc, text)

    def goods_properties_tab_attr_value_list6(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list6_loc, text)

    def goods_properties_tab_attr_value_list7(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list7_loc, text)

    def goods_properties_tab_attr_value_list8(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list8_loc, text)

    def goods_properties_tab_attr_value_list9(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list9_loc, text)

    def goods_properties_tab_attr_value_list10(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list10_loc, text)

    def goods_properties_tab_attr_value_list11(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list11_loc, text)

    def goods_properties_tab_attr_value_list12(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list12_loc, text)

    def goods_properties_tab_attr_value_list13(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list13_loc, text)

    def goods_properties_tab_attr_value_list14(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list14_loc, text)

    def goods_properties_tab_attr_value_list15(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list15_loc, text)

    def goods_properties_tab_attr_value_list16(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list16_loc, text)

    def goods_properties_tab_attr_value_list17(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list17_loc, text)

    def goods_properties_tab_attr_value_list18(self, text):
        self.send_keys(self.goods_properties_tab_attr_value_list18_loc, text)

    def goods_centent_surch(self, text):
        self.send_keys(self.goods_centent_surch_loc, text)

    def goods_centent_surch_click(self):
        self.click(self.goods_centent_surch_click_loc)

    def goods_centent_surch_is_sussecc(self, text):
        self.is_text_inelement(self.goods_centent_surch_is_sussecc_loc, text)


if __name__ == '__main__':
    import time

    driver = open_browser()
    Add_goods = Add_goods(driver)
    Add_goods.open_url(admin_url2)
    Add_goods.add_submit()
    Add_goods.click_ecshop()
    Add_goods.input_username('admin')
    Add_goods.input_password('admin888')
    Add_goods.submit()
    Add_goods.switch_ifarme_clik()
    Add_goods.click_add_goods()
    Add_goods.click_add_goods2()
    Add_goods.alert_back()
    Add_goods.switch_ifarme_clik2()
    time.sleep(4)
    Add_goods.send_keys_add_goodsname("shoujia")

    Add_goods.send_keys_oods_number(788945645)
    Add_goods.goods_name_style('下划线')
    Add_goods.cat_id('数码时尚')
    Add_goods.add_goods_button()
    Add_goods.add_goods_send('1242')
    Add_goods.add_goods_send_click()
    Add_goods.add_goodes_addother()
    Add_goods.add_goods_mennu_addother('智能硬件')
    Add_goods.goods_brand("飞利浦")
    Add_goods.add_goods_brand()
    Add_goods.goods_brand_send("1111")
    Add_goods.add_goods_brand_click()
    Add_goods.goods_supplier("北京供货商")
    Add_goods.goods_shop_price(100)
    Add_goods.goods_volume_number(20)
    Add_goods.goods_volume_price(170)
    Add_goods.goods_market('140.5')
    Add_goods.goods_market_price_int()
    Add_goods.goods_virtual_sales(150)
    Add_goods.goods_give_integral('-0.8')
    Add_goods.goods_rank_integral('-0.8')
    Add_goods.goods_integral('3')
    Add_goods.goods_is_promote()
    Add_goods.goods_promote_1(200)
    Add_goods.goods_promote_start_date_js()
    Add_goods.goods_promote_end_date_js()
    Add_goods.goods_promote_start_date('2019-11-11')
    Add_goods.goods_promote_end_date('2019-11-30')
    Add_goods.goods_goods_img(r'C:\Users\简小芳\Desktop\u=1630069208,1869311629&fm=26&gp=0.jpg')
    Add_goods.goods_goods_img_url(r'u=1630069208,1869311629&fm=26&gp=0.jpg')
    Add_goods.goods_auto_thumb()
    Add_goods.goods_goods_thumb(r'C:\Users\简小芳\Desktop\u=1630069208,1869311629&fm=26&gp=0.jpg')
    Add_goods.goods_goods_thumb_url(r'u=1630069208,1869311629&fm=26&gp=0.jpg')

    Add_goods.goods_descripitopn_click()
    Add_goods.goods_descripitopn_frame()
    Add_goods.goods_descripitopn_frame2()
    Add_goods.goods_descripitopn_send("12312312312312")
    Add_goods.alert_back()
    Add_goods.alert_back()
    Add_goods.goods_mix_tab_click()
    Add_goods.goods_mix_tab_click_goods_weight(100)
    Add_goods.goods_mix_tab_weight_unit('克')
    Add_goods.goods_mix_tab_weight_goods_number(200)
    Add_goods.goods_mix_tab_weight_warn_number(50)
    Add_goods.goods_mix_tab_weight_is_best()
    Add_goods.goods_mix_tab_is_on_sale()
    Add_goods.goods_mix_tab_is_alone_sale()
    Add_goods.goods_mix_tab_is_shipping()
    Add_goods.goods_mix_tab_is_keywords("手机")
    Add_goods.goods_mix_tab_is_goods_brief("手机")
    Add_goods.goods_mix_tab_is_seller_note("苹果手机")
    Add_goods.goods_properties_tab_click()
    Add_goods.goods_properties_tab_goods_type('笔记本电脑')
    Add_goods.goods_properties_tab_attr_value_list(13256)
    Add_goods.goods_properties_tab_attr_value_list1(12354)
    Add_goods.goods_properties_tab_attr_value_list2(12354)
    Add_goods.goods_properties_tab_attr_value_list3(12354)
    Add_goods.goods_properties_tab_attr_value_list4(12354)
    Add_goods.goods_properties_tab_attr_value_list5(12354)
    Add_goods.goods_properties_tab_attr_value_list6(12354)
    Add_goods.goods_properties_tab_attr_value_list7(12354)
    Add_goods.goods_properties_tab_attr_value_list8(12354)
    Add_goods.goods_properties_tab_attr_value_list9(12354)
    Add_goods.goods_properties_tab_attr_value_list10(12354)
    Add_goods.goods_properties_tab_attr_value_list11(12354)
    Add_goods.goods_properties_tab_attr_value_list12(12354)
    Add_goods.goods_properties_tab_attr_value_list13(12354)
    Add_goods.goods_properties_tab_attr_value_list14(12354)
    Add_goods.goods_properties_tab_attr_value_list15(12354)
    Add_goods.goods_properties_tab_attr_value_list16(12354)
    Add_goods.goods_properties_tab_attr_value_list17(12354)
    Add_goods.goods_properties_tab_attr_value_list18(12354)
    # Add_goods.add_goods_reset()
    Add_goods.add_goods_sure()
    # time.sleep(5)
    # Add_goods.surch_goods("shoujia")
    # Add_goods.surch_goods_click()
    # print(Add_goods.surch_goods_result('没有找到任何记录'))
    Add_goods.open_url('http://172.16.1.244/ecshop')
    Add_goods.goods_centent_surch()
    Add_goods.goods_centent_surch_click()
    Add_goods.goods_centent_surch_is_sussecc('无法搜索到您要找的商品！')
