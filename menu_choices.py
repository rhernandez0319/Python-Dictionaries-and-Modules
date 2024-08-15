# Display the menu.

def get_menu_choice():
    print()
    print("Name of Performer and the Location where seen.")
    print("________________________________________")
    print("1. Look up Performer")
    print("2. Add a new Performer")
    print("3. Change a Location")
    print("4. Delete a Performer")
    print("5. Display the Performer and Location")
    print("6. QUIT")
    print()
    # Get the user's choice.
    choice = int(input('Enter your choice: '))
    return choice
