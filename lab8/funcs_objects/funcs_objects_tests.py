# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Section Number: 08

import unittest
from objects import *
from funcs_objects import *

class TestCases(unittest.TestCase):
   def test_point1(self):
      p = Point(2, 3)
      self.assertEqual(p.x, 2)
      self.assertEqual(p.y, 3)
      pass

   def test_point2(self):
      p = Point(4, 8)
      self.assertEqual(p.x, 4)
      self.assertEqual(p.y, 8)
      pass

   def test_circle1(self):
      center = Point(2, 3)
      c = Circle(center, 8)
      self.assertEqual(c.center.x, 2)
      self.assertEqual(c.center.y, 3)
      self.assertEqual(c.radius, 8)
      pass

   def test_circle2(self):
      center = Point(4, 5)
      c = Circle(center, 9)
      self.assertEqual(c.center.x, 4)
      self.assertEqual(c.center.y, 5)
      self.assertEqual(c.radius, 9)
      pass

   def test_distance1(self):
      point1 = Point(1.0, 1.0)
      point2 = Point(4.0, 5.0)
      self.assertEqual(distance(point1, point2), 5.0)
      pass

   def test_distance2(self):
      point1 = Point(0, 0)
      point2 = Point(3.0, 4.0)
      self.assertEqual(distance(point1, point2), 5.0)
      pass

   def test_circles_overlap1(self):
      circle1 = Circle(Point(0.0, 1.0), 3.0)
      circle2 = Circle(Point(1.0, 2.0), 2.0)
      self.assertTrue(circles_overlap(circle1, circle2), True)
      pass

   def test_circles_overlap2(self):
      circle1 = Circle(Point(0.0, 1.0), 2.0)
      circle2 = Circle(Point(7.0, 10.0), 3.0)
      self.assertFalse(circles_overlap(circle1, circle2), False)
      pass

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

