# 此模块处理excel查询及写入相关

import openpyxl

class HandleExcel:

    def __init__(self,file_name,sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name

    def read_data(self):
        #  读取excel数据
        workbook1 = openpyxl.load_workbook(self.file_name)
        sh1 = workbook1[self.sheet_name]

        res1 = list(sh1.rows)
        title1 = [i.value for i in res1[0]]
        list_all = []

        for item in res1[1:]:
            data1 = [i.value for i in item]
            dict1 = dict(zip(title1, data1))
            list_all.append(dict1)
        return list_all

