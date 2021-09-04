# coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
# import requests
from Base.base_request import request
import unittest

url = "http://www.imooc.com"
data ={
    "uesrname":"test",
    "password":"123456"
}

class TestCase01(unittest.TestCase):
    # def setUp(self):
    #     print('case开始执行')

    # def tearDown(self):
    #     print('case执行结束')

    @classmethod
    def setUpClass(cls):
        print('case类开始执行')

    @classmethod
    def tearDownClass(cls):
        print('case类执行结束')

    def test_01(self):
        print('case01')

    def test_02(self):
        print('case02')

    def test_06(self):
        res = request.run_main('get',url,data)
        print(res)


if __name__ == '__main__':
    unittest.main()