'''
公共方法（环境变量）
'''
# 封装公共URL
# 封装请求头
from config import init_log_config

BASE_URL = 'http://182.92.81.159'
BASE_headers = {"Content-Type": "application/json"}
userid = None

init_log_config()