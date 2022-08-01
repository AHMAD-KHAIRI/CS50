# CS50P - Lecture 2 - Loops
# Made by AK on 30072022

# print("Meow")
# print("Meow")
# print("Meow")

# Ask the user how many times to repeat printing meow
# n = int(input("How many times to Meow? "))
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
# i = 0
# while i < 3:
#     print("Meow")
#     i += 1

# Introduction of for loop and list [] data type
# for i in [0, 1, 2]:
#     print("Meow")

# use the function range to replace the list
# for i in range(3):
#     print("Meow")

# use _ as special identifier in Python without a variable name that stores the last result 
# for _ in range(3):
#     print("Meow")

# one step further to improve the code taking advantage of python features
# print("Meow\n" * 3, end="")

# while True:
#     n = int(input("What's n? "))
#     if n < 0:
#         continue
#     else:
#         break

# or do like this:
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("Meow")

# create functions to print meow
# first create the main function
def main():
    # declare a variable (number) to prompt the user for a number from another function (get_number)
    number = get_number()
    # once we get the number, call up the function to print Meow 'n' times
    meow(number)

# create a function that prompts the user for a +ve number using a loop
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break    
    return n

# create a function that will loop 'n' times and print Meow
def meow(n):
    for _ in range (n):
        print("Meow")

# call up the main function
main()