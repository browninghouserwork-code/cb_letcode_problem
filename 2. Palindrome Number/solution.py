def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    if x != 0 and x % 10 == 0:
        return False
    y = x
    m = 0
    # Commit: Reverse the number digit by digit
    while x > 0:
        n = x % 10
        m = m * 10 + n
        x //= 10
    # Commit: Check if the reversed number equals the original
    return m == y


