import unittest
import filter

class TestCases(unittest.TestCase):

   def test_1(self):
      t = [-1, 0, 1, 2, 3]
      self.assertTrue(filter.are_positive(t), [0, 1, 2, 3])
      pass

   def test_2(self):
      t = [-2, -1, -3, 0, 5]
      self.assertTrue(filter.are_positive(t), [0, 5])
      pass

   def test_3(self):
      t = [1, 2, 6, 7, 8]
      n = 5
      self.assertTrue(filter.are_greater_than_n(n, t), [6, 7, 8])
      pass

   def test_4(self):
      t = [-3, -2, -1, 0, 5]
      n = 1
      self.assertTrue(filter.are_greater_than_n(n, t), [5])
      pass

   def test_5(self):
      t = [1, 2, 6, 7, 8]
      n = 2
      self.assertTrue(filter.are_divisible_by_n(n, t), [2, 6, 8])
      pass

   def test_6(self):
      t = [2, 5, 6, 8, 9]
      n = 3
      self.assertTrue(filter.are_divisible_by_n(n, t), [6, 9])
      pass

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

