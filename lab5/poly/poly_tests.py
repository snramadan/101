import unittest
import poly

class TestPoly(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)
   
   def test_case1(self):
      poly1 = [2, 3, 4]
      poly2 = [5, 6, 7]
      x = poly.poly_add2(poly1, poly2)
      self.assertListAlmostEqual(x, [7, 9, 11])
      pass

   def test_case2(self):
      poly1 = [3.1, 2.1, 4.1]
      poly2 = [1.2, 3.2, 4.2]
      x = poly.poly_add2(poly1, poly2)
      self.assertListAlmostEqual(x, [4.3, 5.3, 8.3])
      pass

   def test_case3(self):
      poly1 = [1, 1, 1]
      poly2 = [2, 2, 2]
      x = poly.poly_mult2(poly1, poly2)
      self.assertListAlmostEqual(x, [2, 4, 6, 4, 2])
      pass

   def test_case4(self):
      poly1 = [1, 2, 2]
      poly2 = [2, 1, 3]
      x = poly.poly_mult2(poly1, poly2)
      self.assertListAlmostEqual(x, [6, 8, 9, 5, 2])
      pass

if __name__ == '__main__':
   unittest.main()
