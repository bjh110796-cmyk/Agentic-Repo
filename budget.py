"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""



gross_income = float(input("Please enter your monthly income: "))
print(f"${gross_income}")

food_money = float(input("How much do you spend in food each month?: "))
print(f"${food_money}")

rent = float(input("How much is your monthly rent or mortgage?: "))
print(f"${rent}")

insurance = float(input("How much is insurance each month?: "))
print(f"${insurance}")

subscriptions = float(input("How much are your subscriptions each month?: "))
print(f"${subscriptions}")

misc = float(input("Any other monthly fees or charges?: "))
print(f"${misc}")

final_tally = gross_income - food_money - rent - insurance - subscriptions - misc
print(f"${final_tally} is your money left over for the month.")

ratio = final_tally / gross_income * 100
print(f"{ratio,:.2%}")
