import unittest
from divisible_by_5 import divisible_by_5


class MyTestCase(unittest.TestCase):
    def test_divisible_by_5(self):
        self.assertTrue(divisible_by_5(10))

        self.assertFalse(divisible_by_5(7))

        self.assertTrue(divisible_by_5(0))

        self.assertTrue(divisible_by_5(-5))


if __name__ == '__main__':
    unittest.main()
