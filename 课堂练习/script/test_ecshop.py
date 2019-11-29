import pytest
"""
掌握pttest fixture定义
步骤
    在定义的函数前添加装饰器
    @pytest.fixture()
    编写函数
   @pytest.fixture()
   def 函数名():
        函数体
    在测试用例函数名成当作参数传入到测试用例中即可
    """
@pytest.fixture(autouse=True)
def login():
    print("用户登陆")
    yield #当用例执行完成后,执行yield后的代码
    print("关闭app")


def test_add_cart():
    print("添加商品---需要登陆")


def test_add_address():
    print("添加地址----需要登陆")


def test_show_goods():
    print("浏览商品---不需要登陆")



if __name__ == '__main__':
    pytest.main()