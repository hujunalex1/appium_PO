#coding:utf-8

from Public import HTMLTestRunner
import unittest
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

import os

case_path = 'E:\\appium\\TestCase\\'
result = 'E:\\appium\\Result\\'

def Creatsuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path, pattern='Test_*.py', top_level_dir=None)

    #将测试用例加入测试容器中
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
        print testunit
    return testunit

test_case = Creatsuite()

#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

#定义个报告存放路径，支持相对路径
tdresult = result + day
if os.path.exists(tdresult):
    filename = tdresult + "\\" + now + "_result.html"
    fp = file(filename, 'wb')
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'NALA_app测试报告', description=u'用例详情：')

    #运行测试用例
    runner.run(test_case)
    fp.close()  #关闭报告文件
else:
    os.mkdir(tdresult)
    filename = tdresult + "\\" + now + "_result.html"
    fp = file(filename, 'wb')
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'NALA_app测试报告', description=u'用例详情：')
    #运行测试用例
    runner.run(test_case)
    fp.close()  #关闭报告文件

def new_file(case_path):
    #列举test_dir目录下的所有文件，结果以列表形式返回。
    lists=os.listdir(case_path)
    #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    #最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn:os.path.getmtime(case_path+'\\'+fn))
    #获取最新文件的绝对路径
    file_path=os.path.join(case_path,lists[-1])
    return file_path

def send_email(newfile):
    f=open(newfile,'rb')
    #读取文件内容
    mail_body=f.read()
    f.close()
    #发送邮箱服务器
    smtpserver = 'smtp.163.com'
    #发送邮箱用户名/密码
    user = 'xxxx'
    password='xxxx'
    #发送邮箱
    sender='xxxx'
    #多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver=['xxx']
    #发送邮件主题
    subject = 'NALA_APP定时自动化测试报告'

    msg=MIMEMultipart('mixed')

    msg_html1 = MIMEText(mail_body,'html','utf-8')
    msg.attach(msg_html1)

    msg_html = MIMEText(mail_body,'html','utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)
    msg['From'] = 'xxx <xxxx>'
    msg['To'] = ";".join(receiver)
    msg['Subject']=Header(subject,'utf-8')

    #连接发送邮件
    smtp=smtplib.SMTP()
    smtp.connect(smtpserver,25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

if __name__=='__main__':
    print '=====AutoTest Start======'

    test_report_dir='E:\\appium\\Result\\2018-03-05'

    #取最新测试报告
    new_report=new_file(test_report_dir)

    #发送邮件，发送最新测试报告html
    send_email(new_report)

    print '=====AutoTest End======'



