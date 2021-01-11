# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Assignment Number: 09

import unittest
from groups import *

class TestCases(unittest.TestCase):

    def test1(self):
        x = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(groups_of_3(x), [[1,2,3], [4,5,6], [7,8,9]])
        pass 
    
    def test2(self):
        x = [1,2,3,4,5,6,7]
        self.assertEqual(groups_of_3(x), [[1,2,3], [4,5,6], [7]])
        pass 

# unitest cases
if __name__ == '__main__':
   unittest.main()
