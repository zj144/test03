import logging
import unittest

from parameterized import parameterized
from toos.assert_common import login_assert
import api
from toos.read_json import read_json
from toos.read_txt import read_login_txt



class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 获取api登录对象
        from api.api_login import ApiLogin
        cls.api = ApiLogin()
    @parameterized.expand(read_login_txt('login.txt'))
    # @parameterized.expand(read_json('login.json'))


    def test01_login(self,mobile,password,code,success,cd,message,n1):
        logging.info('info级别日志{}'.format(read_login_txt('login.txt')))


        rp = self.api.api_login(mobile,password)
        print(rp.status_code)
        print(rp.json())
        if cd == '10000':
            api.BASE_headers['Authorization']='Bearer '+rp.json().get('data')
            print('登录成功后请求头',api.BASE_headers)

            # logging.debug('登录成功后请求头',api.BASE_headers)

        # print(type(str(rp.json().get('code'))))
        # print(str(rp.json().get('code')))
        #
        # print(type(str(rp.json().get('success'))))
        # print(str(rp.json().get('success')))
        #
        # print(type(str(rp.json().get('message'))))
        # print(str(rp.json().get('message')))
        login_assert(self=self,rp=rp,code=code,success=success,cd=cd,message=message,n1=n1)