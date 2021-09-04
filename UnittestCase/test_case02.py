#coding=utf-8
import requests
import unittest

url = 'http://127.0.0.1:5000/searchdata'
header = {
    'Content-Type':'application/x-www-form-urlencoded'
}
data = {
    'url':'api3/newcourseskill'
}

class TestCase02(unittest.TestCase):
    def setUp(self):
        print('case开始执行')

    def tearDown(self):
        print('case结束执行')

    # @classmethod
    # def setUpClass(cls):
    #     print('case类开始执行')

    # @classmethod
    # def tearDownClass(cls):
    #     print('case类结束执行')

    def test01(self):
        print("执行case01")
        res = requests.post(url=url,headers=header,data=data,verify=False).json()
        # print(type(res))
        info = {
            "status": 1,
            "data": {
                "id": 0,
                "name": "全部课程",
                "pic": "http://static.mukewang.com/static/img/all.png",
                "numbers": 881
            },
            "errorCode": 1000,
            "errorDesc": "成功",
            "timestamp": 1561274619244,
            "data2": 12
        }
        # print(type(info))
        self.assertDictEqual(res,info,msg='这两个字典不相等')

    def test02(self):
        print("执行case02")
        str1 = '123456'
        str2 = '654321'
        self.assertEqual(str1,str2,msg='这两个字符串不相等')

    def test03(self):
        print("执行case03")
        flag = True
        self.assertFalse(flag)

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    # suite.addTest(TestCase01('test01'))
    # suite.addTest(TestCase01('test03'))
    # suite.addTest(TestCase01('test02'))

    # tests = [TestCase01('test03'),TestCase01('test01'),TestCase01('test02')]
    # suite.addTests(tests)

    # runner = unittest.TextTestRunner()
    # runner.run(suite)