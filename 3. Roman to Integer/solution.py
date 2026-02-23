def roman_to_int(s: str) -> int:
    numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    total = 0
    i = 0
    while i < len(s):
    # Check for subtractive combination like IV, IX, XL, etc.
    # commit: handle cases where a smaller numeral precedes a larger one
        if i + 1 < len(s) and numbers[s[i]] < numbers[s[i + 1]]:
            total += numbers[s[i + 1]] - numbers[s[i]]
            i += 2
        else:
            total += numbers[s[i]]
            i += 1
    # commit: return the final integer result
    return total
