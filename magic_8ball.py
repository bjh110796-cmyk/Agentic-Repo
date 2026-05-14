"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""
import random

# TODO: Create a tuple of at least 8 responses
RESPONSES = ("Yes", "No", "Maybe", "Ask again later")

print("Welcome to the Digital Oracle!")

# TODO: Create a while loop that keeps asking questions
# TODO: Use random.choice(RESPONSES) to answer
# TODO: If user types "quit", break the loop

import random

RESPONSES = (
    "It is certain.",
    "Without a doubt.",
    "You may rely on it.",
    "Yes, definitely.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Don't count on it.",
    "My sources say no.",
    "Very doubtful.",
    "Outlook not so good.",
)

print("Welcome to the Digital Oracle!")
print("Ask me anything... or type 'quit' to leave.\n")

while True:
    question = input("🎱 Your question: ").strip()

    if "quit" in question.lower():
        print("The Oracle has spoken its last. Farewell!")
        break

    if question == "":
        print("The Oracle senses... nothing. Please ask a real question!\n")
        continue

    answer = random.choice(RESPONSES)
    print(f"🔮 {answer}\n")