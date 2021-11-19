import unittest
import math
from sphere import volume_of_sphere


class MyTestCase(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(volume_of_sphere(2), (4/3) * math.pi * (1**3))
        self.assertEqual(volume_of_sphere(0), 0)
        self.assertEqual(volume_of_sphere(-1), 0)


if __name__ == '__main__':
    unittest.main()
