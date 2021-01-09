#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        """ to test max"""
        self.assertEqual(max_integer([5, 3, 2]), 5)
        self.assertEqual(max_integer([-5, 3, 2]), 3)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-5, -3, -2]), -2)
        self.assertEqual(max_integer([3, 5, 9, 2]), 9)
        self.assertEqual(max_integer(["a", "t", "e"]), "t") 
        self.assertEqual(max_integer("atenea"), "t")
    
    def test_none(self):
        """to test if empty"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer([None]))
        self.assertIsNone(max_integer())
        

    def test_intergers(self):
        """check for intergers"""
        with self.assertRaises(TypeError): max_integer([1, 3, "atenea"])
        with self.assertRaises(TypeError): max_integer(6)

    

    if __name__ == '__main__':
        unittest.main()
