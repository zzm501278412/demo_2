"""
将需要执行的测试用例,添加到测试套件中
将用例执行的结果生成HTML格式的测试报告

"""
import unittest
from common import HTMLTestRunner_cn
import time
from tomorrow import threads

#确定测试用例存放路径
case_path=r'./script'
#将测试文件夹中的测试用例放到测试套件中
discover=unittest.defaultTestLoader.discover(case_path)
#执行测试用例并生成报告
report_path=r'./report'
#确定测试报告的名称
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_file=report_path+'/'+now+'report.HTML'
with open(report_file,'wb') as fp:
    runner=HTMLTestRunner_cn.HTMLTestRunner(
                            stream=fp,
                           title=' ECshop自动化测试报告',
                            description='用例执行情况')

    runner.run((discover))
    fp.close()