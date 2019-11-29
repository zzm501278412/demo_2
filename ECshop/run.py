from common.HTMLTestRunner_cn import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os0

#  定义发送邮件
a =["1564681001@qq.com",'475682349@qq.com','lhxpdy@qq.com','347900268@qq.com','775770566@qq.com']
def  send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf_8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com")
    smtp.login("zzm8023qian@qq.com",  "entsuyggmwvzbjdi")
    smtp.sendmail("zzm8023qian@qq.com",a, msg.as_string())
    smtp.quit()
    print('邮件已发送,请注意查收!')


def new_report(testreport):
    lists = os.listdir((testreport))
    lists.sort(key=lambda fn: os.path.getmtime(testreport+"\\"+fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

#指定测试用例为当前文件夹下test_case目录

if __name__ == '__main__':

    test_dir = r'./script'
    test_report =r'./report'

    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern='test_*.py')

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report+'\\'+now+'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                           title=' 测试报告',
                            description='用例执行情况')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)