#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class Test_Max_Integer(unittest.TestCase):
    """first we can test for correct output"""
    def test_norm(self):
        self.assertEqual(max_integer([2,4,6,8]), 8)
        self.assertEqual(max_integer([-2, -6, -3, -9]), -2)
        self.assertEqual(max_integer([10]), 10)



if __name__ == "__main__":
    unittest.main()

