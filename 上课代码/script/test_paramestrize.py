"""
掌握pytest参数化方法
parametrize(argnames,agevalues)
    argnames  表示参数的名称
    agevaluese  表示参数的值
@pytest.mark.parametrize()
单个参数的使用
    argnames 一定和测试用例中的参数名保持一致
    argvalues 是一个列表格式
多个参数的使用
    argnames 字符串格式,各个参数之间逗号隔开
    argvalues [(参数值1,参数值2),参数值1,参数值2),参数值1,参数值2)]列表嵌套元组,元组元素的个数和参数个数一致

"""
import pytest
data=['110','10086','120']
@pytest.mark.parametrize("phonenum",data)
def test_login(phonenum):
    print("输入电话号码:%s"%phonenum)

key="phonenum","username","password"
value=[("110",'jerry','123456'),("120",'tom','456789'),("10086",'eddie',"987456")]
@pytest.mark.parametrize(key,value)
def test_login1(phonenum,username,password):
    print("输入电话号码:%s"%phonenum)
    print("输入用户名:%s"%username)
    print("输入密码:%s"%password)
    assert phonenum=="110"
if __name__ == '__main__':
    pytest.main()
