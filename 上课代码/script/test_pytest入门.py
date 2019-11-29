import pytest

"""
掌握pytest编写测试用例的基本方法
操作步骤
    导入pytest
    直接编写测试用例  test开头
    执行用例
    pytest.main("-s 文件名")
python assert断言
    assert 条件,msg"异常信息"
"""

def test_a():
    print("------------------->test_a")
    assert 1

def test_b():
    print("------------------->test_b")
    assert 0
if __name__ == '__main__':
    pytest.main()