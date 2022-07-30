# third exercise 

# Ask the user
# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# use the method to define function
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# improvement on the function is_even 
# def is_even(n):
#     return True if n % 2 == 0 else False

#  more improvement on is_even
def is_even(n):
    return n % 2 == 0

main()