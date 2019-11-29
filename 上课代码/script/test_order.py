"""
掌握pytest用例执行顺序
操作步骤
    pytest框架下用例执行的默认顺序--按照书写顺序从上到下执行
    控制用例执行顺序方法:
    在测试用例前添加一个装饰
    @pytest.mark.run(数字)
    执行顺序的问题
    0>较小的正数>较大的正数>不使用order>较小的负数>较大复数

"""
import pytest


@pytest.mark.run(order=1)
def test_a():
    """第一条"""
    print("------------------->test_a")
    assert 1
@pytest.mark.run(order=4)
def test_b():
    """第二条"""
    print("------------------->test_b")
    assert 0
@pytest.mark.run(order=2)
def test_c():
    """第三条"""
    print("------------------->test_b")
    assert 1
@pytest.mark.run(order=3)
def test_d():
    """第四条"""
    print("------------------->test_d")
    assert 1
if __name__ == '__main__':
    pytest.main()