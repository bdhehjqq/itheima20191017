"""
封装员工的增删改查请求实现

"""

import app


class EmpCRUD:

    # 函数1：增
    def add(self, session, username, mobile, workNumber):
        # return session对象.post("新增的URL", json = 提交的数据)
        myAddEmp = {
            "username": username,
            "mobile": mobile,
            "workNumber": workNumber
        }
        print("API文件中token的值为：%s " % app.TOKEN)
        return session.post(app.BASE_URL + "user",
                            json=myAddEmp,
                            headers={"Authorization": "Bearer " + app.TOKEN}
                            )

    # 函数2：改
    def update(self, session, username, userId):
        myUpdateEmp = {"username": username,

                       }
        print("-" * 100)
        print("API文件接收到的传递过来的员工ID为：%s" % userId)
        id = "".join(userId)  # 传过来的员工id是个列表，要转成字符串
        print("**********************id = %s" % id)
        return session.put(app.BASE_URL + "user/" + id, json=myUpdateEmp,
                            headers={"Authorization": "Bearer " + app.TOKEN}
                            )

    # 函数3：查
    def get(self):
        pass

    # 函数4：删
    def delete(self):
        pass

