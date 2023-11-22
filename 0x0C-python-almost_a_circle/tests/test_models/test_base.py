#!/usr/bin/python3
"""test module for the base class/file
"""


import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_base(unittest.TestCase):
    """methods for testing the base class"""

    def test_isSublass(self):

        k = Base()

        self.assertIsInstance(k, Base)

        self.assertIsNot(k, Base)





if __name__ == '__main__':
    unittest.main()
