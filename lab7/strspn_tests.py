# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Assignment Number: 07

import unittest
from strspn import *

class TestCases(unittest.TestCase):

    def test1(self):
        str1 = 'calpoly'
        str2 = 'california'
        self.assertEqual(my_strspn(str1, str2), 3)
        pass

    def test2(self):
        str1 = 'cccca'
        str2 = 'office'
        self.assertEqual(my_strspn(str1, str2), 4)
        pass

    def test3(self):
        str1 = 'ant'
        str2 = 'and'
        self.assertEqual(my_strspn(str1, str2), 2)
        pass

    def test4(self):
        str1 = 'try'
        str2 = 'hope'
        self.assertEqual(my_strspn(str1, str2), 0)
        pass

# Run the unit tests
if __name__ == '__main__':
   unittest.main()
