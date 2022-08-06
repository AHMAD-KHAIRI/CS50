# CS50P - Lecture 3 - Exceptions
# 06082022

# x = int(input("What's x? "))
# print(f"x is {x}")

# when programming, anticipate that the user might not follow instructions thus creating bugs/errors
# For the example above, when asked to input an integer, the user might typed in a string e.g. cat
# This will result in a ValueError
# In Python, we can use the function try and except like the example below:
# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

# In the example below, when the user typed in a string, NameError was generated 
# NameError: name 'x' is not defined
# This is because the value of x was not saved 
# The solution is to use else for the last print statement
# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")


# using an infinite loop 'while' and 'break' to exit the loop
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")


# make it into a function using def so that it can be used back again
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x

# tighten up the code
# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")


# how to handle an exception/error in python but want to silently ignore it, we can use 'pass'
# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             pass


# tighten up the code even more
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()