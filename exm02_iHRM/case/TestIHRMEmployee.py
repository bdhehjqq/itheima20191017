# 导包
import unittest
import requests
import jsonpath

# 创建测试类
import app
from api.EmpAPI import EmpCRUD


class TestEmployee(unittest.TestCase):
    # 初始化函数
    def setUp(self):
        self.session = requests.Session()
        # 创建调用的api类的对象
        self.emp_obj = EmpCRUD()

    # 资源销毁函数
    def tearDown(self):
        self.session.close()

    # 测试函数1：增
    def test_emp_add(self):
        # 1.发起请求
        response = self.emp_obj.add(self.session, "xujmg126", "139202011126", "202011026")
        # 2.对返回的响应结果进行断言
        print("新增员工成功的响应结果", response.json())
        # 3.获取新增用户的ID # jres['data'][0]['bbb']
        # self.userId = response.json().get("data").id
        """
        import jsonpath
        s = jsonpath.jsonpath(dic,'$..name')   #不管有多少层，写两个.都能取到
        print(s) #['xiaohei'] 返回的是一个列表
        s = jsonpath.jsonpath(dic,'$..hehe')   #当不存在hehe这个key时，返回false
        print(s)  #False
"""
        app.USER_ID = jsonpath.jsonpath(response.json(), '$..id')
        print("---新增用户的ID为---%s" % app.USER_ID)

    # 测试函数2：改
    def test_emp_update(self):
        # 1.发起请求
        response = self.emp_obj.update(self.session, "xujmg1a7", app.USER_ID)
        # print(app.USER_ID)
        # 2.对返回的响应结果进行断言
        print("修改员工成功的响应结果", response.json())

    # 测试函数3：查
    def test_emp_get(self):
        pass

    # 测试函数4：删
    def test_emp_delete(self):
        pass
