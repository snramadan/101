# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Assignment Number: 08

from objects import*
from math import*

def distance_all(list1):
    return [sqrt(((point.x-0.0)**2)+((point.y-0.0)**2)) for point in list1]

def are_in_first_quadrant(list1):
    return [p1 for p1 in list1 if p1.x>=0 and p1.y>=0]
