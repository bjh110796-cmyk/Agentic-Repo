"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

TOPPINGS = ("Pepperoni","Mushrooms","Black Olives","Green Peppers","Sausage","Extra Cheese")

SIZES = {"S": ("Small",  8.99), "M": ("Medium", 11.99), "L": ("Large",  14.99)}
DELIVERY_FEE = 2.50

def make_pizza(customer: str, size: str, topping: str, is_delivery: bool = False):
    
    size_label, base_price = SIZES.get(size.upper(), ("Medium", 11.99))
    total = base_price + (DELIVERY_FEE if is_delivery else 0)
    delivery_label = "Delivery" if is_delivery else "Office Pickup"

    print("MONTY'S PIZZA PARTY")
    print(f"Customer: {customer}")
    print(f"Size: {size_label}")
    print(f"Topping: {topping}")
    print(f"Order Type: {delivery_label}")
    print(f"Base Price:$ {base_price:.2f}")
    if is_delivery:
        print(f"Delivery: ${DELIVERY_FEE:.2f}")
    print(f"{'TOTAL':10}: ${total:.2f}")
    print(f"Thank you, {customer.split()[0]}! Your pizza is on its way!")


def main():
    print("Welcome to Monty's Office Pizza Party!🎉")

    print("Available Toppings: ")
    for i, topping in enumerate(TOPPINGS, 1):
        print(f" {i}. {topping}")

    print("\nAvailable Sizes: ")
    for key, (label, price) in SIZES.items():
        print(f" {key}. {label:8} — ${price:.2f}")

    print()
    customer = input("Enter your name: ").strip().title()

    size_input = input("Choose a size (S / M / L): ").strip().upper()
    if size_input not in SIZES:
        print("Invalid size — defaulting to Medium.")
        size_input = "M"

    try:
        topping_choice = int(input(f"Choose a topping (1-{len(TOPPINGS)}): ").strip())
        if not 1 <= topping_choice <= len(TOPPINGS):
            raise ValueError
        topping = TOPPINGS[topping_choice - 1]
    except ValueError:
        print("Invalid choice — defaulting to Pepperoni.")
        topping = TOPPINGS[0]

    delivery_input = input("Is this a delivery? (y / n): ").strip().lower()
    is_delivery = delivery_input == "y"

    make_pizza(
        customer=customer,
        size=size_input,
        topping=topping,
        is_delivery=is_delivery,
    )


main()