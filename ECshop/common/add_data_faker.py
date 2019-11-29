from faker import Faker
import random


class Add_data_feker():
    def __init__(self):
        self.f = Faker(locale='zh_CN')

    def random_goods_name(self):
        # 随机生成名字
        a = self.f.word()
        return a

    def random_goods_prcie(self):
        # 随机生成价格
        a = self.f.random_int(100, 9999)
        return a

    def random_goods_numberid(self):
        # 生成商品编号
        a = self.f.random_int(100000, 999999)
        b = f'ECS{a}'
        return b

    def random_name_style(self):
        a = ["加粗", "下划线", '删除线', '斜体']
        return random.choice(a)

    def random_suppliers_id(self):
        a = ["北京供货商", '上海供货商',]
        return random.choice(a)

    def random_brand(self):
        a = ["飞利浦", '夏新', '仓品']
        return random.choice(a)
    def random_cat_id(self):
        a=['数码时尚','智能硬件','手机类型','移动电源','配件']
        return random.choice(a)
    def random_start_time(self):
        return self.f.date_between(start_date="-1d", end_date="today")
    def random_end_time(self):
        return self.f.date_between(start_date="today", end_date='+30d')
    def random_goods_img(self):
        a=[r'./datas/u=1630069208,1869311629&fm=26&gp=0.jpg']
        return random.choice(a)
if __name__ == '__main__':
    print(Add_data_feker().random_goods_name())
    print(Add_data_feker().random_goods_prcie())
    print(Add_data_feker().random_goods_numberid())
    print(Add_data_feker().random_name_style())
    print(Add_data_feker().random_suppliers_id())
    print(Add_data_feker().random_brand())
    print(Add_data_feker().random_cat_id())
    print(Add_data_feker().random_start_time())
    print(Add_data_feker().random_end_time())
    print(Add_data_feker().random_goods_img())
