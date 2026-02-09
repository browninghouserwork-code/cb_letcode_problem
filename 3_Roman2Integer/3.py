# 13. Roman to Integer
# Given a roman numeral, convert it to an integer.
# Example 1:
# Input: s = "III"
# Output: 3
# Example 2:
# Input: s = "IV"
# Output: 4
# Example 3:
# Input: s = "IX"
# Output: 9


def roman_to_int(s):
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    prev_value = 0

    for char in s:
        value = roman_numerals[char]
        if prev_value < value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value

    return total


print(roman_to_int("III"))  # expected 3
print(roman_to_int("IV"))  # expected 4
print(roman_to_int("IX"))  # expected 9
print(roman_to_int("LVIII"))  # expected 58
print(roman_to_int("MCMXCIV"))  # expected 1994
print(roman_to_int("MMXXIV"))  # expected 2024
