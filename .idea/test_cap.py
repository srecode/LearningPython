import unittest
import cap

class TestCap(unittest.TestCase):
    def test_one_word(self):
        s = 'python'
        result = cap.cap_string(s)
        self.assertEqual(result, 'Python')

    def test_multi_word(self):
        s = 'monty python'
        result = cap.cap_string(s)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()