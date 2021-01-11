# Stane, Danielle & Ramadan, Saba
# Lecture Section # 13
# Lab Assignment Number: 06

import unittest
from fold import *

class TestCases(unittest.TestCase):
   def test_1(self):
      t = [1, 2, 3, 4, 5]
      self.assertTrue(sum(t), 15)
      pass

   def test_2(self):
      t = [2, 4, 6, 8, 10]
      self.assertTrue(sum(t), 30)
      pass

   def test_3(self):
      t = [1, 2, 6, 8, 10]
      self.assertTrue(index_of_smallest(t), 0)
      pass

   def test_4(self):
      t = []
      self.assertFalse(index_of_smallest(t), -1)
      pass

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

