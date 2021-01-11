#Project 1

#Name: Saba Ramadan
#Instructor: M. Jani
#Section: 13

import unittest
import funcs

class TestCases(unittest.TestCase):
   def test1(self):
       pounds=100
       self.assertAlmostEqual(funcs.poundsToKG(pounds), 45.3592)
       pass
   def test2(self):
       pounds=120
       self.assertAlmostEqual(funcs.poundsToKG(pounds), 54.43104)
       pass
   def test3(self):
       object='t'
       self.assertTrue(funcs.getMassObject(object), 0.1)
       pass
   def test4(self):
       object='p'
       self.assertTrue(funcs.getMassObject(object), 1.0)
       pass
   def test5(self):
       object='r'
       self.assertTrue(funcs.getMassObject(object), 3.0)
       pass
   def test6(self):
       object='g'
       self.assertTrue(funcs.getMassObject(object), 5.3)
       pass
   def test7(self):
       object='l'
       self.assertTrue(funcs.getMassObject(object), 9.07)
       pass 
   def test8(self):
       object='s'
       self.assertFalse(funcs.getMassObject(object), 0.0)
       pass
   def test9(self):
       distance=12
       self.assertAlmostEqual(funcs.getVelocityObject(distance), 7.6681158)
       pass
   def test10(self):
       distance=10
       self.assertEqual(funcs.getVelocityObject(distance), 7) 
       pass
   def test11(self):
       massSkater=100
       massObject=150
       velocityObject=50
       self.assertEqual(funcs.getVelocitySkater(massSkater, massObject, velocityObject), 75)
       pass
   def test12(self):
       massSkater=200
       massObject=260
       velocityObject=30
       self.assertEqual(funcs.getVelocitySkater(massSkater, massObject, velocityObject), 39)
       pass

if __name__ == '__main__':
   unittest.main()    
