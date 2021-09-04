#coding-utf-8
import openpyxl
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

class RunMain:
    def run_case(self):
        
        rows = excel_data.get_rows()  #获取行数
        # print(rows)
        for i in range(rows):
            cookie = None
            get_cookie = None
            header = None
            depend_data = None

            data = excel_data.get_rows_value(i+2)         #获取到的是excel表格里case的值
            # print(data)
            is_run = data[2]              #是否执行

            if is_run == 'yes':
                is_depend = data[3]
                
                url = data[5]             # api3/beta4
                method = data[6]          # post or get

                data1 = json.loads(data[7])           #{"username":"111111"}

                cookie_method = data[8]   #cookie操作 yes or write
                is_header = data[9]
                except_method = data[10]   #预期结果方式 mec、errorcode、json
                except_result = data[11]   #预期结果       

                if is_depend:
                    #pass
                    depend_key = data[4]
                    depend_data = get_data(is_depend)
                    # print("获取前置用例里需要取得的数据，作为后置用例的前提------》",depend_data)
                    data1[depend_key] = depend_data

                if cookie_method == 'yes':
                    cookie = get_cookie_value('app')
                if cookie_method == 'write':
                    get_cookie = {"is_cookie":"app"}

                if is_header == 'yes':
                    header = get_header()
                # print(header)

                res = request.run_main(method,url,data1,cookie,get_cookie,header)   #获取到的是base_request import request.run_main
                # print(res)

                # if cookie_method == 'write':
                #     write_cookie(res,'app')
                    
                code = str(res['errorCode'])   
                # print(code)
                message = res['errorDesc']     

                if except_method == 'mec':
                    config_message = handle_result(url,code)   

                    if message == config_message:
                        excel_data.excel_write_data(i+2,13,'通过')
                    else:
                        excel_data.excel_write_data(i+2,13,'失败')
                        excel_data.excel_write_data(i+2,14,json.dumps(res))

                if except_method == 'errorcode':
                    # print(type(except_result))
                    # print(type(code))
                    if except_result == code:
                        excel_data.excel_write_data(i+2,13,'通过')
                    else:
                        excel_data.excel_write_data(i+2,13,'失败')
                        excel_data.excel_write_data(i+2,14,json.dumps(res))

                if except_method == 'json':
                    # pass
                    # print(code)
                    if code == '1000':
                        status_str = 'sucess'
                    else:
                        status_str = 'error'
                    # print(status_str)
                    excepect_result = get_result_json(url,status_str)  #/Config/result.json 下的url对应数据
                    # print(excepect_result)

                    result = handle_result_json(res,excepect_result)
                    if result:
                        excel_data.excel_write_data(i+2,13,'通过')
                    else:
                        excel_data.excel_write_data(i+2,13,'失败')
                        excel_data.excel_write_data(i+2,14,json.dumps(res))
                    

if __name__ == "__main__":
    run = RunMain()
    run.run_case()

