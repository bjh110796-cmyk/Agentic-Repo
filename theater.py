"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

seats = list(range(1,21))

print("Welcome to CMA Theaters!")

while seats > 0:
    print("Available seats {seats} remaining:")
    print(seats)

    user_input = input("Please enter a seat number to purchase or press 0 to exit.")
    seat_choice = int(user_input)

    if seat_choice == 0:
        print("Thank you for your selection!")

    if seat_choice < 1 or seat_choice < 20:
        print("Error, seat doesn't exist, please make another selection.")

    if seat_choice not in seats:
        print("Error, seat {seat_choice} has been taken, please make another selection.")
    
    seats.remove(seat_choice)
    print("Thank you! Seat has been purchased!")

    if seats == 0:
        print("All seats have been sold, have a nice day and enjoy the show!")