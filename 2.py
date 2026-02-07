def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    if x != 0 and x % 10 == 0:
        return False
    y = x
    m = 0
    while x > 0:
        n = x % 10
        m = m * 10 + n
        x //= 10
    return m == y


