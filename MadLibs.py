"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Assignment Name, Date, File Name).
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

name = input("Please enter a name: ")
noun = input("Please enter a noun: ")

print(f"{name} was walking down the street when they saw a {noun}")
print(f"\n\n{name} was walking down the street when they saw a {noun}")

name2 = input("Please enter another name: ")
verb = input("Please enter a verb: ")

print(f"{name2} saw {name} and then proceeded to {verb} them")
print(f"\n\n{name2} saw {name} and then proceeded to {verb} them")

animal = input("Please enter an animal: ")
verb2 = input("Please enter another verb: ")

print(f"{name} and {name2} then ran into a {animal}, then {verb2} the {animal}")

vehicle = input("Please enter a vehicle: ")
result = input("Please enter what happens to the vehicle: ")

print(f"Then, from nowhere, a {vehicle} came around and then {result}")
print(f"\n\nThen, from nowhere, a {vehicle} came around and then {result}")

plane = input("Please enter an aircraft: ")
finalaction = input("Please enter a Finale to the MadLib: ")

print(f"Then, a {plane} flew by and {finalaction}, and everyone laughed")
print(f"\n\nThen, a {plane} flew by and {finalaction}, and everyone laughed")

#The End