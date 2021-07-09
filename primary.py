# author: <name here>
# date: <date here>

# -------------------- Section 1 -------------------- #

# Input | Saving String Responses to Variables

# Objectives:
#   1. Name in Reverse
#       a. Prompts input from the user in the form of a first name and last name.
#           Save these values to variables first_name and last_name.
#       b. Print the first and last names in reverse order.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> first name... elia
#   >> last name... deppe
#   deppe, elia
#
# ---- WRITE CODE BELOW ---- #
first_name = input("enter your first name: ")
last_name = input("enter your last name: ")

print(last_name + ",",first_name + "\n")

#   2. Pyramid
#       a. Prompt input from the user in the form of a single character. Save to a variable named symbol.
#       b. Using the symbol, create a pyramid like you see in the example output. (Think, how can you make
#           duplicates of text symbol?)
#
# ----- EXAMPLE OUTPUT ----- #
#   >> $
#
#   $
#   $$
#   $$$
#   $$
#   $
#
# ---- WRITE CODE BELOW ---- #
symbol = input('enter a symbol: ')

print(symbol)
print(symbol*2)
print(symbol*3)
print(symbol*2)
print(symbol + "\n")
#   3. Parallelogram
#       a. Prompt input from the user in the form of a single character. Save to a variable named symbol.
#       b. Using the symbol, create a pyramid like you see in the example output. (Think, how can you make
#           duplicates of text symbol?)
#
# ----- EXAMPLE OUTPUT ----- #
#   >> @
#
#   @
#   @@
#   @@@
#   @@@@
#    @@@
#     @@
#      @
#
# ---- WRITE CODE BELOW ---- #
new_symbol = input('symbol >> ')
print(' '*1,new_symbol)
print(' '*1,new_symbol*2)
print(' '*1,new_symbol*3)
print(' '*1,new_symbol*4)
print(' '*2, new_symbol*3)
print(' '*3, new_symbol*2)
print(' '*4, new_symbol)
# -------------------- Section 2 -------------------- #

# Casting | Getting Integers and Floats from the User

# Objectives:
#   1. Comparison
#       a. Prompt the user to enter a number, and save it to a variable named num1. DO NOT CAST IT.
#       b. Prompt the user to enter a number, and save it to a variable named num2. CAST IT TO AN INTEGER.
#       c. Prompt the user to enter a number, and save it to a variable named num3. CAST IT TO A FLOAT.
#       d. Print out each variable multiplied by 10.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> num1... 45
#   >> num2... -132.45
#   >> num3... 2132.24
#
#   num1 (str)   | 45454545454545454545
#   num2 (int)   | -1320
#   num3 (float) | 21322.4
#
# ---- WRITE CODE BELOW ---- #
num1 = input('enter a num: ')
num2 = int(input('enter num: '))
num3 = float(input('enter a num: '))

print(num1*10)
print(num2*10)
print(num3*10)


# Objectives:
#   2. Diameter of a Circle
#       a. Prompt input from the user to enter a radius. Save this value to a
#           variable named num as an integer or float.
#       b. Compute the diameter, and print it to the user.
#           diameter = radius * 2
#
# ----- EXAMPLE OUTPUT ----- #
#   >> radius... 12.3
#
#   diameter = 24.6
#
# ---- WRITE CODE BELOW ---- #
radius = int(input('Enter a radius: '))
diameter = radius * 2
print(diameter)

# Objectives:
#   3. Area of a Circle
#       a. Define a function named area_circle(). Accept the parameters listed below.
#           Name   | Type(s)         | Description
#           radius | Integer / Float | The radius of the circle.
#
#           The function should compute the area of a circle, and print it to the terminal.
#               area = 3.14 * radius ** 2
#       b. Prompt input from the user to enter a radius. Save this value to a
#           variable named num as an integer or float.
#       c. Compute the radius by calling the function area_circle(), sending num as a parameter.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> radius... 44.2
#
#   area of the circle: 6134.4296
#
# ---- WRITE CODE BELOW ---- #
def area_circle(num):
    area = 3.14 * num ** 2 
num = float(input('enter a radius: ') )
area = area_circle(num)
print(area) 
# -------------------- Section 4 -------------------- #
#
# Create a conversation with a faux (fake) AI, using input and print().
# See the example in example.py
name = input("What's your name? ")
print('Hello!', name)
fav_color = input("what is your favorite color? ")
print("Ok, Cool. I don't have a favorite color because I love all of the colors equally.")
fav_holiday = input("What is your favorite holoday? ")
print("Oh wow that's nice my favorite holiday is Thanksgiving because we spend time with our families and have so much fun!")
fav_season = input("What is your favorite season? ")
print("That's nice I love the summer because  ")
feeling = input('How are you feeling today! ')
print('Ok, today try to be and feel the best you can! ')
tv_show = input('What is your favorite tv show? ')
print('Oh yeah, that is a good one!')
siblings = input('do you have siblings? ')
print("If you do then I hope that they are fun to hang around and if you don't I bet you are having so much fun with your parents.")
siblings_num = int(input("How many siblings do you have? "))
print("oh wow you will have so much fun with your family!")
print('Have a great day!! It was nice to talk to you! Bye!')
bye = input("enter any message to the AI. >> ")