

# 初始化日志器配置
import logging
import os
from logging.handlers import TimedRotatingFileHandler
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def init_log_config():
    # 实例化日志器
    logger = logging.getLogger()
    # 设置日志添加级别
    logger.setLevel(logging.INFO)

    shi = logging.StreamHandler()
    trfhl = TimedRotatingFileHandler(BASE_DIR+'/log/mylog.log',when='h',interval=1,backupCount=0,encoding='utf8')

    fm = logging.Formatter(
        fmt="%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s")

    shi.setFormatter(fm)
    trfhl.setFormatter(fm)

    logger.addHandler(shi)
    logger.addHandler(trfhl)
