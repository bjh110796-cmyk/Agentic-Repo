"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. ATM runs in a "while True" loop to remain awake.
[ ] 3. Main menu uses match-case logic for selections.
[ ] 4. Inputs are validated (e.g., .isdigit()) to prevent crashes.
[ ] 5. Logic prevents overdrafts and negative deposits.
[ ] 6. All currency is formatted to two decimal places (:.2f).
[ ] 7. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

balance = 1000.00

print("Welcome to Brandon's Atm!")

while True:
    print("Main menu.")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input(" Enter a selection: ").strip()

    match choice:
        case "1":
            print(f"Your current balance is: ${balance:.2f}")

        case "2":
            amount_input = input("Enter deposit amount:$ ").strip()

            if not amount_input.replace(".", "", 1).isdigit():
                print("Error: Please enter a valid number.")
            else:
                amount = float(amount_input)
                if amount <= 0:
                    print("Error: Deposit amount must be greater than $0.00.")
                else:
                    balance += amount
                    print(f"Successfully deposited ${amount:.2f}.")
                    print(f"New balance: ${balance:.2f}")

        case "3":
             amount_input = input("Enter withdrawal amount:$ ").strip()

             if not amount_input.replace(".", "", 1).isdigit():
                print("Error: Please enter a valid number.")
             else:
                amount = float(amount_input)
                if amount <= 0:
                    print("Error: Withdrawal amount must be greater than $0.00.")
                elif amount > balance:
                    print(f"Error: Insufficient funds. Your balance is only ${balance:.2f}.")
                else:
                    balance -= amount
                    print(f"Successfully withdrew ${amount:.2f}.")
                    print(f"New balance: ${balance:.2f}")

        case "4":
            print(f"Final balance: ${balance:.2f}")
            print("Thank you for using Python ATM. Goodbye!")
            break

        case _:
            print("Error, please select a valid number.")
