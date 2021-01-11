# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Assignent Number: 08

from math import *
from objects import *

def distance(point1, point2):
    distance = sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
    return distance

def circles_overlap(circle1, circle2):
    return (distance(circle1.center, circle2.center)) < (circle1.radius + circle2.radius)
