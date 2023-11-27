print("Hello"[0])
print(123_332_532+345)
print(2232.423*2)
print(False - True)
name_char=len(input("What is your name?\n"))
print("Your name has "+ str(name_char) + " characters.")
# The following program will add the digits of a user given
# 2 digit number.
x = str(input("Please enter a number:\n"))
print(int(x[0])+int(x[1]))
# PEMDAS
print(3*3+3/3-3)
print(3*(3+3)/3-3)
# BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
print(int(float(weight)/(float(height)**2)))
# rounding
print(round(8/3,3))
# fstrings
score = 0
height = 1.8    
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
# Life in Weeks
age = int(input("What is your current age? "))
year = 90 - age
months = year * 12
weeks = year * 52
days = year * 365
print(f"You have {days} days, {weeks} weeks, and {months} months left")
# Tip Calculator
print("Welcome to the tip calculator")
bill = float(input("What was the total bill?\n"))
percentage = float(input("What percentage tip would you like to give?\n"))
people = float(input("How many people to split the bill?\n"))
ppbill = round((bill + (bill * (percentage/100)))/people,2)
print(f"Each person should pay: ${ppbill}")

