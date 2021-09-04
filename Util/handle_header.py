import sys
# print(sys.path)
import os
bath_path = os.getcwd()   #用于返回当前工作目录
sys.path.append(bath_path)
import hashlib

from Util.handle_json import read_json

def get_header():
    data = read_json("/Config/header.json")
    # print(data)
    return data

def header_md5(key):
    data = get_header()
    data_md5 = data[key]
    print(data_md5)
    
    md5 = hashlib.md5()
    md5.update(data_md5.encode('utf-8'))
    reps = md5.hexdigest()

    print(reps)
    return reps

if __name__ == '__main__':
    header_md5('id')