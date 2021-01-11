# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Assigment Number: 08

from utility import *

class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __eq__(self, other):
        if ((epsilon_equal(self.x, other.x)) and (epsilon_equal(self.y, other.y))):
            return True
        else:
            return False

class Circle(object):
    def __init__(self, center = 0, radius = 0):
        self.center = center
        self.radius = radius
