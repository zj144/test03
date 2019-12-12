def login_assert(self,rp,code=None,success=None,cd=None,message=None,n1=None):
    # 断言响应状态码
    self.assertEqual(code,str(rp.status_code))
    # 断言返回success
    self.assertEqual(success,str(rp.json().get('success')))
    # 判断返回code
    self.assertEqual(cd, str(rp.json().get('code')))
    # 断言返回message
    self.assertEqual(message,str(rp.json().get('message')))
    # 断言返回data是状态
    if n1 == '1':
        self.assertTrue(rp.json().get('data'))
    elif n1 == '0':
        self.assertEqual(None,rp.json().get('data'))

def employee_assert(self,rp,code=None,success=None,cd=None,message=None,n1=None):
    # 断言响应状态码
    self.assertEqual(code,str(rp.status_code))
    # 断言返回success
    self.assertEqual(success,str(rp.json().get('success')))
    # 判断返回code
    self.assertEqual(cd, str(rp.json().get('code')))
    # 断言返回message
    self.assertEqual(message,str(rp.json().get('message')))
    # 断言返回data是状态
    if n1 == '1':
        self.assertTrue(rp.json().get('data'))
    elif n1 == '0':
        self.assertEqual(None,rp.json().get('data'))
