"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""

# -----------------------------------------------------------------------
# PHASE 1: Read and parse menu_config.txt into a dictionary
# -----------------------------------------------------------------------
 
menu_dict = {}  
 
try:
    with open("menu_config.txt", "r") as config_file:
        for line in config_file:
            line = line.strip()
            if not line:          
                continue
 
            
            parts       = line.split(",")
            category    = parts[0]
            items       = parts[1].split("/")
            prices      = parts[2].split("/")
 
            menu_dict[category] = dict(zip(items, prices))
 
except FileNotFoundError:
    print("ERROR: 'menu_config.txt' was not found.")
    print("Please make sure the file is in the same folder as this script.")
    exit()         
 
 
burgers  = menu_dict.get("Burgers",  {})
drinks   = menu_dict.get("Drinks",   {})
sides    = menu_dict.get("Sides",    {})
desserts = menu_dict.get("Desserts", {})
 
 
def print_category(name, items):
   
    print(f"  {' ' + name")
    print(f"  {'Item':<22} {'Price':>10}")
    for item, price in items.items():
        print(f"  {item:<22} ${float(price):>8.2f}")
 
print("RESTAURANT MENU CONFIGURATION")
 
print_category("BURGERS",  burgers)
print_category("DRINKS",   drinks)
print_category("SIDES",    sides)
print_category("DESSERTS", desserts)
 
print(f"  Total categories loaded: {len(menu_dict)}")

