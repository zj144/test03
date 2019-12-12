import unittest

from parameterized import parameterized

import api
from api.api_employee import ApiEmployee
from toos.read_json import read_json
from toos.assert_common import employee_assert

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):


        cls.api = ApiEmployee()
    @parameterized.expand(read_json('post_employee.json'))
    def test01_post_employee(self,un,mb,wn,code,success,cd,message,n):
        rp = self.api.post_employee(un,mb,wn)

        api.userid = rp.json().get('data').get('id')

        print('添加后的id',api.userid)

        # 断言
        employee_assert(self=self,rp=rp,code=code,success=success,cd=cd,message=message,n1=n)

    @parameterized.expand(read_json('get_delete_employee.json'))
    def test03_get_employee(self,code,success,cd,message,n):
        rp = self.api.get_employee(api.userid)
        print('查询添加后的员工信息',rp.json())
        employee_assert(self=self, rp=rp, code=code, success=success, cd=cd, message=message, n1=n)

    @parameterized.expand(read_json('put_employee.json'))
    def test02_put_employee(self,um,code,success,cd,message,n):
        rp = self.api.put_employee(um,api.userid)
        print('修改后员工信息',rp.json())
        employee_assert(self=self, rp=rp, code=code, success=success, cd=cd, message=message, n1=n)

    @parameterized.expand(read_json('delete_employee.json'))
    def test04_delete_employee(self,code,success,cd,message,n):
        rp = self.api.delete_employee(api.userid)
        print('删除后返回信息',rp.json())
        employee_assert(self=self, rp=rp, code=code, success=success, cd=cd, message=message, n1=n)