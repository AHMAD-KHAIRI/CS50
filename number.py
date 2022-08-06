# CS50P - Lecture 3 - Exceptions
# 06082022

# x = int(input("What's x? "))
# print(f"x is {x}")

# when programming, anticipate that the user might not follow instructions thus creating bugs/errors
# For the example above, when asked to input an integer, the user might typed in a string e.g. cat
# This will result in a ValueError
# In Python, we can use the function try and except like the example below:
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
