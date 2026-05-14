"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")

def get_price(size: float):
    
    prices = {"Small": 4.99, "Medium": 6.49, "Large": 7.99}
    return prices[size]

def blend(size: str, base: str, fruit: str, scoops: int):
    
    price     = get_price(size)
    scoop_fee = (scoops - 1) * 0.75        
    total     = price + scoop_fee

    print("🥤 SMOOTHIE SPRINT ORDER 🥤")
    print(f"Size: {size}")
    print(f"Base: {base}")
    print(f"Fruit: {fruit}")
    print(f"Scoops: {scoops}")
    print(f"Base Price: ${price:.2f}")
    if scoop_fee > 0:
        print(f"Extra Scoops:  ${scoop_fee:.2f}  ({scoops - 1} extra @ $0.75 each)")
    print(f"  {'TOTAL':11}:  ${total:.2f}")
    print("  Blending your smoothie... 🌀 Enjoy!")

def main():
    print("🍓 Welcome to Smoothie Sprint! 🍓")

    sizes = ("Small", "Medium", "Large")
    print("Sizes available:")
    for i, s in enumerate(sizes, 1):
        print(f"{i}. {s:8} — ${get_price(s):.2f}")

    size_choice = input("Choose a size (1-3): ").strip()
    size = sizes[int(size_choice) - 1] if size_choice in ("1", "2", "3") else "Medium"

    print("\nBases available:")
    for i, b in enumerate(BASES, 1):
        print(f"{i}. {b}")

    base_choice = input("Choose a base (1-4): ").strip()
    base = BASES[int(base_choice) - 1] if base_choice in ("1", "2", "3", "4") else BASES[0]

    print("\nFruits available:")
    for i, f in enumerate(FRUITS, 1):
        print(f"{i}. {f}")

    fruit_choice = input("Choose a fruit (1-4): ").strip()
    fruit = FRUITS[int(fruit_choice) - 1] if fruit_choice in ("1", "2", "3", "4") else FRUITS[0]

    try:
        scoops = int(input("\nHow many scoops of fruit? (1-5): ").strip())
        if scoops < 1 or scoops > 5:
            raise ValueError
    except ValueError:
        print("⚠️  Invalid scoop count — defaulting to 1 scoop.")
        scoops = 1

    blend(size, base, fruit, scoops)


main()

# TODO: Define get_price(size)

# TODO: Define blend(size, base, fruit, scoops)

# TODO: Define main() to collect input and call your logic