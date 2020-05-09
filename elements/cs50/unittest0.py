from unittest import TestCase

from prime import is_prime

class Tests(unittest.TestCase):

    def test_1(self):
        self.assertFalse(is_prime(1))

    def test_2(self):
        self.assertFalse(is_prime(8))

    def test_3(self):
        self.assertFalse(is_prime(2))

if __name__ == "__main__":
    unittest.main()