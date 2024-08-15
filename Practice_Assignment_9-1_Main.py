# Create a dictionary, application, subject of your choosing.
# In addition to menu choices provided to the user. Add menu items to display the entire dictionary.
# Main Program
# Look up and display function.
# Add Function.
# Change and Delete Function.
import menu_choices
import look_up
import add_function
import change
import delete
import display

# Global constants for menu choices.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
DISPLAY = 5
QUIT = 6


# This program uses a dictionary to keep music Performers and Location of were seen.
def main():
    # Create an empty dictionary.
    performers = {}

    # Initiate a variable for the user's choice.
    choice = 0
    while choice != QUIT:
        # Get the user's menu choice.
        choice = menu_choices.get_menu_choice()

        # Validate the choice.
        while choice < LOOK_UP or choice > QUIT:
            choice = int(input('Enter a valid choice: '))

        # Process the choice.
        if choice == LOOK_UP:
            look_up.look_up_artist(performers)
        elif choice == ADD:
            add_function.add(performers)
        elif choice == CHANGE:
            change.change(performers)
        elif choice == DELETE:
            delete.delete(performers)
        elif choice == DISPLAY:
            display.display(performers)


if __name__ == '__main__':
    main()
