
import unittest


def add(a, b):
    return a + b


class TestDemo(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
