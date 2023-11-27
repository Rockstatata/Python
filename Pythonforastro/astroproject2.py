#this program calculates the angular distance between two stars

import math as m

def hms2deg(hours,minutes,seconds):
    deg = (hours  + (minutes / 60) + (seconds / 3600))*15
    return deg

def dms2deg(degrees,minutes,seconds):
    if(degrees<0):
        deg = -(-degrees + (minutes / 60) + (seconds / 3600))
    else:
        deg = (degrees + (minutes / 60) + (seconds / 3600))
    return deg

def angular_distance(ascension1,declination1,ascension2,declination2): 
    angdist = 2*m.asin(m.sqrt((m.sin((abs(declination1-declination2))/2))**2+(m.cos(declination1))*(m.cos(declination2))*(m.sin(abs(ascension1-ascension2)/2)**2)))
    return angdist

print("Please enter the first star's right ascension coordinates:") 
hours1 = float(input("Please enter the hours coordinate:"))
while(hours1<0 or hours1>24):
    hours1=float(input("Please enter a value between 0 and 24:"))
minutes1 = float(input("Please enter the minutes coordinate:")) 
seconds1 = float(input("Please enter the seconds coordinate:"))

print("Please enter the first star's declination coordinates:") 
degrees1 = float(input("Please enter the degrees coordinate:")) 
minutes2 = float(input("Please enter the minutes coordinate:")) 
seconds2 = float(input("Please enter the seconds coordinate:"))

print("Please enter the second star's right ascension coordinates:") 
hours2 = float(input("Please enter the hours coordinate:")) 
while(hours2<0 or hours2>24):
    hours2=float(input("Please enter a value between 0 and 24:"))
minutes3 = float(input("Please enter the minutes coordinate:")) 
seconds3 = float(input("Please enter the seconds coordinate:"))

print("Please enter the second star's declination coordinates:") 
degrees2 = float(input("Please enter the degrees coordinate:")) 
minutes4 = float(input("Please enter the minutes coordinate:")) 
seconds4 = float(input("Please enter the seconds coordinate:"))

ascension1= hms2deg(hours1,minutes1,seconds1) 
declination1= dms2deg(degrees1,minutes2,seconds2) 
ascension2= hms2deg(hours2,minutes3,seconds3) 
declination2= dms2deg(degrees2,minutes4,seconds4)

angdist = angular_distance(ascension1,declination1,ascension2,declination2)

print(f"The angular distance between two stars is {angdist}")