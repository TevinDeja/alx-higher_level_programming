#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_to_int_mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0
    index = 0

    while index < len(roman_string):
        current_symbol = roman_string[index]
        next_symbol = roman_string[index + 1] if index + 1 < len(roman_string) else None

        if next_symbol is not None and roman_to_int_mapping[next_symbol] > roman_to_int_mapping[current_symbol]:
            result += roman_to_int_mapping[next_symbol] - roman_to_int_mapping[current_symbol]
            index += 2
        else:
            result += roman_to_int_mapping[current_symbol]
            index += 1

    return result
