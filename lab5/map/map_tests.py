import unittest
import map

class TestCases(unittest.TestCase):

   def test_1(self):
      t = [1, 2, 3]
      x = map.square_all(t)
      self.assertTrue(x, [1, 4, 9])
      pass

   def test_2(self):
      t = [2.0, 4.0, 6.1]
      x = map.square_all(t)
      self.assertTrue(x, [4.0, 16.0, 37.21])
      pass

   def test_3(self):
      t = [1, 2, 3]
      x = 1
      a = map.add_n_all(x, t)
      self.assertTrue(x, [2, 3, 4])
      pass

   def test_4(self):
      t = [2.0, 4.0, 6.1]
      x = 2
      a = map.add_n_all(x, t)
      self.assertTrue(x, [4.0, 6.0, 8.1])
      pass

   def test_5(self):
      t = [1, 2, 3]
      x = map.even_or_odd_all(t)
      self.assertTrue(x, [False, True, False])
      pass

   def test_6(self):
      t = [2, 4, 6]
      x = map.even_or_odd_all(t)
      self.assertTrue(x, [True, True, True])
      pass

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

