def add_binary(a: str, b: str) -> str:
    result = []
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    while i >= 0 or j >= 0 or carry:
        if i >= 0: digit_a = int(a[i])
        else: digit_a = 0
        if j >= 0: digit_b = int(b[j])  
        else: digit_b = 0         

        total = digit_a + digit_b + carry
        result.append(str(total % 2))
        
        carry = total // 2
        
        i -= 1
        j -= 1
    
    return ''.join(reversed(result))
