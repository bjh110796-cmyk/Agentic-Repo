"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

#start of inputs
num1 = float(input("Please enter a number: "))

num2 = float(input("Please enter a second number: "))

#check #1
both_positive = num1 > 0 and num2 > 0
print(f"Both numbers are positive.")

#check #2
both_over100 = num1 > 100 and num2 > 100
print(f"Both numbers are greater than 100.")

#check #3
even = num1 %2 == 0 or num2 %2 == 0
print(f"Both numbers are even.")

#check #4
both_neither100 = num1 < 100 and num2 < 100
print(f"Both are less than 100.")

#check #5
not_equal = num1 != num2
print(f"Neither numbers are equal.")

#check #6
not_zero = num1 != 0 and num2 != 0
print(f"Neither are not equal to zero.")

#if/elif/else checks
if num1 > 0: print(f"Number 1 is positive.")

elif num1 < 0: print(f"Number 1 is negative.")

else: print(f"Number 1 is 0.")