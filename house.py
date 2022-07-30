#  fourth exercise in CS50P - Lecture 1 - Conditionals
# prompts user for their name and outputs their house in Harry Potter

name = input("What's your name? ")

# use if elif else statements
# if name == "Harry" or "Hermione" or "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# Introduction of match conditional statement as alternative to if conditional statement
match name:
    case "Harry"| "Hermione" | "Ron":
    # case "Hermione":
    # case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")