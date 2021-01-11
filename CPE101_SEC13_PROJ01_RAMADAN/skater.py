#Project 1

#Name: Saba Ramadan
#Instructor: M. Jani
#Section: 13

import math
import funcs

def main():
    weight=raw_input('How much do you weigh (pounds)? ')

    distance=raw_input('How far away is your professor (meters)? ')

    object=raw_input('Will you throw a rotton (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ')
    
    print ('')

    massObject=funcs.getMassObject(object)

    Distance=float(distance)

    if (massObject <= 0.1):
        print "Nice throw! You're going to get an F!"
    if (0.1 < massObject <= 1.0): 
        print 'Nice throw! Make sure your professor is OK.'
    if (massObject > 1.0 and Distance <20):
        print 'Nice throw! How far away is the hospital?'
    if (massObject > 1.0 and Distance >= 20): 
        print 'Nice throw! RIP professor.'
    
    massSkater=funcs.poundsToKG(float(weight))
    
    velocityObject=funcs.getVelocityObject(Distance)
    
    velocitySkater=funcs.getVelocitySkater(massSkater, massObject, velocityObject)
    print 'Velocity of skater: ', round(velocitySkater, 3), 'm/s'

    if (velocitySkater < 0.2):
        print 'My grandmother skates faster than you!'
    if (0.2 < velocitySkater < 1.0):
        print none
    if (velocitySkater >= 1.0):
        print 'Look out for that railing!!!'

if __name__ == '__main__':
   main()
