"""
架构介绍：
    核心：api + case + data
        |--api:请求业务（request）
        |--case:测试用例（unittest)
        |--data:参数化（json文件封装数据）
        调用关系：调用者--case, 被调用者--api + data

    报告：request + tools + run_suite


"""
import  os

# 封装 URL 的前缀
BASE_URL = "http://182.92.81.159/api/sys/"
# 动态获取绝对路径
PRO_PATH = os.path.dirname(os.path.abspath(__file__))

# 全局变量：
TOKEN = None  # 登录后返回的token值
print("app.py中token的值为：%s" % TOKEN)

USER_ID = None # 新增用户的ID
print("--->>>app.py文件中，新增用户的ID为<<<---%s" % USER_ID)

























