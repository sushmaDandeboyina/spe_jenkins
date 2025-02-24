import unittest

from Prog1 import summation

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [20, 36]
        result = summation(data)
        self.assertEqual(result, 56)

if __name__ == '__main__':
    unittest.main()
