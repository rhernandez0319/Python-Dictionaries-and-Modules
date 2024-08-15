# Changes an existing entry.

def change(performers):
    # Get a name to lookup.
    name = input("Enter a name of a Performer:")

    if name in performers:
        # Enter a new location.
        location = input("Enter a new location:")
        # Update the entry.
        performers[name] = location
    else:
        print("The name is not found.")
