"""
 掌握pyest中setup和teardown
步骤
    1setup和teardown分类
        模块级---针对.py文件   setup_module/teardown_module
        类级别---setup_class/teardown_class
        方法级别---setup_method/teardown_method
        函数级别---setup_function/teardown_function
"""
import pytest


def test_a():
    print("------------------->test_a")
    assert 1

def test_b():
    print("------------------->test_b")
    assert 0
def setup_function():
    print("打开浏览器/打开app")
def teardown_function():
    print("关闭浏览器/关闭app")
class Test_ecshop():
    def teardown_class(self):
        print("类级别的teardown")
    def setup_class(self):
        print("类级别的setup")

    def setup_method(self):
        print("方法级别的setup")
    def teardown_method(self):
        print("方法级别的teardown")


    def test_a(self):
        print("------------------->test_a")
        assert 1


    def test_b(self):
        print("------------------->test_b")
        assert 0
if __name__ == '__main__':
    pytest.main()