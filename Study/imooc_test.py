# coding=utf-8
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
import unittest
from Base.base_request import request

host = 'http://www.imooc.com/'
class ImoocCase(unittest.TestCase):
    def test_newcourse(self):
        url = host+'api3/newcourseskill'
        data = {
            'uid':'8128908',
            'secrect':'',
            'uuid':'b98908694ee8f7c64d07cb21d42adde5',
            'timestamp':'1626353016108',
            'cid':'0',
            'token':'3472d88c0077f08ad09d726632f48316'
        }     
        res = request.run_main('post',url,data)
        print(res)
        self.assertEqual(res['errorCode'],'1000')

if __name__ == "__main__":
    unittest.main()
