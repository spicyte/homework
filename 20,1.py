import unittest

def add_number(a, b):
    return a + b

class TestAddNumber(unittest.TestCase):
    def test_add_number(self):
        self.assertEqual(add_number(10, 5), 15)
        self.assertEqual(add_number(-10, -5), -15)  # Исправлено знак числа
        self.assertEqual(add_number(-10, 5), -5)

if __name__ == '__main__':
    unittest.main()
