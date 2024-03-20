#!/usr/bin/python3
def roman_to_int(roman_string):
     if not isinstance(roman_string, str):
        return 0
    roman_numeral_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    for i in range(len(roman_string)):
        current_value = roman_numeral_map[roman_string[i]]
        if i > 0 and current_value > roman_numeral_map[roman_string[i - 1]]:
            result += current_value - 2 * roman_numeral_map[roman_string[i - 1]]
        else:
            result += current_value

    return result
