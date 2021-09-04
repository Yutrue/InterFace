#coding-utf-8
import openpyxl
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path) 

import json
from Util.handle_json import get_value,read_json,write_value
'''
1、获取cookie
2、写入cookie
3、是否携带
''' 

#获取cookie
def get_cookie_value(cookie_key):
    data1 = read_json("/Config/cookie.json")
    return data1[cookie_key]

    # data["web"] = data1
    # write_value(data)

#写入cookie
def write_cookie(data,cookie_key):
    data1 = read_json("/Config/cookie.json")
    data1[cookie_key] = data
    write_value(data1)


if __name__ == '__main__':
    # print(get_cookie_value('web'))
    data = {
        "456": "123"
        }
    write_cookie(data,"web")
