# print out the vertical bricks like in mario
# print("#")
# print("#")
# print("#")

# use for loop and range
# for _ in range(3):
#     print("#")

# use functions
# def main():
#     print_column(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")

# different way to do this
# def print_column(height):
#     print("#\n" * height, end="")

# main()

# print out the horizontal ? bricks like in mario
# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

# main()

# print out 3 x 3 squares/bricks like in mario
def main():
    print_square(3)

# def print_square(size):

#     # For each row in square
#     for i in range(size):

#         # For each brick in row
#         for j in range(size):

#             # Print brick
#             print("#", end="")
        
#         # Print blank new line
#         print()

# we can also do like this
# def print_square(size):
#     for i in range(size):
#         print("#" * size)

# or like this
def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()