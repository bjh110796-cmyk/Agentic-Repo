"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
"""

MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

print("The Locked Calender")
print("All months of the year: ")

for month in MONTHS:
    print(f" {month}")

#attempting the error
print("Attempting to error the calender")

try:
    MONTHS[0] = "Januwary"
except TypeError as e:
    print("Modification Failed! TypeError: {e}")
    print("Tuples are immutable and cannot be changed.")

print("The Calender is unchanged.")
print(MONTHS)
