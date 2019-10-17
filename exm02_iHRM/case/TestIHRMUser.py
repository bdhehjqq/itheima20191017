import json
import unittest
import requests
import app


# 编写 json 解析函数
from api.UserAPI import UserLogin


def read_json():
    # 1. 创建接收数据的空列表
    data = []
    # 2. 打开文件流，将数据导入列表
    with open(app.PRO_PATH + "/data/login_data.json", "r", encoding="utf-8") as f:
        for value in json.load(f).values():
            mobile = value.get("mobile")
            password = value.get("password")
            success = value.get("success")
            code = value.get("code")
            message = value.get("message")
            ele = (mobile, password, success, code, message)
            data.append(ele)
    # 3.返回列表
    return data


# 创建测试类
class TestUser(unittest.TestCase):
    # 初始化函数
    def setUp(self):
        # 初始化session
        self.session = requests.Session()
        # 初始化 api 对象
        self.user_obj = UserLogin()

    # 资源销毁函数
    def tearDown(self):
        # 销毁session
        self.session.close()

    # 测试函数1：登录
    # 使用参数化
    def test_login(self, session, mobile, password):
        # 1.调用请求业务
        # response = 初始化api对象.登录()
        response = self.user_obj.login(self.session, mobile, password)

        # 2.调用断言业务
        print(response.json())
        result = response.json()
        self.assertEqual(successe, result.get("success"))

    # 测试函数2：只实现登录成功
    def test_login_success(self):
        print("-" * 100)
        print("登录成功的接口：")
        # 1.请求业务
        response = self.user_obj.login(self.session, "13800000002", "123456")
        print(response)
        # 2.断言业务
        result = response.json()
        print("登录成功的响应结果", result)
        self.assertEqual(True, result.get("success"))
        self.assertEqual(10000, result.get("code"))
        self.assertIn("操作成功", result.get("message"))

        # 获取响应结果的token
        token = response.json().get("data")
        app.TOKEN = token
        print("-------登录成功后的token值为：%s" % app.TOKEN)



















