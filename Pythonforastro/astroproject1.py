#this program turns celestial coordinates into degree coordinates

def hms2deg(hours,minutes,seconds):
    deg = (hours  + (minutes / 60) + (seconds / 3600))*15
    return deg

def dms2deg(degrees,minutes,seconds):
    if(degrees<0):
        deg = -(-degrees + (minutes / 60) + (seconds / 3600))
    else:
        deg = -(degrees + (minutes / 60) + (seconds / 3600))
    return deg

print("Please enter the right ascension coordinates:")
hours = float(input("Please enter the hours coordinate:"))
while(hours<0 or hours>24):
    hours=float(input("Please enter a value between 0 and 24:"))
minutes = float(input("Please enter the minutes coordinate:"))
seconds = float(input("Please enter the seconds coordinate:"))

print("Please enter the declination coordinates:")
degrees = float(input("Please enter the degrees coordinate:"))
minutes = float(input("Please enter the minutes coordinate:"))
seconds = float(input("Please enter the seconds coordinate:"))

ascension= hms2deg(hours,minutes,seconds)
declination= dms2deg(degrees,minutes,seconds)

print(f"ascension is {ascension} degrees and declination is {declination} degrees")