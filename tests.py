import random
import unittest

from recursion import get_fib, recursive_factorial
from searching import binary_search
from sorting import bubble_sort



class BinarySearchTest(unittest.TestCase):

    def setUp(self):
        self.test_list = [1, 3, 9, 11, 15, 19, 29]

    def tearDown(self):
        del self.test_list

    def test_binary_search_in_list(self):
        search_result = binary_search(self.test_list, 15)
        self.assertEqual(search_result, 4)

    def test_binary_search_not_in_list(self):
        search_result = binary_search(self.test_list, 25)
        self.assertEqual(search_result, -1)


class RecursiveFactorialTest(unittest.TestCase):

    def test_recursive_factorial_zero(self):
        self.assertEqual(recursive_factorial(0), 1)

    def test_recursive_factorial_one(self):
        self.assertEqual(recursive_factorial(1), 1)

    def test_recursive_factorial_seven(self):
        self.assertEqual(recursive_factorial(7), 5040)


class RecursiveFibonacciTest(unittest.TestCase):

    def test_recursive_fibonacci_nine(self):
        self.assertEqual(get_fib(9), 34)

    def test_recursive_fibonacci_eleven(self):
        self.assertEqual(get_fib(11), 89)

    def test_recursive_fibonacci_zero(self):
        self.assertEqual(get_fib(0), 0)


class SortingTest(unittest.TestCase):

    def setUp(self):
        self.wrong_order = [random.randint(0, 100) for x in range(20)]

    def testDown(self):
        del self.wrong_order

    def test_bubble_sort(self):
        bubble_sort(self.wrong_order)
        start = 0
        terminus = len(self.wrong_order) - 1
        while start < terminus:
            self.assertGreaterEqual(
                self.wrong_order[terminus],
                self.wrong_order[start]
            )
            start += 1
            terminus -= 1


if __name__ == "__main__":
    unittest.main()
