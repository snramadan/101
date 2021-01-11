# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Assignment Number: 08

import unittest
from list_comp import*
from objects import*

class TestCases(unittest.TestCase):
   def test_1(self):
      list1 = [Point(3.0, 4.0), Point(0.0, 6.0)]
      self.assertEqual(distance_all(list1), [5.0, 6.0])
      pass
   
   def test_2(self):
      list1 = [Point(3.0, 4.0), Point(0.0, 0.0)]
      self.assertEqual(distance_all(list1), [5.0, 0.0])
      pass

   def test_3(self):
      list1 = [Point(3.0, 4.0), Point(0.0, -6.0)]
      self.assertEqual(are_in_first_quadrant(list1), [Point(3.0, 4.0)])
      pass

   def test_4(self):
      list1 = [Point(2.0, 3.0), Point(1.0, 0.0)]
      self.assertEqual(are_in_first_quadrant(list1), [Point(2.0, 3.0), Point(1.0, 0.0)])
      pass

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

