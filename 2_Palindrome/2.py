# Palindrome Checker - Optimized for both numbers and strings


def isPalindrome(x):
    # Convert to string and remove non-alphanumeric characters
    s = str(x)
    s = "".join(c for c in s if c.isalnum()).lower()

    # Check if the cleaned string is a palindrome
    return s == s[::-1]


print(isPalindrome(121))  # expected true
print(isPalindrome("A man, a plan, a canal: Panama"))  # expected true
print(isPalindrome("race a car"))  # expected false
