import unittest
from count_word import *


class MyTestCase(unittest.TestCase):
    def test_remove_punctuation(self):
        self.assertEqual(remove_punctuation("test!?."), "test")

    def test_count_word(self):
        self.assertEqual(count_word("This is a test. Test the word 'test'!", "test"),
                         "The word test was found 3 time(s).")

        self.assertEqual(count_word("Hello, world!", "test"),
                         "The word test was found 0 time(s).")


if __name__ == '__main__':
    unittest.main()
