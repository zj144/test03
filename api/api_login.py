import requests


class ApiLogin:
    def __init__(self):
        import api
        self.headers = api.BASE_headers
        self.login_url = api.BASE_URL+'/api/sys/login'
    # 封装登录
    def api_login(self,mobile,password):
        data = {"mobile":mobile, "password":password}

        import api
        # 111
        return requests.post(url=self.login_url,headers=api.BASE_headers,json=data)
