"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[ ] 3. Program takes a word and uppercases it.
[ ] 4. Program loops through letters and prints NATO words.
[ ] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
"""
NATO_ALPHABET = {
    "A": "Alpha",   "B": "Bravo",   "C": "Charlie", "D": "Delta",
    "E": "Echo",    "F": "Foxtrot", "G": "Golf",    "H": "Hotel",
    "I": "India",   "J": "Juliet",  "K": "Kilo",    "L": "Lima",
    "M": "Mike",    "N": "November","O": "Oscar",   "P": "Papa",
    "Q": "Quebec",  "R": "Romeo",   "S": "Sierra",  "T": "Tango",
    "U": "Uniform", "V": "Victor",  "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee",  "Z": "Zulu",
}
word = input("Enter word to spell: ").upper()

print(f"\nNATO Translation for '{word}':")
print("-" * 30)

for char in word:
    try:
        if char == " ":
            print("[SPACE]")
        else:
            print(f"  {char}  →  {NATO_ALPHABET[char]}")
    except KeyError:
        print(f"  {char}  →  ['{char}' is not a letter — skipped]")

# TODO: Loop through each character
# TODO: try to print the NATO code, except if character is missing