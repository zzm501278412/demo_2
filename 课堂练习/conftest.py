"""
掌握confitest.py文件编写格式
操作步骤
    confitest.py文件名不能修改
    在函数前添加@pytest.fixture()装饰器
    在fonfitest.py文件中存放项目所有fixture
    方便对fixture管理和维护
总结
    yield
"""


import pytest
from selenium import webdriver


@pytest.fixture()
def login():
    print("用户登陆")
    yield #当用例执行完成后,执行yield后的代码
    print("关闭app")
@pytest.fixture()
def driver(request):
    driver=webdriver.Chrome()
    def end():
        driver.quit()
    request.addfinalizer(end)
    return driver
