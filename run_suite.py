import unittest

from config import BASE_DIR
from toos.HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover('./scripts/')
with open('{}/report/report.html'.format(BASE_DIR),'wb') as f:
     HTMLTestRunner(stream=f).run(suite)


# unittest.TextTestRunner().run(suite)