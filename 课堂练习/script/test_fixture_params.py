"""
掌握带参数化fixture编写
@pytest.fixture(params=[列表格式数据])
request是pytest中内置关键字
总结
    pytest.fixture 主要是用来完成测试用例执行前后操作
        例如:测试前后对数据库连接/端口,打开/关闭浏览器app
    fixture还可以用来准备测试数据
        带参数fixture
        有返回值fixture--推荐使用
    fixtur中的参数
        scope:确定fixture作业范围 默认function,还可以写出class,module,session
        autouse:当值为True的时候,相当于setup
        name:对fixture重命名

"""
import pytest
@pytest.fixture(params=[1,2,2,3,3,])
def data(request):
    return request.param



def test_data(data):
    print("传入数据%s"%data)
    assert 1==data
if __name__ == '__main__':
    pytest.main()