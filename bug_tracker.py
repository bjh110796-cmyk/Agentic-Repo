"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""

import datetime

PRIORITIES = ("Low", "Medium", "High", "Critical")


def get_priority() -> str:
    
    print("Priority Levels:")
    for i, level in enumerate(PRIORITIES, 1):
        print(f"{i}. {level}")

    while True:
        choice = input("Choose a priority (1-4): ").strip()
        if choice in ("1", "2", "3", "4"):
            return PRIORITIES[int(choice) - 1]
        print("Invalid choice — please enter 1, 2, 3, or 4.")


def build_bug(file_name: str, description: str, priority: str) -> dict:
   
    return {
        "timestamp"  : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "file_name"  : file_name,
        "description": description,
        "priority"   : priority,
    }


def save_bug(bug: dict) -> None:
    with open("bug_log.txt", "a") as log:
        log.write(f"BUG REPORT")
        log.write(f"Timestamp  : {bug['timestamp']}")
        log.write(f"File       : {bug['file_name']}")
        log.write(f"Priority   : {bug['priority']}")
        log.write(f"Description: {bug['description']}")


def main() -> None:
    print("Welcome to the Bug Tracking Log!")
    print("   Type 'quit' at any prompt to exit.")

    bugs_logged = 0

    while True:
        print("New Bug Entry")

        file_name = input("File name (e.g. main.py): ").strip()
        if file_name.lower() == "quit":
            break
        if not file_name:
            print("File name cannot be blank.")
            continue

        description = input("Bug description: ").strip()
        if description.lower() == "quit":
            break
        if not description:
            print("Description cannot be blank.")
            continue

        priority = get_priority()

        bug = build_bug(file_name, description, priority)
        save_bug(bug)
        bugs_logged += 1

        print(f"Bug #{bugs_logged} logged successfully — [{priority}] in {file_name}")

    print(f"Session ended. {bugs_logged} bug(s) saved to bug_log.txt.\n")


main()