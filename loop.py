"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# variables
arrival = False
while arrival: print("Are we there yet?")
answer = input("Have we arrived? Yes or No?: ")

#boolean variable
if answer == "yes": arrival == True
print("We are here!")

#99 bottles of beer
for bottles in range(99, 0, -1):
    if bottles > 1:
        print(f"{bottles} bottles of beer on the wall!")
    else: print(f"{bottles} bottle of beer on the wall!")
