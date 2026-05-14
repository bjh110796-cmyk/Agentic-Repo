"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator
DATE: [Insert Date]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Print the final price formatted as currency (e.g., $16.95).
-----------------------------------------------------------------------
"""

#Intro and Greeting
age = int(input("Hi! How old is the customer?: "))

#start of age strings
if age < 1:print("Cost is $0.")

elif age == 1:print("Cost is $1.")

elif age == 2:print("Cost is $2.")

elif age == 3:print("Cost is $3.")

elif age == 4:print("Cost is $4.")

elif age == 5:print("Cost is $5.")

elif age == 6:print("Cost is $6.")

elif age == 7:print("Cost is $7.")

elif age == 8:print("Cost is $8.")

elif age == 9:print("Cost is $9.")

elif age == 10:print("Cost is $10.")

elif age == 11:print("Cost is $11.")

elif age >= 12:print("Cost is standard price of $16.95.")

elif age >= 65:print("Cost is discounted price of $12.95.")
#end of age strings
