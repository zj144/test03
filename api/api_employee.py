'''
员工信息管理场景api
接口url:
    1.添加员工
    2.添加员工后返回的员工id
请求头
    1.都需要使用带有token的请求头

'''
import requests

import api


class ApiEmployee:
    def __init__(self):
        self.add_url = api.BASE_URL + '/api/sys/user'
        self.use_url = api.BASE_URL + '/api/sys/user/{}'


    def post_employee(self, username, mobile, worknumber):
        data = {"username": username,
                "mobile": mobile,
                "workNumber": worknumber
                }
        return requests.post(url=self.add_url,json=data,headers=api.BASE_headers)

    def get_employee(self,x):
        return requests.get(url=self.use_url.format(x),headers=api.BASE_headers)

    def put_employee(self,u,x):
        data = {
                "username": u
                }
        return requests.put(url=self.use_url.format(x),json=data,headers=api.BASE_headers)

    def delete_employee(self,x):
        return requests.delete(url=self.use_url.format(x),headers=api.BASE_headers)

