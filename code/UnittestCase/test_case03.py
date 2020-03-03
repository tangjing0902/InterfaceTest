#-*- coding: UTF-8 -*-
import unittest


class TestCase03(unittest.TestCase):

    def setUp(self):
        print("case开始执行")

    def test_01(self):
        print("TestCase03_test_01")

    def test_02(self):
        print("TestCase03_test_02")

    def tearDown(self):
        print("case结束执行")
