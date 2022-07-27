# define function

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()    

# float data type
# Ask user to input a number
# nested float data type with input function
x = float(input("What's x? "))
y = float(input("What's y? "))

# Do the math calculation 
# and round the numbers to 2 digits precision
z = x + y
# z = round(x + y, 2)

# Prints out the results
# using f strings to round the numbers to 2 digits precision and separated by comma
print(f"{z:,.2f}")

# using f strings to include comma as separator for 3 digits of numbers
# print(f"{z:,}")

# using the round function where the number will be rounded to 2 digits precision 
# print(f"{round(z,2):,}")

# --------------------------------------------------------------------------------
# int data type

#  method 2: nesting int data type with input function and saving it in a variable
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# print(x + y)

# method 1
# x = 1
# y = 2

# z = int(x) + int (y)

# print(z)