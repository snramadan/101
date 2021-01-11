# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Assignment Number: 09

import unittest
from parse_file import *

class TestCases(unittest.TestCase):

    def test1(self):
        f = 'test0.txt'
        self.assertEqual(main(f), (2, 3, 4))
        pass
    
    def test2(self):
        f = 'test1.txt'
        self.assertEqual(main(f), (2, 3, 4))
        pass
 
# unittest cases
if __name__ == '__main__':
   unittest.main()
