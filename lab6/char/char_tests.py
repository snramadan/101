# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Assignment Number: 06

import unittest
from char import *

class TestChar(unittest.TestCase):

   def test_lower1(self):
      t = 'd'
      self.assertTrue(is_lower_101(t), True)
      pass

   def test_lower2(self):
      t = 'A'
      self.assertFalse(is_lower_101(t), False)
      pass

   def test_rot3(self):
      char = 'a'
      self.assertTrue(char_rot_13(char), 'n')
      pass

   def test_rot4(self):
      char = 'N'
      self.assertTrue(char_rot_13(char), 'A')
      pass

if __name__ == '__main__':
   unittest.main()
