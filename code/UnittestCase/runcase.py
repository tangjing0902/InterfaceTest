#-*- coding: UTF-8 -*-
import os
import unittest
# from UnittestCase.test_case01 import TestCase01
# from UnittestCase.test_case02 import TestCase02
# from UnittestCase.test_case03 import TestCase03

# test01 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
# test02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
# test03 = unittest.TestLoader().loadTestsFromTestCase(TestCase03)

case_path = os.getcwd()
# suite = unittest.TestSuite([test01,test02,test03])
suite = unittest.defaultTestLoader.discover(case_path)
unittest.TextTestRunner().run(suite)