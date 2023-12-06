#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        return None
    best_score = a_dictionary[next(iter(a_dictionary))]
    best_key = next(iter(a_dictionary))
    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
            best_key = key
    return best_key
