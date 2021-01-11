#Stane, Danielle & Ramadan, Saba
#Lecture Section #13
#Lab Assignment Number:03

import unittest
import conditional

class TestCases(unittest.TestCase):
   def test1(self):
      x=1
      y=2
      self.assertTrue(conditional.max_101(x,y), 2)
      pass
   def test2(self):
      x=5
      y=3
      self.assertTrue(conditional.max_101(x,y), 5)
      pass
   def test3(self):
      x=4.2
      y=2.4
      z=3.6
      self.assertTrue(conditional.max_of_three(x,y,z), 4.2)
      pass
   def test4(self):
      x=2.6
      y=6.4
      z=4.9
      self.assertTrue(conditional.max_of_three(x,y,z), 6.4)
      pass
   def test5(self):
      x=2.2
      y=3.5
      z=8.6
      self.assertTrue(conditional.max_of_three(x,y,z), 8.6)
      pass
   def test6(self):
      x=0
      self.assertEqual(conditional.rental_late_fee(x), 0)
      pass
   def test7(self):
      x=6
      self.assertEqual(conditional.rental_late_fee(x), 5)
      pass
   def test8(self):
      x=10
      self.assertEqual(conditional.rental_late_fee(x), 7)
      pass
   def test9(self):
      x=20
      self.assertEqual(conditional.rental_late_fee(x), 19)
      pass
   def test10(self):
      x=45
      self.assertEqual(conditional.rental_late_fee(x), 100)
      pass


#Run the unit tests.
if __name__ == '__main__':
   unittest.main()

