#!/usr/bin/python3
"""unittest module for square class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testSquare(unittest.TestCase):

    def test_isSubClass(self):

        k = Square(2, 2)

        self.assertIsInstance(k, Base)
        self.assertIsNot(k, Base)




if __name__ == '__main__':
    unittest.main()
