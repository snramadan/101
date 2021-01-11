#Project 2-Moonlander
#
#Name: Saba Ramadan
#Instructor: M. Jani

import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   def test1(self):
      gravity=1.62
      fuelRate=0
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)
      pass
   def test2(self):
      gravity=1.62
      fuelRate=5
      self.assertAlmostEqual(updateAcceleration(1.62, 5), 0)
      pass
   def test3(self):
      altitude=1
      velocity=1
      acceleration=2
      self.assertAlmostEqual(updateAltitude(1, 1, 2), 3)
      pass
   def test4(self):
      altitude=2
      velocity=2
      acceleration=4
      self.assertAlmostEqual(updateAltitude(2, 2, 4), 6)
      pass
   def test5(self):
      velocity=10
      acceleration=20
      self.assertAlmostEqual(updateVelocity(10, 20), 30)
      pass
   def test6(self):
      velocity=100
      acceleration=200
      self.assertAlmostEqual(updateVelocity(100, 200), 300)
      pass
   def test7(self):
      fuel=150
      fuelRate=50
      self.assertAlmostEqual(updateFuel(150, 50), 100)
      pass
   def test8(self):
      fuel=50
      fuelRate=20
      self.assertAlmostEqual(updateFuel(50, 20), 30)
      pass

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

