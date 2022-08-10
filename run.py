import unittest
import time
from unittestreport import TestRunner
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

suite = unittest.defaultTestLoader.discover("testcases")
file_time = time.strftime("%Y-%m-%d_%H-%M-%S")
file_name = "微棠接口测试报告" + file_time + ".html"
REPORTS_DIR = os.path.join(BASE_DIR,"reports")
runner = TestRunner(suite,filename=file_name,report_dir=REPORTS_DIR,tester="郑鹏",desc="微棠接口测试报告")
runner.run()