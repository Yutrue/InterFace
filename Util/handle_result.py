#coding=utf-8
import json
import openpyxl
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path) 
from Util.handle_json import get_value
from deepdiff import DeepDiff

def handle_result(url,code):

    data = get_value(url,"/Config/code_message.json")
    if data != None:
        for i in data:
            message = i.get(str(code))
            if message:
                return message
    return None

def get_result_json(url,status):
    data = get_value(url,"/Config/result.json")
    # print(data)
    if data != None:
        for i in data:
            # print('这个i是。。。',i)
            # print(status)
            message = i.get(status)
            # print(message)
            if message:
                # print(message)
                return message
    return None

#校验格式
def handle_result_json(dict1,dict2):

    if isinstance(dict1,dict) and isinstance(dict2,dict):
        # dict1 = {"aaa":"111","bbb":"222"}
        # dict2 = {"aa2":"222","bbb":"333"}
        cmp_dict = DeepDiff(dict1,dict2,ignore_order=True).to_dict()
        # print(cmp_dict)
        if cmp_dict.get("dictionary_item_added"):
            return False
        else:
            return True

    return False


if __name__ == '__main__':
    # hun = handle_result('api3/login','1001')
    # print(hun)
    # dict1 = {"aaa":"111","bbb":"222"}
    # dict2 = {"aaa":"222","bbb":"333"}
    # print(handle_result_json(dict1,dict2))
    print(get_result_json('api3/getdownrecommend','error'))

