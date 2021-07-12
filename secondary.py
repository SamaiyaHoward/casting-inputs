# author: <Samaiya Howard>
# date: <7/6/21>

# -------------------- Section 4 -------------------- #

# Input | ASCII Art


# Objectives:
#   1. Diamond
#       a. Define a function that accept the parameters listed below.
#           Name   | Type(s)         | Description
#           symbol | Integer / Float | The symbol used to create the diamond.
#
#           The function should print the chevron seen in the output below using the symbol.
#       b. Prompt input from the user in the form of a single character, save it to a variable.
#       c. Call the function you defined to create the diamond, sending the character as an argument.
#
#       HINT: Start with a smaller diamond! Then make it bigger once you figure out the pattern.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> $
#
#           $
#          $$$
#         $$$$$
#        $$$$$$$
#       $$$$$$$$$
#      $$$$$$$$$$$
#     $$$$$$$$$$$$$
#      $$$$$$$$$$$
#       $$$$$$$$$
#        $$$$$$$
#         $$$$$
#          $$$
#           $
#
# ---- WRITE CODE BELOW ---- #
symbol1 = input('Enter a symbol: ')
print(' '*10,symbol1*1)
print(' '*9,symbol1*3)
print(' '*8,symbol1*5)
print(' '*7,symbol1*7)
print(' '*6,symbol1*9)
print(' '*5,symbol1*11)
print(' '*4,symbol1*13)
print(' '*5,symbol1*11)
print(' '*6,symbol1*9)
print(' '*7,symbol1*7)
print(' '*8,symbol1*5)
print(' '*9,symbol1*3)
print(' '*10,symbol1*1)

#   2. Framed Diamond
#       a. Define a function that accept the parameters listed below.
#           Name   | Type(s)         | Description
#           symbol1 | Integer / Float | The symbol used to create the diamond.
#           symbol2 | Integer / Float | The symbol used to create the frame.
#
#           The function should print the chevron seen in the output below using the symbol.
#       b. Prompt input from the user in the form of a single character, save it to a variable.
#       c. Prompt input from the user in the form of a single character again, and save it to a second variable.
#       d. Call the function you defined to create the framed diamond, sending the characters as arguments.
#
#       HINT: Start with a smaller diamond! Then make it bigger once you figure out the pattern.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> &
#   >> ~
#
#     ~~~~~~$~~~~~~
#     ~~~~~$$$~~~~~
#     ~~~~$$$$$~~~~
#     ~~~$$$$$$$~~~
#     ~~$$$$$$$$$~~
#     ~$$$$$$$$$$$~
#     $$$$$$$$$$$$$
#     ~$$$$$$$$$$$~
#     ~~$$$$$$$$$~~
#     ~~~$$$$$$$~~~
#     ~~~~$$$$$~~~~
#     ~~~~~$$$~~~~~
#     ~~~~~~$~~~~~~
#
# ---- WRITE CODE BELOW ---- #
diamond = input('Enter a symbol: ')
print('~'*10+ diamond*1 +'~'*10)
print('~'*9+ diamond*3 +'~'*9)
print('~'*8+ diamond*5 +'~'*8)
print('~'*7+ diamond*7 +'~'*7)
print('~'*6+ diamond*9 +'~'*6)
print('~'*5+ diamond*11 +'~'*5)
print('~'*4+ diamond*13 +'~'*4)
print('~'*5+ diamond*11 +'~'*5)
print('~'*6+ diamond*9 +'~'*6)
print('~'*7+ diamond*7 +'~'*7)
print('~'*8+ diamond*5 +'~'*8)
print('~'*9+ diamond*3 +'~'*9)
print('~'*10+ diamond*1 +'~'*10)