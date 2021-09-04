# coding=utf-8
import sys
import os
import json
base_path = os.getcwd()
sys.path.append(base_path)

from Util.connect_mysql import GetMysql as ge

def test02():
    result = ge("SELECT * FROM prize WHERE id=1")
    print(result)

if __name__ == '__main__':
    test02()


