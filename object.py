"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: Object practice
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class for a part of your project using PascalCase.
[ ] 3. Use __init__ to set private attributes (__variable).
[ ] 4. Write Setters and Getters for the attributes.
[ ] 5. Write a summary function that returns a formatted description.
[ ] 6. Instantiate two distinct objects and print their summaries.
-----------------------------------------------------------------------
"""

class MenuItem:
 
    def __init__(self, name, category, price, in_stock):
        self.__name      = name       
        self.__category  = category    
        self.__price     = price       
        self.__in_stock  = in_stock    
 
 
    def get_name(self):
        return self.__name
 
    def get_category(self):
        return self.__category
 
    def get_price(self):
        return self.__price
 
    def get_in_stock(self):
        return self.__in_stock
 
    def set_name(self, name):
        self.__name = name
 
    def set_category(self, category):
        self.__category = category
 
    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("ERROR: Price cannot be negative.")
 
    def set_in_stock(self, in_stock):
        self.__in_stock = in_stock
 
    def summary(self):
        status = "In Stock" if self.__in_stock else "Out of Stock"
        return (
            f"  {'MENU ITEM SUMMARY':}\n"
            f"  {'Name:':<14} {self.__name}\n"
            f"  {'Category:':<14} {self.__category}\n"
            f"  {'Price:':<14} ${self.__price:.2f}\n"
            f"  {'Availability:':<14} {status}\n")
 
item1 = MenuItem(
    name      = "Bacon Burger",
    category  = "Burgers",
    price     = 10.99,
    in_stock  = True)
 
item2 = MenuItem(
    name      = "Apple Pie",
    category  = "Desserts",
    price     = 3.49,
    in_stock  = False)

print(item1.summary())
print(item2.summary())
  
print("\n  -- Restocking Apple Pie... --")
item2.set_in_stock(True)
item2.set_price(3.99)
print(item2.summary())