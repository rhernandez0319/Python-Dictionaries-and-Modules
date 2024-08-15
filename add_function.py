# Add a new entry.

def add(performers):
    # Get a name and Venue.
    name = input("Enter a name of a Performer:")
    location = input("Enter the name of the Location:")
    if name not in performers:
        performers[name] = location
    else:
        print("That entry already exists")
