# Import necessary modules
import main_part as mp

# Function to display the main menu options and prompt the user for input
def display_main_menu():
    print("1. Filter by Neighbourhood")
    print("2. Filter by Room type")
    print("3. Filter by Capacity")
    print("4. Filter by Price")
    print("5. Filter by Review Score")
    print("6. Show the result")
    print("7. Exit the program")
    choice = input("Choose accommodation according to your parameters. Enter your choice (1-7): ")
    return choice

# Main menu program loop
while True:
    choice = display_main_menu()
    
    if choice == '1':
        mp.neighbourhood()
    elif choice == '2':
        mp.room()
    elif choice == '3':
        mp.capacity()
    elif choice == '4':
        mp.price()
    elif choice == '5':
        mp.rating()
    elif choice == '6':
        mp.result()
    elif choice == '7':
        print("Exiting the program. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")