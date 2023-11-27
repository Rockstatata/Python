print('Day 1 - Python Print Function\nThe function is declared like this:\nprint("What to print")')
print("Hello"+" "+"Pianto")
#The line below gets executed like this: First the 'Hello' is converted to string, then the
#is executed. In the input function the prompt will be printed and the input will be
#taken as another string. After that all the strings will be concatenated with each
#other and printed as a whole string.
print('Hello'+' '+input("What is your name?: ")+'!')
#The following code gets executed like this:First the input is taken. After that the
#whole input function returns only the given input by the user, which passes through
#the len function.The len function gets executed and returns the length of the string
#which the input function returns.Then it gets printed to the console.
print(len(input("What is your name?\n")))
name = input("What's your name?\n")
print(len(name))
#The following program swaps the values of a and b at once.
a = input(":")
b = input(":")
a,b=b,a
a,b=b,a
temp=a
a=b
b=temp
print(f"a = {a}")
print(f"b = {b}")
### BAND NAME GENERATOR
print("Hello "+input())
city = input("What is the city that you grew up in?\n")
pet = input("What is the name of your pet?\n")
print("Your band name could be "+city + " " + pet)

