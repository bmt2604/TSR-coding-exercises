import unittest
from leap_year import leap_year


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertTrue(leap_year(2024))

        self.assertFalse(leap_year(2021))

        self.assertFalse(leap_year(2100))


if __name__ == '__main__':
    unittest.main()
