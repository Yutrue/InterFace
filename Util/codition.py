#coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from Util.handle_excel import excel_data
from jsonpath_rw import parse
import json

def split_data(data):
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return case_id,rule_data

def depend_data(data):
    case_id = split_data(data)[0]
    row_number = excel_data.get_rows_numble(case_id)  #获取行号
    data = excel_data.get_cell_value(row_number,14)  #获取前置用例里数据
    # print(data)
    return data

#获取依赖字段 通过规则获取前置用例里某条数据 （depend_data(data),split_data(data)[1]）
def get_depend_data(res_data,key):
    res_data = json.loads(res_data)
    json_exe = parse(key)
    madle = json_exe.find(res_data)
    # for math in madle:
    #     return math.value
    return [math.value for math in madle][0]

def get_data(data):
    
    res_data = depend_data(data)
    # print(res_data)
    rule_data = split_data(data)[1]
    # print(rule_data)

    return get_depend_data(res_data,rule_data)


if __name__ == '__main__':
    # data = excel_data.get_cell_value(4,4)
    # print(split_data(data))
    # print(depend_data("imooc_003>userdata:123456"))
    # data = {
    #     "a":"",
    #     "b":"",
    #     "c":[
    #         {
    #             "d":"d1",
    #             "d2":"d2"
    #         }
    #         # {
    #         #     "d":"d2"
    #         # }
    #     ]
    # }
    # key = 'c.[0].d2'
    # print(get_depend_data(data,key))

    # data = {
    #     "status": 1,
    #     "data": [{
    #         "is_update": "0",
    #         "url": "http://file.mukewang.com/apk/app/130/1620358704/imooc_8.0.5_10102001_android.apk?version=1620358706",
    #         "content": "· 体系课改版，学习体验升级\r\n· 全新直播体系课上线\r\n· 首页交互优化升级\r\n· 视频下载功能优化\r\n\r\n\r\n\r\n",
    #         "size": 29118237,
    #         "latest_version": "8050",
    #         "shadow": 0
    #     }],
    #     "errorCode": 1000,
    #     "errorDesc": "成功",
    #     "timestamp": 1621768411790
    # }
    # key = 'data.[0].size'
    # print(get_depend_data(data,key))

    # data = 'imooc_003>data.[0].size'
    # print(get_data(data))
    pass

