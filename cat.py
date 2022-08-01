# CS50P - Lecture 2 - Loops
# Made by AK on 30072022

# print("Meow")
# print("Meow")
# print("Meow")

# Ask the user how many times to repeat printing meow
# n = int(input("How many times? "))
# i = n

# Introduction of while loop
# First we initialize how many times we want the loop to repeat
# i = 3
# # Next, do the while loop and check if i is not equal to 0. If true then print meow and move down. If false then stop
# while i != 0:
#     print("Meow")
#     # After printing meow, do the calculation (e.g. i = 3 - 1 = 2) and return to while loop and check again
#     # i = i - 1
#     i -= 1

# or we do it this way by convention
i = 0
while i < 3:
    print("Meow")
    i += 1

# Introduction of for loop and list [] data type
for i in [0, 1, 2]:
    print("Meow")

# use the function range to replace the list
for i in range(3):
    print("Meow")

# use _ as special identifier in Python without a variable name that stores the last result 
for _ in range(3):
    print("Meow")