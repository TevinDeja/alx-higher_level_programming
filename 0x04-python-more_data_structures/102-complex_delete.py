#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Use a dictionary comprehension to filter out keys with the specified value
    a_dictionary = {key: val for key, val in a_dictionary.items() if val != value}
    return a_dictionary
