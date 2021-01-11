#Stane, Danielle & Ramadan, Saba
#Lecture Section #13
#Lab Assignment Number:02

import unittest
import funcs

class TestCases(unittest.TestCase):
   def test_f_1(self):
       x=1
       self.assertEqual(funcs.f(x), 9)
       pass

   def test_f_2(self):
       x=-1
       self.assertEqual(funcs.f(x), 5)      
       pass

   def test_g_3(self):
       x=1.0
       y=0
       self.assertAlmostEqual(funcs.g(x,y), 0.33333333333)
       pass

   def test_g_4(self):
       x=-1.0
       y=1
       self.assertAlmostEqual(funcs.g(x,y), -0.6666666667)
       pass

   def test_c_5(self):
      a=3
      b=4
      self.assertEqual(funcs.hypotenuse(a,b), 5)
      pass

   def test_c_7(self):
      a=30
      b=40
      self.assertEqual(funcs.hypotenuse(a,b), 50)
      pass

   def test_x_8(self):
      x=1
      self.assertTrue(funcs.is_positive(x), True)
      pass

   def test_x_9(self):
      x=-1
      self.assertFalse(funcs.is_positive(x), False)
      pass

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

