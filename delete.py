# Deletes an entry from the dictionary.

def delete(performers):
    # Get a name to lookup.
    name = input("Enter a name Performer:")
    # if the name is found, delete the entry.
    if name in performers:
        del performers[name]
    else:
        print("That name is not found.")
