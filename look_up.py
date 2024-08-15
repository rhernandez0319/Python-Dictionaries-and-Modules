# Look up function looks up an Artists name.

def look_up_artist(performers):
    name = input("Enter a mame:")
    # Look up in dictionary.
    print(performers.get(name, "Not Found"))
    return name
