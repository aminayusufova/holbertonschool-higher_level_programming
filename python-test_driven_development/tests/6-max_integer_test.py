#!/usr/bin/python3
"""Unit testing module for 6-max_integer_test.py
"""
import unittest
max_int = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Class for testing 6-max_integer_test.py
    """

    def test_max_integer(self):
        """Test case for a normal list of integers without negatives.
        """
        test_list = [1, 2, 3, 8, 4]
        self.assertEqual(max_int(test_list), 8)

    def test_max_integer_neg(self):
        """Test case for a normal list of integers with negatives.
        """
        test_list = [1, 2, 3, 8, 4, -40, -400, -12, 0]
        self.assertEqual(max_int(test_list), 8)

    def test_max_integer_empty(self):
        """Test case for an empty list.
        """
        self.assertEqual(max_int([]), None)

    def test_max_integer_end(self):
        """Test case for list where the maximum value is at the end.
        """
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_int(test_list), 5)

    def test_max_integer_one_element(self):
        """Test case for list with one element.
        """
        test_list = [42]
        self.assertEqual(max_int(test_list), 42)

    def test_max_integer_all_negatives(self):
        """Test case for list with all negative numbers.
        """
        test_list = [-1, -2, -3, -4]
        self.assertEqual(max_int(test_list), -1)

if __name__ == '__main__':
    unittest.main()
