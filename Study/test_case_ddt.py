#coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)

import unittest
import ddt
from Util.handle_excel import excel_data
data = excel_data.get_excel_data()
# data = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9]]

@ddt.ddt
class TestCase01(unittest.TestCase):
    def setUp(self):
        print('case start')

    def tearDown(self):
        print('case end')

    @ddt.data(*data)
    def test01(self,data1):
        #case编号	作用	是否执行	前置条件	依赖key	url	method	data	cookie操作	header操作	预期结果方式	预期结果	result	返回数据

        case_id,function,is_run,condition,depend_key,url,method,data,cookie,header,except_method,except_result,result,result_data = data1
        print('this is test case ',case_id,function,is_run,condition,depend_key,url,method,data,cookie,header,except_method,except_result,result,result_data)


if __name__ == '__main__':
    unittest.main()
