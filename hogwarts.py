# make a list
# students = ["Hermione", "Harry", "Ron", "Draco"]

# print(students[0])

# make a loop
# for student in students:
#     print(student)

# or we can use len for length to check the length of the list
# for i in range(len(students)):
#     print(i + 1, students[i])

# introduction of new data type: dict / dictionaries - associate one value with another
# dict allows you to associate something with something else aka key: value pair

# make another list
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# how to use dict
# students = {
#     "Hermione": "Gryffindor", 
#     "Harry": "Gryffindor", 
#     "Ron": "Gryffindor", 
#     "Draco": "Slytherin"
#     }

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# use for loop with dict to replace multiple print functions and how to call up the value in the dict
# for student in students:
#     print(student, students[student], sep=", ")

# adding another column to the list
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
# special keyword in Python: None --> absence of a value
# keys: name, house, patronus
# values: Hermione, Gryffindor, Otter

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")