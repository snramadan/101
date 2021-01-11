# Project 2 - Moonlander
#
# Name: Saba Ramadan
# Instructor: M. Jani 

def showWelcome():
   print '\nWelcome aboard the Lunar Module Flight Simulator\n'
   print "   To begin you must specify the LM's initial altitude"
   print '   and fuel level.  To simulate the actual LM use'
   print '   values of 1300 meters and 500 liters, respectively.\n'
   print '   Good luck and may the force be with you!\n'

def getFuel():
   fuelAmount=input('Enter the initial amount of fuel on board the LM (in liters): ')
   while (fuelAmount<=0):
       print 'ERROR: Amount of fuel must be positive, please try again'
       fuelAmount=input('Enter the initial amount of fuel on board the LM (in liters): ')
   return fuelAmount

def getAltitude():
   altitude=input('Enter the initial altitude of the LM (in meters): ')
   while ((altitude<1) or (altitude>9999)):
       print 'ERROR: Altitude must be between 1 and 9999, inclusive, please try again'
       altitude=input('Enter the initial altitude of the LM (in meters): ')
   return altitude    

def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
   print 'Elasped Time: %4d s' % (elapsedTime)
   print '        Fuel: ', fuelAmount, 'l'
   print '        Rate:   ', fuelRate, 'l/s'
   print '    Altitude: %5.2f m' % (altitude)
   print '    Velocity: %7.2f m/s\n' % (velocity)


def getFuelRate(currentFuel):
   fuelrate=int(raw_input('Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): '))
   while ((fuelrate < 0) or (fuelrate > 9)):
       print 'ERROR: Fuel rate must be between 0 and 9, inclusive\n'
       fuelrate=int(raw_input('Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): '))
   if (fuelrate>currentFuel):
       fuelrate=currentFuel
   return fuelrate

def updateAcceleration(gravity, fuelRate):
   acceleration=gravity*((float(fuelRate)/5)-1)
   return acceleration
	
def updateAltitude(altitude, velocity, acceleration):
   altitudeX=altitude+velocity+(acceleration/2)
   return altitudeX

def updateVelocity(velocity, acceleration):
   velocityX=velocity+acceleration
   return velocityX

def updateFuel(fuel, fuelRate):
   fuelX=fuel-fuelRate
   return fuelX

def displayLMLandingStatus(velocity):
   if (velocity<0 and velocity>-1):
       print 'Status at landing - The eagle has landed!'
   if (velocity<-1 and velocity>-10):
       print 'Status at landing - Enjoy your oxygen while it lasts!'
   if (velocity<=-10):
       print 'Status at landing - Ouch - that hurt!'
