"""
    组织测试套件，生成测试报告
    准备工作: tools 下粘贴 HTMLTestRunner.py
    流程:
    0. 导包
    1. 创建测试套件对象，被组织被执行的测试函数
    2. 创建并开启文件流，使用 HTMLTestRunner 运行套件对象，并将结果写入文件流

"""
import unittest

from case.TestIHRMEmployee import TestEmployee
from case.TestIHRMUser import TestUser

# 创建套件对象

suite = unittest.TestSuite()
# 添加测试函数或测试类到测试套件中
suite.addTest(TestUser("test_login_success"))
suite.addTest(TestEmployee("test_emp_add"))
suite.addTest(TestEmployee("test_emp_update"))  # 修改员工的用例

# 执行测试套件：
runner = unittest.TextTestRunner()  # runner 是运行者的意思
runner.run(suite)








