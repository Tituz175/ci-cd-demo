import unittest
from main import Calculator

c = Calculator()

class TestMain(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(c.add(3, 7), 10)
        self.assertEqual(c.add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(c.sub(7, 1), 6)
        self.assertEqual(c.sub(-1, -1), 0)

if __name__ == "__main__":
    unittest.main()
