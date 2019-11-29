"""
了解预期失败的方法
    xfail(condition,reason)
        condition;条件为真的时候,用例标记失败
         reason:
         条件     用例执行结果
         True       False
         True       True
         False      False
         False      True
在测试执行过程中,会将xpassed状态的用例直接转成failed
  """
import pytest
@pytest.mark.xfail(True,reason="")
def test_1():
    print("预期失败,结果失败")
    assert False
@pytest.mark.xfail(True,reason="")
def test_2():
    print("预期失败,结果成功")
    assert True

@pytest.mark.xfail(False,reason="")
def test_3():
    print("预期成功,结果失败")
    assert False
@pytest.mark.xfail(False,reason="")
def test_4():
    print("预期成功,结果成功")
    assert True

if __name__ == '__main__':
    pytest.main()