#Stane, Danielle & Ramadan, Saba
#Lecture Section #13
#Lab Assignment Number: 03

import unittest
import logic

class TestCases(unittest.TestCase):
   def test_case1(self):
       x=2
       self.assertTrue(logic.is_even(x), True)
       pass
   def test_case2(self):
       x=5
       self.assertFalse(logic.is_even(x), False)
       pass
   def test_case3(self):
       x=2
       self.assertTrue(logic.in_an_interval(x), True)
       pass
   def test_case4(self):
       x=4
       self.assertTrue(logic.in_an_interval(x), True)
       pass   
   def test_case5(self):
       x=11
       self.assertFalse(logic.in_an_interval(x), False)
       pass
   def test_case6(self):
       x=50
       self.assertTrue(logic.in_an_interval(x), True)
       pass
   def test_case7(self):
       x=93
       self.assertFalse(logic.in_an_interval(x), False)
       pass
   def test_case8(self):
       x=12
       self.assertFalse(logic.in_an_interval(x), False)
       pass
   def test_case9(self):
       x=19
       self.assertTrue(logic.in_an_interval(x), True)
       pass
   def test_case10(self):
       x=102
       self.assertTrue(logic.in_an_interval(x), True)
       pass
   def test_case11(self):
       x=104
       self.assertFalse(logic.in_an_interval(x), False)
       pass
   def test_case12(self):
       x=101
       self.assertTrue(logic.in_an_interval(x), True)
       pass
   def test_case13(self):
       x=103
       self.assertTrue(logic.in_an_interval(x), True)
       pass

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

