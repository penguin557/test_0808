import json
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
import requests
from unittestreport import ddt,list_data
from common.handle_excel import HandleExcel
import unittest


@ddt
class Web_sjkb_all(unittest.TestCase):
    """ 获取excel测试数据 """
    DATA_DIR = os.path.join(BASE_DIR,"datas")
    excel_data = HandleExcel(os.path.join(DATA_DIR,"testcase3.xlsx"),"web_more_tz")

    cases = excel_data.read_data()
    #获取到的列表类型数据传给list_data

    @list_data(cases)
    def test_web_sjkb(self,item):

        method = item["method"]
        url1 = "http://uat2-vtown-center.yuanjingweitang.com" + item["path"]
        data22 = eval(item["data"])
        token2 = "1E1A2AFB69434DC69BEAA00D6BDB10E9"
        headers2 = {"token": token2}
        respond = requests.request(method, url=url1, headers=headers2, json=data22)
        res = respond.json()
        print(res)
        check = res["code"]

        try:
            self.assertIn("200",check)
        except AssertionError as e:
            print(e)
            # my_log.error(e)
            # my_log.exception(e)
            raise e

if __name__ == '__main__':
    unittest.main

# url2 = "http://uat2-vtown-center.yuanjingweitang.com/rent-api/v1/contract/rent/tobe/expired"
# data22 = {"currentPage":1,"pageSize":10,"projectKeys":["cc27b35adfd246cfa7acb00ff890c2dc"],"rentContractExpireDays":30000}
# header2 = {"token":"40CF983D77BA4486991A9EC7A3C02772"}

"""url1 = cases[0]["url"]
print("这是case:",cases)
print(url1)

token1 = conf.get("user_data","token")
print("这是token:",token1)
header1 = {"token":token1}

data1 = eval(cases[0]["data"])
print(data1)
print(type(data1))

url = "http://uat2-vtown-center.yuanjingweitang.com/rent-api/v1/business/user/space/biz/residence/list"
header = {"Token":"D824DD21054A44979BDA830C2102DC0A"}
data = {'currentPage': 1, 'pageSize': 10, 'projectKeys': ['cc27b35adfd246cfa7acb00ff890c2dc'], 'rentContractExpireDays': 30000}

respond = requests.request("post",url=url1,headers=header1,json=data1)
print(respond.text)"""