# Stane, Danielle & Ramadan, Saba
# Lecture Section# 13
# Lab Assignment Number: 06

import unittest
from string_101 import *

class TestString(unittest.TestCase):
   def test_lower1(self):
      string = 'hi'
      self.assertTrue(str_rot_13(string), 'uv')    
      pass

   def test_lower2(self):
      string = 'two'
      self.assertTrue(str_rot_13(string), 'dgb')    
      pass

   def test_lower3(self):
      string = 'hello'
      x = 'h'
      y = 'j'
      self.assertTrue(str_translate_101(string, x, y), 'jello')    
      pass

   def test_lower4(self):
      string = 'two'
      x = 'o'
      y = 'e'
      self.assertTrue(str_translate_101(string, x, y), 'twe')    
      pass

if __name__ == '__main__':
   unittest.main()

