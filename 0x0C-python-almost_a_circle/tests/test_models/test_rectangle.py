#!/usr/bin/python3
"""unit trst module for rectangle class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_isSubClass(self):

        k = Rectangle(2, 2)

        self.assertIsInstance(k , Base)
        self.assertIsNot(k, Base)





if __name__ == '__main__':
    unittest.main()
