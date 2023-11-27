import random
import string 
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
# Average height
student_heights = input("Input a list of student heights ").split()
sum = 0
count = 0
for height in student_heights:
    sum += int(height)
    count+=1
print(round(sum/count))
# Highest Score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
max = student_scores[0]
for score in student_scores:
    if(score>max):
        max = score
print(f"The highest score in the class is: {max}")
# range function
sum = 0     
for number in range(1,101):
    sum+=number
print(sum)
# Even number
sum = 0
for number in range(1,101):
    if(number%2==0):
        sum+=number
print(sum)
# FizzBuzz game
for number in range(1,101):
    if (number%3 != 0 and number%5 != 0):
        print(number)
    if (number%3==0):
        if(number%5==0):
            print("FizzBuzz")
        else:
            print("Fizz")
    if (number%5==0 and number%3!=0):
        print("Buzz")
# Password Generator
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
listall = []
listpassword = []
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
for letter in range(0,nr_letters):
    letter1 = chr(random.randint(ord('a'),ord('z')))
    letter2 = chr(random.randint(ord('A'),ord('Z')))
    letter = [letter1,letter2]
    listall.append(letter[random.randint(0,1)])
for symbol in range(0,nr_symbols):
    symbol = symbols[random.randint(0,len(symbols)-1)]
    listall.append(symbol)
for number in range(0,nr_numbers):
    number = random.randint(0,9)
    listall.append(number)
for all in range(0,len(listall)):
    all = listall[random.randint(0,len(listall)-1)]
    listpassword.append(all)
for char in listpassword:
    print(char,end="")