"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

#name input
name = input("Hello! Please print first and last name.: ")
while name == "":
    print("Field cannot be blank!")
    name = input("Please enter first and last name.: ")

#age verification
age = 0
while age < 5 or age > 18:
    try:
        age = int(input("Age of the student: "))
        if age < 5 or age > 18:
            print("Error. Age is not in range, please enter again.")
    except ValueError:
        print("Error, please print a whole number.")
        age = 0 

#ticket section
tickets = 0
while tickets < 1 or tickets > 10:
    try:
        tickets = int(input("Please enter the number of tickets from 1 to 10.: "))
        if tickets < 1 or tickets > 10:
            print("Error, entry must be between 1 and 10.")
    except ValueError:
        print("Please enter a number from 1 to 10.")
        tickets = 0

#chaperones
chaperone = ""
while chaperone.upper() != "Y" and chaperone.upper() != "N":
    chaperone = input("Is a chaperone present? (Y/N): ")
    if chaperone.upper() != "Y" and chaperone.upper() != "N":
        print("Error: Please enter Y or N.")


