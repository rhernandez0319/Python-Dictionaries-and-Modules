# This Function will pickle the dictionary to a file.
import pickle


def save(performers):
    output_file = open("info.dat", "wb")
    pickle.dump(performers, output_file)
    output_file.close()
