"""
掌握带返回值的fixture
    编写带返回值fixture
    使用用例调用
"""
import pytest
#编写fixture
@pytest.fixture()
def data():
    print("生成数据的方法")
    return 3

def test_data(data):
    print("执行用例步骤")
    print("得到数据%s"%data)
    assert data==3
if __name__ == '__main__':
    pytest.main()