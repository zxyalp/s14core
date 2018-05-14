# -*- coding: utf-8 -*-
"""
Created on 2017/7/3

@author: summe
"""
import unittest


class TestDemo(unittest.TestCase):

    def setUp(self):
        print("start;")

    def test_add01(self):
        print("test1")

    def test_add02(self):
        print("test2")

    def tearDown(self):
        print("end....")


if __name__ == '__main__':

    suite = unittest.TestSuite()

    suite.addTest(TestDemo('test_add01'))

    runner = unittest.TextTestRunner()

    runner.run(suite)


def test():
    print("shjdhj")


if __name__ == '__main__':
    test()

