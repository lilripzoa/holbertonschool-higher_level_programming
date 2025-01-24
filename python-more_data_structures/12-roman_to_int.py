#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    num = 0
    for i in range(len(roman_string)):
        if i > 0:
            prev_value = roman_dict[roman_string[i - 1]]
            curr_value = roman_dict[roman_string[i]]
            num += curr_value - 2 * prev_value
        if roman_dict[roman_string[i]] > roman_dict[roman_string[i - 1]]:
            prev_value = roman_dict[roman_string[i - 1]]
            curr_value = roman_dict[roman_string[i]]
            num += curr_value - 2 * prev_value
        else:
            num += roman_dict[roman_string[i]]
    return num
