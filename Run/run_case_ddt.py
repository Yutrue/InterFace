#coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)

import json
from Util.handle_excel import excel_data
from Base.base_request import request
from Util.handle_result import handle_result,handle_result_json,get_result_json
from Util.handle_cookie import get_cookie_value,write_cookie
from Util.handle_header import get_header
from Util.codition import get_data

import unittest
import ddt
data = excel_data.get_excel_data()

import HTMLTestRunner

@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):
    @ddt.data(*data)
    def test_main_case(self,data):
        cookie = None
        get_cookie = None
        header = None
        depend_data = None
        is_run = data[2]              #是否执行
        case_id = data[0]
        i = excel_data.get_rows_numble(case_id)
        if is_run == 'yes':
            is_depend = data[3]
            url = data[5]             # api3/beta4
            method = data[6]          # post or get
            data1 = json.loads(data[7])           #{"username":"111111"}
            cookie_method = data[8]   #cookie操作 yes or write
            is_header = data[9]
            except_method = data[10]   #预期结果方式 mec、errorcode、json
            except_result = data[11]   #预期结果    

            try:
                if is_depend:
                    depend_key = data[4]
                    depend_data = get_data(is_depend)
                    data1[depend_key] = depend_data

                if cookie_method == 'yes':
                    cookie = get_cookie_value('app')
                if cookie_method == 'write':
                    get_cookie = {"is_cookie":"app"}

                if is_header == 'yes':
                    header = get_header()
            
                res = request.run_main(method,url,data1,cookie,get_cookie,header)   #获取到的是base_request import request.run_main   
                code = str(res['errorCode'])   
                message = res['errorDesc']     

                if except_method == 'mec':
                    config_message = handle_result(url,code)   
                    try:
                        self.assertEqual(message,config_message)
                        excel_data.excel_write_data(i,13,'通过')
                    except Exception as e:
                        excel_data.excel_write_data(i,13,'失败')
                        excel_data.excel_write_data(i,14,json.dumps(res))
                        raise e

                if except_method == 'errorcode':
                    try:
                        self.assertEqual(except_result,code)
                        excel_data.excel_write_data(i,13,'通过')
                    except Exception as e:
                        excel_data.excel_write_data(i,13,'失败')
                        excel_data.excel_write_data(i,14,json.dumps(res))
                        raise e

                if except_method == 'json':
                    if code == '1000':
                        status_str = 'sucess'
                    else:
                        status_str = 'error'
                    excepect_result = get_result_json(url,status_str)  #/Config/result.json 下的url对应数据
                    result = handle_result_json(res,excepect_result)
                    try:
                        self.assertTrue(result)
                        excel_data.excel_write_data(i,13,'通过')
                    except Exception as e:
                        excel_data.excel_write_data(i,13,'失败')
                        excel_data.excel_write_data(i,14,json.dumps(res))
                        raise e

            except Exception as e:
                excel_data.excel_write_data(i,13,'失败')
                raise e

                
if __name__ == '__main__':
    # unittest.main()
    case_path = base_path+"/Run"
    report_path = base_path+"/Report/report.html"
    discover = unittest.defaultTestLoader.discover(case_path,pattern="run_case_*.py")
    with open(report_path,"wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="test",description="test one")
        runner.run(discover)
        