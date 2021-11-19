import unittest
from counting_letters import count_letters


class MyTestCase(unittest.TestCase):
    def test_count_letters(self):
        self.assertEqual(count_letters("Hello, world!"), "Vowels: 3, Consonants: 7")
        
        self.assertEqual(count_letters(""), "Vowels: 0, Consonants: 0")


if __name__ == '__main__':
    unittest.main()
