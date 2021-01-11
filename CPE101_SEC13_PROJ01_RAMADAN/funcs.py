#Project 1

#Name: Saba Ramadan
#Instructor: M. Jani
#Section: 13

import math

def poundsToKG(pounds):
    kilograms=pounds*0.453592
    return kilograms

def getMassObject(object):
    if object == 't':
        return 0.1
    elif object == 'p':
        return 1.0
    elif object == 'r':
        return 3.0
    elif object == 'g':
        return 5.3
    elif object == 'l':
        return 9.07
    else:
        return 0.0

def getVelocityObject(distance):
    gravity=9.8  
    velocityObject=math.sqrt((gravity*distance)/2)
    return velocityObject

def getVelocitySkater(massSkater, massObject, velocityObject):
    velocitySkater=((massObject*velocityObject)/massSkater)
    return velocitySkater     
