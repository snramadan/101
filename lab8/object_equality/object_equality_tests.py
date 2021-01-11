# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Assignment Number: 08

import unittest
from objects import *

class TestCases(unittest.TestCase):
   def test_equality1(self):
      self1 = Point(2.0, 3.0)
      other1 = Point(2.0, 3.0)     
      self.assertEqual(Point.__eq__(self1, other1), True)
      pass

   def test_equality2(self):
      self1 = Point(2.0, 3.0)
      other1 = Point(6.0, 7.0)     
      self.assertEqual(Point.__eq__(self1, other1), False)
      pass
 
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

