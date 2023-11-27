import random
import pi
random_integer = random.randint(1,100)
print(random_integer)
random_float = random.random()
print(random_float)
print(random_float * 5)
love_score = random.randint(1,100)
print(f"Your love score is {love_score}")
print(pi.pix)
# Coin Toss
coin = random.randint(0,1)
if(coin==1):
    print("Heads.")
else:
    print("Tails.")
# Lists
fruits = ['apple', 'banana', 'orange']
Divisions =['Dhaka', 'Rajshahi', 'Chittagong', 'Khulna', 'Sylhet', 'Rangpur', 'Barishal','Mymensingh']
print(Divisions[0])
Divisions.append("Cumilla")
Divisions.extend(["Namuland","Pinuland","Namupinuland"])
# Bankers roulette
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
length = len(names)
roulette = random.randint(0,length-1)
print(f"{names[roulette]} is going to buy the meal today!")
print(names)
# Treasure map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
map[int(position[1])-1][int(position[0])-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")
# ROCK PAPER SCISSORS
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = int(input("What do you choose?Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
compchoice = random.randint(0,2)
if(choice == 0):
    print(rock)
    if(compchoice == 0):
        print(f"Computer chose:\n{rock}")
        print("The game is ended by a draw")
    if(compchoice == 1):
        print(f"Computer chose:\n{paper}")
        print("You lose")
    if(compchoice == 2):
        print(f"Computer chose:\n{scissors}")
        print("You win!")
if(choice == 1):
    print(paper)
    if(compchoice == 1):
        print(f"Computer chose:\n{paper}")
        print("The game is ended by a draw")
    if(compchoice == 2):
        print(f"Computer chose:\n{scissors}")
        print("You lose")
    if(compchoice == 0):
        print(f"Computer chose:\n{rock}")
        print("You win!")
if(choice == 2):
    print(scissors)
    if(compchoice == 2):
        print(f"Computer chose:\n{scissors}")
        print("The game is ended by a draw")
    if(compchoice == 0):
        print(f"Computer chose:\n{rock}")
        print("You lose")
    if(compchoice == 1):
        print(f"Computer chose:\n{paper}")
        print("You win!")
        