# This function will retrieve the dictionary.
import pickle

def retrieve():
    input_file = open("info.dat", "rb")
    x = pickle.load(input_file)
    input_file.close()
    return x
