#coding = utf-8
import sys
import os
# sys.path.append('D:/WorkSpace/ImoocInterface/')
import unittest

case_path = os.getcwd()
print(case_path)

# from UnittestCase.test_case01 import TestCase01
# from UnittestCase.test_case02 import TestCase02
# from UnittestCase.test_case03 import TestCase03
# case01 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
# case02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
# case03 = unittest.TestLoader().loadTestsFromTestCase(TestCase03)
# suote = unittest.TestSuite([case01,case02,case03])
# unittest.TextTestRunner().run(suote)

discover = unittest.defaultTestLoader.discover(case_path)
# print(discover)
unittest.TextTestRunner().run(discover)