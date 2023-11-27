# ROLLER COASTER
height = int(input("What is your height in cm?\n"))
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    photo = input("Do you want a photo?\n")
    if(age<12):
        if(photo == 'Yes'):
            print("Please pay 8$.")
        else:   
            print("Please pay 5$.")
    elif(age<=18):
        if(photo == 'Yes'):
            print("Please pay 10$.")
        else:   
            print("Please pay 7$.")
    elif(age>=45 and age<=55):
        print("Everything is going to be okay. Have a free ride with us.")
    else:
        if(photo == 'Yes'):
            print("Please pay 15$.")
        else:   
            print("Please pay 12$.")
else:
    print("Sorry, you have to grow taller before you can ride.") 
# ODD EVEN
num = int(input("Please enter a number:\n"))
if (num%2) == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
# BMI 2.0
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight/((height)**2))
if(bmi<18.5):
    print(f"Your BMI is {bmi}, you are underweight.")
elif(bmi<25):
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif(bmi<30):
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif(bmi<35):
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
# Leap Year
year = int(input("Please enter a year\n"))
if(year % 100 !=0):
    if(year%4 == 0):
        print("Leap year.")
    else:
        print("Not leap year.")
else:
    if(year%400 == 0):
        print("Leap year.")
    else:
        print("Not leap year.")
# Pizza order
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
if(size=='S'):
    bill = 15
    if(add_pepperoni=='Y'):
        bill+=2
    if(extra_cheese =='Y'):
        bill+=1
elif(size=='M'):
    bill = 20
    if(add_pepperoni=='Y'):
        bill+=3
    if(extra_cheese =='Y'):
        bill+=1
else:
    bill = 25
    if(add_pepperoni=='Y'):
        bill+=3
    if(extra_cheese =='Y'):
        bill+=1
print(f"Your final bill is: ${bill}.")
# Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1 = name1.lower()
name2 = name2.lower()
name1_count = name1.count('t')+name1.count('r')+name1.count('u')+name1.count('e')
name1_count2 = name1.count('l')+name1.count('o')+name1.count('v')+name1.count('e')
name2_count = name2.count('t')+name2.count('r')+name2.count('u')+name2.count('e')
name2_count2 = name2.count('l')+name2.count('o')+name2.count('v')+name2.count('e')
total_count1 = name1_count+name2_count
total_count2 = name1_count2+name2_count2
total_count = int(str(total_count1)+str(total_count2))
if(total_count<10 or total_count>90):
    print(f"Your score is {total_count}, you go together like coke and mentos.")
elif(total_count>=40 and total_count<=50):
    print(f"Your score is {total_count}, you are alright together.")
else:
    print(f"Your score is {total_count}.")
# Treasure Hunt  
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Hunt.")
print("Your mission is to find the treasure.") 
first_choice = input("You're at a hallway. Where do you want to go? Type 'Left' or 'Right'\n")
if(first_choice == 'Left'):
    second_choice = input("You come to a swimming pool. Do you jump or wait? Type 'Jump' or 'Wait'\n")
    if(second_choice=='Jump'):
        third_choice = input("You are underwater now. You see three chests on the poolbed.One red, one yellow, one purple. Which color do you choose?\n")
        if(third_choice=='red'):
            print("You encounter a snake! Game over.\n")
        elif(third_choice=='yellow'):
            print("You trigger a mine. Game over.\n")
        else:
            print("You have found the treasure. Congratulations, You win!\n")
    else:
        print("You have waited an eternity and now you are dead. Game over\n")
else:
    print("You encounter a beast, and now you are dead! Game over.\n") 