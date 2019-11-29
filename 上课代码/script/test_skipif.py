"""
掌握pytest跳过测试的方法
    skipif(condition=判断条件,reason=跳过的原因)
    @pytesr.mark.skipif(条件,原因)#条件为跳过程
"""
import pytest


def login_data():
    return "jerry", "123456"


@pytest.mark.skipif(login_data()[0] == "jerry", reason='不记住密码登陆')  # 当条件为真 跳过测试
def test_login():
    username = login_data()[0]
    password = login_data()[1]
    print("输入用户名%s" % username)
    print("输入密码%s" % password)
    print("点击登录按钮")
    assert username == "jerry"


if __name__ == '__main__':
    pytest.main()
